from flask import Flask, render_template, request, g, session, jsonify, url_for, redirect
from models import db
from flask_migrate import Migrate
import sqlite3
import hashlib
import os
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = os.urandom(16)

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
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT id, email, first_name, last_name, username, gender, university_name, password_hash FROM users WHERE id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    return {'id': row[0], 'email': row[1], 'first_name': row[2], 'last_name': row[3], 'username': row[4], 'gender': row[5], 'university_name': row[6], 'password': row[7]}


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


def db_query(query, args=()):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return rv

# execute a database query


def db_execute(script, args=()):
    conn = get_db()
    conn.execute(script, args)
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
    name = g.user['username']# get the username provided in the sign up page
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
    if g.user is None:
        return redirect(url_for('signin'))
    return render_template('input.html')



#this takes in the submitted form can provides a table for the users base on their names
@app.route('/meal', methods=["GET", "POST"])
def meal():
    if g.user is None:
        return redirect(url_for('signin'))
    if request.method == "POST":
        name = g.user['username']# get the username provided in the sign up page
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
        # Display the user's first name on the client side
        first_name = g.user["first_name"]
        return render_template("meal.html", meal=meal, groceries=groceries, first_name=first_name)

    elif request.method == "GET":
        try:
            name = g.user['username']# get the username provided in the sign up page
            grocery = name + '1'
            groceries = get_meal_from_db(grocery)
            meal = get_meal_from_db(name)
            return render_template("meal.html", meal=meal, groceries=groceries)
        
        except sqlite3.OperationalError:
                return render_template('input.html')

#this provides a table for the grocery list
@app.route('/grocery')
def grocery():
    name = g.user['username']# get the username provided in the sign up page
    grocery = name + '1'
    groceries = get_meal_from_db(grocery)
    data = []
    for row in groceries:
        data.append({'Date': row[0], 'Item': row[1]})
    return jsonify(data)


############# THE STRESS MANAGEMENT RESOURSE #########################

class StressManagementResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    def __init__(self, title, decsription):
        self.title = title
        self.description = decsription
    
    def __repr__(self):
        return f"StressManagementResource(id={self.id}, title='{self.title}')"
    
# API endpoint to get all stress management resources
@app.route('/resources', methods=['GET'])
def get_stress_management_resources():
    resources = StressManagementResource.query.all()
    output = []
    for resource in resources:
        resource_data = {
            'id': resource.id,
            'title': resource.title,
            'description': resource.description
        }
        output.append(resource_data)
    return jsonify({'resources': output})

@app.route('/resources/<int:id>')
def get_stress_management_resource(id):
    resource = StressManagementResource.query.get(id)
    if resource is None:
        return 404
    return jsonify({'resource': resource})

#API endpoint to create a new stress management resouce
@app.route('/resources', methods=['POST'])
def create_stress_management_resources():
    data = request.get_json()
    new_resource = StressManagementResource(title=data['title'], description=data['description'])
    db.session.add(new_resource)
    db.session.commit()
    # return jsonify({'message': 'Resource created successfully'})
    return 201, {'resource': new_resource}


@app.route('/resources/<int:id>', methods=['PUT'])
def update_stress_management_resource(id):
    data = request.get_json()
    resource = StressManagementResource.query.get(id)
    if resource is None:
        return 404
    resource.title = data['title']
    resource.description = data['description']
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

#################### STRESS MANAGEMENT RESOURCE END ###########################

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

        # Hash password
        password_hash = hash_password(password)

        # Insert user into database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (email, first_name, last_name, username, gender, university_name, password_hash) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (email, first_name, last_name, username, gender, university_name, password_hash))
        conn.commit()
        conn.close()

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
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT id, password_hash FROM users WHERE email = ?", (email,))
        row = c.fetchone()

        if row is None:
            # User not found
            error = 'Invalid email or password'
            return render_template('signin.html', error=error)

        # Check password
        password_hash = row[1]
        if check_password(password, password_hash):
            # Password is correct, store user ID in session
            session['user_id'] = row[0]
            return redirect('/home')
        else:
            # Password is incorrect
            error = 'Invalid email or password'
            return render_template('signin.html', error=error)

    # Render sign-in page
    return render_template('signin.html')


@app.route('/signout')
def signout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('signin'))

@app.route('/home')
def home():
    return render_template('home.html', user=g.user)


@app.route('/api')
def api():
    url = "https://workoutdb1.p.rapidapi.com/user/update"

    payload = {
        "lastName": "DOE",
        "firstName": "JOHN"
    }
    headers = {
        "content-type": "application/json",
        "id-token": "{{idToken}}",
        "X-RapidAPI-Key": "040d644d14mshd1a90104a210a66p1edfabjsnc25e68304e4b",
        "X-RapidAPI-Host": "workoutdb1.p.rapidapi.com"
    }

    response = requests.patch(url, json=payload, headers=headers)

    a = (response.json())
    return render_template('api.html', a=a)

if __name__ == '__main__':
    app.run(debug=True)
