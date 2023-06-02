from flask import Flask, render_template, request, g, session, jsonify, url_for, redirect
from models import db
from stress_management_resources import stress_management_resources
from flask_migrate import Migrate
import sqlite3, requests, hashlib, os, warnings
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import googleapiclient.discovery
from googleapiclient.discovery import build
import requests, datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = os.urandom(16)

# i kept on getting a warning about flask future upadate so i
# Ignored the FSADeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

# initialize the app with the extension
db.init_app(app)
migrate = Migrate(app, db)

#  for mySQLite
app.secret_key = 'your'
DATABASE_FILE = 'database.db'


# Function handling the hash password
def hash_password(password):
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 100000)
    return salt + password_hash

# Function handling the password checker for correctness and tallying
def check_password(password, password_hash):
    salt = password_hash[:16]
    stored_password_hash = password_hash[16:]
    new_password_hash = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 100000)
    return new_password_hash == stored_password_hash


def get_user(user_id):
    query = "SELECT id, email, first_name, last_name, username, gender, university_name, password_hash, notification_enabled, privacy_enabled FROM users WHERE id = ?"
    args = (user_id,)
    row = db_query(query, args)

    if not row:
        return None

    return {
        'id': row[0][0], 'email': row[0][1], 'first_name': row[0][2], 'last_name': row[0][3], 'username': row[0][4], 'gender': row[0][5], 'university_name': row[0][6], 'password': row[0][7], 'notification_enabled': bool(row[0][8]), 'privacy_enabled': bool(row[0][9])
        }


@app.before_request
def load_user():
    user_id = session.get('user_id')
    if user_id is not None:
        g.user = get_user(user_id)
    else:
        g.user = None


@app.route('/')
def index():
    return render_template('index.html', user=g.user)

# Route to the  blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')


# Usuage based on mySQLite

# Get a useable connection to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_FILE)
        db.row_factory = sqlite3.Row
    return db

# Close the database connection when the app shuts down
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# return the results from a database query
def db_query(query, args=None):
    cur = get_db().execute(query, args or ())
    rv = cur.fetchall()
    cur.close()
    return rv

# execute a database query
def db_execute(query, args=()):
    conn = get_db()
    conn.execute(query, args)
    conn.commit()
    return True



def replicate_table(table_name, new_table_name):
    try:
        # Retrieve column names and types for the original table
        column_data = db_query("PRAGMA table_info(%s)" % table_name)

        # Construct a new CREATE TABLE query with the same columns and types
        create_query = "CREATE TABLE %s (" % new_table_name
        for column in column_data:
            column_name = column[1]
            column_type = column[2]
            create_query += "%s %s, " % (column_name, column_type)
        create_query = create_query[:-2] + ")"

        # Execute the CREATE TABLE query for the new table
        db_execute(create_query)

        # Insert the data from the original table into the new table
        db_execute("INSERT INTO %s SELECT * FROM %s" %

                   (new_table_name, table_name))

        print("Successfully replicated %s as %s" %

              (table_name, new_table_name))
    except sqlite3.Error as e:
        if str(e).startswith('table %s already exists' % new_table_name):
            print('Table %s already exists. Please choose a different name.' %
                  new_table_name)
        else:
            print('Error replicating table:', e)

# This get the details from the table in the database


def get_meal_from_db(table_name):
    query = "SELECT * FROM {}".format(table_name)
    results = db_query(query)
    if results:
        return results
    else:
        return None

# edit made to the table is sent here where it is being sent to the databse for an update


@app.route('/update', methods=['POST'])
def update():
    name = g.user['username']  # get the username provided in the sign up page
    data = request.json
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE {} SET Breakfast = ?, Lunch = ?, Dinner = ? WHERE Date = ?'.format(
        name), (data['BreakFast'], data['Lunch'], data['Dinner'], data['Date']))
    conn.commit()
    conn.close()
    return '/meal'

# this directs users to the database were they fill the form were a table can be made for them base on their nutrional requirements


@app.route('/input')
def input():
    if g.user is not None:
        first_name = g.user["first_name"]
        return render_template('input.html', first_name=first_name)
    return redirect(url_for('signin'))


# this takes in the submitted form can provides a table for the users base on their names
@app.route('/meal', methods=["GET", "POST"])
def meal():
    if g.user is None:
        return redirect(url_for('signin'))
    
    visited = "checked your Meal"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)

   
    if request.method == "POST":

        # get the username provided in the sign up page
        name = g.user['username']
        session['name'] = name
        vegetarian = request.form['Vegetarian']
        allergies = request.form['Allergies']
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        meal = request.form['meal']
        grocery = name + '1'

        m = height * height
        bmi = weight / m

        tables = {
            ('Yes', 'Yes'): {'two': 'Allegies_UW2', 'three': 'Allegies_UW3'},
            ('Yes', 'No'): {'two': 'Vegetarian_UW2', 'three': 'Vegetarian_UW3'},
            ('No', 'Yes'): {'two': 'Allegies_UW2', 'three': 'Allegies_UW3'},
            ('No', 'No'): {'two': 'Under_weight2', 'three': 'Under_weight3'}
        }

        if bmi > 18.5:
            tables.update({
                ('Yes', 'Yes'): {'two': 'Allegies_NW2', 'three': 'Allegies_NW3'},
                ('Yes', 'No'): {'two': 'Vegetarian_NW2', 'three': 'Vegetarian_NW3'},
                ('No', 'Yes'): {'two': 'Allegies_NW2', 'three': 'Allegies_NW3'},
                ('No', 'No'): {'two': 'Normal_weight2', 'three': 'Normal_weight3'}
            })

        if bmi > 26.0:
            tables.update({
                ('Yes', 'Yes'): {'two': 'Allegies_OW2', 'three': 'Allegies_OW3'},
                ('Yes', 'No'): {'two': 'Vegetarian_OW2', 'three': 'Vegetarian_OW3'},
                ('No', 'Yes'): {'two': 'Allegies_OW2', 'three': 'Allegies_OW3'},
                ('No', 'No'): {'two': 'Over_weight2', 'three': 'Over_weight3'}
            })

        table_name = tables[(vegetarian, allergies)][meal]
        replicate_table(table_name, name)
        replicate_table(f"{table_name}_Grocery", grocery)

        groceries = get_meal_from_db(grocery)
        meal = get_meal_from_db(name)
        return render_template("meal.html", meal=meal, groceries=groceries, first_name=name)

    elif request.method == "GET":
        try:

            # get the username provided in the sign up page
            name = g.user['username']
            grocery = name + '1'
            groceries = get_meal_from_db(grocery)
            meal = get_meal_from_db(name)
            return render_template("meal.html", meal=meal, groceries=groceries, first_name=name)

        except sqlite3.OperationalError:
            return render_template('input.html')

# this provides a table for the grocery list


@app.route('/grocery')
def grocery():
    name = g.user['username']  # get the username provided in the sign up page
    grocery = name + '1'
    groceries = get_meal_from_db(grocery)
    data = []
    for row in groceries:
        data.append({'Date': row[0], 'Item': row[1]})
    return jsonify(data)


############# THE STRESS MANAGEMENT RESOUCEs ROUTE #########################


class StressManagementResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(255), nullable=True)

    def __init__(self, title, description, link):
        self.title = title
        self.description = description
        self.link = link

    def __repr__(self):
        return f"StressManagementResource(id={self.id}, title='{self.title}', link='{self.link}')"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'link': self.link
        }

# API endpoint to get all stress management resources


@app.route('/resources', methods=['GET'])
def get_stress_management_resources():
    resources = []
    for resource in stress_management_resources:
        new_resource = StressManagementResource(
            title=resource["title"],
            description=resource["description"],
            link=resource["link"]
        )
        db.session.add(new_resource)
        db.session.commit()
        resources.append(new_resource.to_dict())
    return jsonify({'resources': resources})


@app.route('/resources/<int:id>')
def get_stress_management_resource(id):
    resource = StressManagementResource.query.get(id)
    if resource is None:
        return 404
    return jsonify({'resource': resource})

# API endpoint to create a new stress management resouce


@app.route('/resources', methods=['POST'])
def create_stress_management_resources():
    data = request.get_json()
    new_resource = StressManagementResource(
        title=data['title'], description=data['description'], link=data['link'])
    db.session.add(new_resource)
    db.session.commit()
    # return jsonify({'message': 'Resource created successfully'})
    return jsonify({'resource': new_resource}), 201


@app.route('/resources/<int:id>', methods=['PUT'])
def update_stress_management_resource(id):
    data = request.get_json()
    resource = StressManagementResource.query.get(id)
    if resource is None:
        return 404
    resource.title = data['title']
    resource.description = data['description']
    resource.link = data['link']
    db.session.commit()
    return 200, {'resource': resource}


@app.route('/resources/<int:id>', methods=['DELETE'])
def delete_stress_management_resource(id):
    resource = StressManagementResource.query.get(id)
    if resource is None:
        return 404
    db.session.delete(resource)
    db.session.commit()
    return 204

############################# STRESS MANAGEMENT RESOUCE END ##########################


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        gender = request.form['gender']
        university_name = request.form['university_name']
        password = request.form['password']
        session['username'] = username

        # Hash password
        password_hash = hash_password(password)

        # Insert user into database
        query = "INSERT INTO users (email, first_name, last_name, username, gender, university_name, password_hash) VALUES (?, ?, ?, ?, ?, ?, ?)"
        args = (email, first_name, last_name, username, gender, university_name, password_hash)

        db_connection = get_db()
        cur = db_connection.cursor()
        cur.execute(query, args)
        db_connection.commit()

        # Redirect to sign-in page
        return redirect(url_for('signin'))
    
    # Render sign-up page
    return render_template('signup.html')




@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        password = request.form['password']

        # Check if user exists in database
        query = "SELECT id, password_hash FROM users WHERE email = ?"
        args = (email,)
        row = db_query(query, args)

        if not row:  # Check if row is empty
            # User not found
            error = 'Invalid email or password'
            return render_template('signin.html', error=error)

        # Check password
        password_hash = row[0][1]  # Access the first row's second element
        if check_password(password, password_hash):
            # Password is correct, store user ID in session
            session['user_id'] = row[0][0]  # Access the first row's first element
            return redirect('/home')
        else:
            # Password is incorrect
            error = 'Invalid email or password'
            return render_template('signin.html', error=error)

    # Render sign-in page
    return render_template('signin.html')




@app.route('/signout')
def signout():
    visited = "Sign out"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)

    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('signin'))


@app.route('/home')
def home():
    if g.user is None:
        return redirect(url_for('signin'))
    
    visited = "new sign in"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)


    return render_template('home.html', user=g.user)


@app.route('/stress')
def video_list():
    if g.user is None:
        return redirect(url_for('signin'))
    
    visited = "used the relaxation page"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)


    med_files = ['m1.mp4', 'm2.mp4', 'm3.mp4', 'm4.mp4', 'm5.mp4',
                 'm6.mp4', 'm7.mp4', 'm8.mp4', 'm9.mp4', 'm10.mp4', 'm11.mp4']
    pers_files = ['p1.mp4', 'p2.mp4', 'p3.mp4', 'p4.mp4', 'p5.mp4']
    relax_files = ['r1.mp4', 'r2.mp4', 'r3.p4', 'r4.mp4',
                   'r5.mp4', 'r6.mp4', 'r7.mp4', 'r8.mp4', 'r9.mp4', 'r10.mp4']
    return render_template('mental.html', meditations=med_files, personalize=pers_files, relax=relax_files)


# User settings
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/signin')

    user = get_user(user_id)
    if g.user is None:
        return redirect(url_for('signin'))
    
    visited = "Updated your settings"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)

    # selecting notification
    query = "SELECT notification_enabled FROM users WHERE id = ?"
    args = (user_id,)
    notification = db_query(query, args)

    # selecting Privacy
    query = "SELECT notification_enabled FROM users WHERE id = ?"
    args = (user_id,)
    privacy = db_query(query, args)

    # Default values for notification_enabled and privacy_enabled
    notification_enabled = notification
    privacy_enabled = privacy

    if request.method == 'POST':
        notification_enabled = bool(request.form.get('notification_enabled'))
        privacy_enabled = bool(request.form.get('privacy_enabled'))

        query = "UPDATE users SET notification_enabled = ?, privacy_enabled = ? WHERE id = ?"
        args = (notification_enabled, privacy_enabled, user['id'])
        db_connection = get_db()
        cur = db_connection.cursor()
        cur.execute(query, args)
        db_connection.commit()

        return redirect('/settings')
    print(notification_enabled, privacy_enabled)
    return render_template('settings.html', user=user, notification_enabled=notification_enabled, privacy_enabled=privacy_enabled)

# Records user usage history
def record_usage_history(user_id, route):
    timestamp = datetime.datetime.now()

    query = "INSERT INTO usage_history (user_id, route, timestamp) VALUES (?, ?, ?)"
    args = (user_id, route, timestamp)
    db_connection = get_db()
    cur = db_connection.cursor()
    cur.execute(query, args)
    db_connection.commit()

# Usage history route
@app.route('/history')
def usage_history():
    if g.user is None:
        return redirect(url_for('signin')) 

    visited = "viewed history in your calendar"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)


    query = "SELECT * FROM usage_history WHERE user_id = ? ORDER BY timestamp DESC"
    args = (user_id,)
    usage_records = db_query(query, args)

    return render_template('history.html', usage_records=usage_records)

#this creates the goal
@app.route('/create_goal', methods=['GET', 'POST'])
def create_goal():
    if g.user is None:
        return redirect(url_for('signin')) 
    
    visited = "created goal in your calendar"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)


    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        query = "INSERT INTO goals (user_id, title, description, completed) VALUES (?, ?, ?, ?)"
        args = (session['user_id'], title, description, False)
        db_connection = get_db()
        cur = db_connection.cursor()
        cur.execute(query, args)
        db_connection.commit()

        return redirect('/calendar')

    return render_template('goal.html')

# Create a milestone for a goal
@app.route('/create_milestone/<int:goal_id>', methods=['GET', 'POST'])
def create_milestone(goal_id):
    if g.user is None:
        return redirect(url_for('signin')) 
    
    visited = "create milestone in your calendar"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)

    if request.method == 'POST':
        description = request.form['description']

        query = "INSERT INTO milestones (goal_id, description, completed) VALUES (?, ?, ?)"
        args = (goal_id, description, False)
        db_connection = get_db()
        cur = db_connection.cursor()
        cur.execute(query, args)
        db_connection.commit()

        # Fetches the updated list of goals with their associated milestones
        query = "SELECT g.id, g.title, g.description, g.completed, m.id AS milestone_id, m.description AS milestone_description, m.completed AS milestone_completed FROM goals g LEFT JOIN milestones m ON g.id = m.goal_id WHERE g.user_id = ?"
        args = (session['user_id'],)
        goals = db_query(query, args)

        return render_template('calendar.html', goals=goals)
    return render_template('milestone.html', goal_id=goal_id)


# Update milestone progress
@app.route('/update_progress/<int:milestone_id>', methods=['POST'])
def update_progress(milestone_id):
    if g.user is None:
        return redirect(url_for('signin')) 
    
    visited = "updated milestone in your calendar"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)


    query = "SELECT * FROM milestones WHERE id = ?"
    args = (milestone_id,)
    milestone = db_query(query, args)
    if milestone:
        new_completed = not milestone[0]['completed']
        query = "UPDATE milestones SET completed = ? WHERE id = ?"
        args = (new_completed, milestone_id)
        db_connection = get_db()
        cur = db_connection.cursor()
        cur.execute(query, args)
        db_connection.commit()

    return redirect('/calendar')

#This gets the milestone from the db, so it can be accesed with goal using foreign keys
@app.template_global()
def get_milestones(goal_id):
    query = "SELECT * FROM milestones WHERE goal_id = ?"
    args = (goal_id,)
    milestones = db_query(query, args)
    return milestones


# Calendar route
@app.route('/calendar')
def calendar():
    if g.user is None:
        return redirect(url_for('signin')) 
    
    visited = "checked your calendar"    
    user_id = session['user_id']
    record_usage_history(user_id, visited)

    query = "SELECT * FROM goals WHERE user_id = ?" 
    args = (session['user_id'],)
    goals = db_query(query, args)

    return render_template('calendar.html', goals=goals)


    
    
if __name__ == '__main__':
    app.run(debug=True)