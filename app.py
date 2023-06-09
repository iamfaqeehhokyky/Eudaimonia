from flask import Flask, render_template, request, g, session, jsonify, url_for, redirect, flash, send_from_directory
import sqlite3, requests, hashlib, os, warnings, requests, datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(16)

# i kept on getting a warning about flask future upadate so i
# Ignored the FSADeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        university_name = request.form['university_name']
        faculty_name = request.form['faculty_name']
        department_name = request.form['department_name']
        subject = request.form['subject']
        message = request.form['message']

        try:
            # Insert user into database
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("INSERT INTO contact_us (first_name, last_name, email, university_name, faculty_name, department_name, subject, message) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                      (first_name, last_name, email, university_name, faculty_name, department_name, subject, message))
            conn.commit()
            conn.close()
            flash('Form submitted successfully!', 'success')
            # return redirect('/')
        except:
            flash(
                'An error occurred while submitting the form. Please try again later.', 'error')

    # Render home page
    return render_template('index.html')

# Route to the blog page


@app.route('/blog')
def blog():
    return render_template('blog.html')

# Route to the home blog page


@app.route('/homeblog')
def homeblog():
    return render_template('homeblog.html')


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


@app.route('/first_input')
def first_input():
    if g.user is not None:
        first_name = g.user["first_name"]
        return render_template('allergies.html', first_name=first_name)
    return redirect(url_for('signin'))


@app.route('/input')
def input():
    if g.user is not None:
        first_name = g.user["first_name"]
        return render_template('input.html', first_name=first_name)
    return redirect(url_for('signin'))

# This process the first submitted form for allegies


@app.route('/allergies', methods=["GET", "POST"])
def allergies():
    if g.user is None:
        return redirect(url_for('signin'))
    first_name = g.user["first_name"]

    if request.method == "POST":
        # get the information provided in the sign up page
        allergies = request.form['Allergies']
        session['allergies'] = allergies
        if allergies == 'Yes':
            return render_template('input.html', first_name=first_name)
        if allergies == 'No':
            return render_template('input.html', first_name=first_name)

# implementation for replacing whaet in the meals


def wheat(meal):
    substituted_meal = []
    name = g.user['username']
    query = "SELECT Date, BreakFast, Lunch, Dinner FROM {} WHERE BreakFast LIKE %s OR Lunch LIKE %s OR Dinner LIKE %s.".format(
        name)
    args = ('%wheat%', '%wheat%', '%wheat%')
    meals_with_wheat = db_query(query, args)

    # Substitute wheat meals with suitable alternatives
    for row in meals_with_wheat:
        date = row[0]
        breakfast = row[1]
        lunch = row[2]
        dinner = row[3]

        # Perform substitution logic, replace wheat meals with suitable alternatives
        substituted_breakfast = breakfast.replace('wheat', 'Garri')
        substituted_lunch = lunch.replace('wheat', 'Garri')
        substituted_dinner = dinner.replace('wheat', 'Garri')

        # Update the substituted meals in the substituted meal plan
        substituted_meal.append({
            'Date': date,
            'BreakFast': substituted_breakfast,
            'Lunch': substituted_lunch,
            'Dinner': substituted_dinner
        })

    return substituted_meal

# implementation for replacing oat in the meals


def oat(meal):
    substituted_meal = []
    name = g.user['username']
    query = "SELECT Date, BreakFast, Lunch, Dinner FROM {} WHERE BreakFast LIKE %s OR Lunch LIKE %s OR Dinner LIKE %s.".format(
        name)
    args = ('%Oatmeal%', '%Oatmeal%', '%Oatmeal%')
    meals_with_wheat = db_query(query, args)

    # Substitute wheat meals with suitable alternatives
    for row in meals_with_wheat:
        date = row[0]
        breakfast = row[1]
        lunch = row[2]
        dinner = row[3]

        # Perform substitution logic, replace wheat meals with suitable alternatives
        substituted_breakfast = breakfast.replace('Oatmeal', 'drink')
        substituted_lunch = lunch.replace('Oatmeal', 'drink')
        substituted_dinner = dinner.replace('Oatmeal', 'drink')

        # Update the substituted meals in the substituted meal plan
        substituted_meal.append({
            'Date': date,
            'BreakFast': substituted_breakfast,
            'Lunch': substituted_lunch,
            'Dinner': substituted_dinner
        })

    return substituted_meal

# implementation for replacing egg in the meals


def egg(meal):
    substituted_meal = []
    name = g.user['username']
    query = "SELECT Date, BreakFast, Lunch, Dinner FROM {} WHERE BreakFast LIKE %s OR Lunch LIKE %s OR Dinner LIKE %s.".format(
        name)
    args = ('%egg%', '%egg%', '%Oatmeal%')
    meals_with_wheat = db_query(query, args)

    # Substitute wheat meals with suitable alternatives
    for row in meals_with_wheat:
        date = row[0]
        breakfast = row[1]
        lunch = row[2]
        dinner = row[3]

        # Perform substitution logic, replace wheat meals with suitable alternatives
        substituted_breakfast = breakfast.replace('egg', 'meat stew')
        substituted_lunch = lunch.replace('egg', 'meat stew')
        substituted_dinner = dinner.replace('egg', 'meat stew')

        # Update the substituted meals in the substituted meal plan
        substituted_meal.append({
            'Date': date,
            'BreakFast': substituted_breakfast,
            'Lunch': substituted_lunch,
            'Dinner': substituted_dinner
        })

    return substituted_meal

# implementation for replacing oil in the meals


def oil(meal):
    substituted_meal = []
    name = g.user['username']
    query = "SELECT Date, BreakFast, Lunch, Dinner FROM {} WHERE BreakFast LIKE %s OR Lunch LIKE %s OR Dinner LIKE %s.".format(
        name)
    args = ('%groundnut oil%', '%groundnut oil%', '%groundnut oil%')
    meals_with_wheat = db_query(query, args)

    # Substitute wheat meals with suitable alternatives
    for row in meals_with_wheat:
        date = row[0]
        breakfast = row[1]
        lunch = row[2]
        dinner = row[3]

        # Perform substitution logic, replace wheat meals with suitable alternatives
        substituted_breakfast = breakfast.replace('groundnut oil', 'vegetable')
        substituted_lunch = lunch.replace('groundnut oil', 'vegetable')
        substituted_dinner = dinner.replace('groundnut oil', 'vegetable')

        # Update the substituted meals in the substituted meal plan
        substituted_meal.append({
            'Date': date,
            'BreakFast': substituted_breakfast,
            'Lunch': substituted_lunch,
            'Dinner': substituted_dinner
        })

    return substituted_meal

# this performs the replacing of the food items, based on the allegies chosen


def allergy_meals(meal, allergies):
    if 'Wheat' in allergies:
        allergy = wheat(meal)
        return allergy

    if 'Oil' in allergies:
        allergy = oil(meal)
        return allergy

    if 'Oat' in allergies:
        allergy = oat(meal)
        return allergy

    if 'Egg' in allergies:
        allergy = egg(meal)
        return allergy


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
        allergies = session.get('allergies')
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

        # This changes the selected food a user have allergies for
        if allergies == 'Yes':
            meal = allergy_meals(meal, allergies)
            meal_data = get_meal_from_db(name)
            meal = list(meal_data)

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
            return render_template('allergies.html')

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


class StressManagementResource:
    def __init__(self, title, description, link):
        self.id = None
        self.title = title
        self.description = description
        self.link = link

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
    query = "SELECT * FROM stress_management_resources"
    rows = db_query(query, ())
    resources = []
    for row in rows:
        resource = StressManagementResource(
            title=row[1],
            description=row[2],
            link=row[3]
        )
        resource.id = row[0]
        resources.append(resource.to_dict())
    return jsonify({'resources': resources})

@app.route('/resources/<int:id>')
def get_stress_management_resource(id):
    query = "SELECT * FROM stress_management_resources WHERE id = ?"
    args = (id,)
    row = db_query(query, args)
    if row is None:
        return jsonify({'message': 'Resource not found'}), 404
    resource = StressManagementResource(
        title=row[1],
        description=row[2],
        link=row[3]
    )
    resource.id = row[0]
    return jsonify({'resource': resource.to_dict()})

# API endpoint to create a new stress management resouce
@app.route('/resources', methods=['POST'])
def create_stress_management_resources():
    data = request.get_json()
    resource = StressManagementResource(
        title=data['title'],
        description=data['description'],
        link=data['link']
    )
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO stress_management_resources (title, description, link) VALUES (?, ?, ?)',
              (resource.title, resource.description, resource.link))
    conn.commit()
    resource.id = c.lastrowid
    conn.close()
    return jsonify({'resource': resource.to_dict()}), 201

@app.route('/resources/<int:id>', methods=['PUT'])
def update_stress_management_resource(id):
    data = request.get_json()
    resource = StressManagementResource(
        title=data['title'],
        description=data['description'],
        link=data['link']
    )
    resource.id = id
    query = "UPDATE stress_management_resources SET title = ?, description = ?, link = ? WHERE id = ?"
    args = (resource.title, resource.description, resource.link, resource.id)
    db_connection = get_db()
    cur = db_connection.cursor()
    cur.execute(query, args)
    db_connection.commit()
    return jsonify({'resource': resource.to_dict()})

@app.route('/resources/<int:id>', methods=['DELETE'])
def delete_stress_management_resource(id):
    query = "DELETE FROM stress_management_resources WHERE id = ?"
    args = (id,)
    db_connection = get_db()
    cur = db_connection.cursor()
    cur.execute(query, args)
    db_connection.commit()
    return '', 204

@app.route('/api', methods=['GET', 'POST'])
def api():
    if g.user is None:
        return redirect(url_for('signin'))
    return render_template('api.html')

############################# STRESS MANAGEMENT RESOUCE END ##########################


def check_user_exists(email, username):
    # Check if user with the given email exists
    query = "SELECT * FROM users WHERE email = ?"
    args = (email,)
    user_email = db_query(query, args)

    # Check if user with the given username exists
    query1 = "SELECT * FROM users WHERE username = ?"
    args1 = (username,)
    user_username = db_query(query1, args1)

    if user_email or user_username:
        return True
    else:
        return False


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

        # Check if user already exists
        user_exists = check_user_exists(email, username)
        if user_exists:
            error_message = 'User with the same email or username already exists.'
            return render_template('signup.html', error=error_message)

        # Hash password
        password_hash = hash_password(password)

        # Insert user into database
        query = "INSERT INTO users (email, first_name, last_name, username, gender, university_name, password_hash) VALUES (?, ?, ?, ?, ?, ?, ?)"
        args = (email, first_name, last_name, username,
                gender, university_name, password_hash)

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
            # Access the first row's first element
            session['user_id'] = row[0][0]
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


@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/hometeam')
def hometeam():
    return render_template('hometeam.html')

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
    date = datetime.datetime.now()
    timestamp = date.strftime('%Y-%m-%d %H:%M')

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

# this creates the goal


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

# This gets the milestone from the db, so it can be accesed with goal using foreign keys


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

# Dashboard route


@app.route('/dashboard')
def dashboard():
    if g.user is None:
        return redirect(url_for('signin'))
    visited = "You visited the  dashboard"
    user_id = session['user_id']
    record_usage_history(user_id, visited)
    return render_template('dashboard.html')

# profile route


@app.route('/profile')
def profile():
    if g.user is None:
        return redirect(url_for('signin'))
    
    name = g.user['username']


    visited = "You checked your profile"
    user_id = session['user_id']
    record_usage_history(user_id, visited)
    user = get_user(user_id)
    query = "SELECT profile_image FROM users WHERE username = ?"
    args = (name,)
    image_row = db_query(query, args)[0]
    image = dict(image_row)

    session['image'] = image

    return render_template('profile.html', user=user, image=session['image'])


IMAGE = os.path.join(app.root_path, 'static', 'assets/img')

@app.route('/profile_update', methods=['GET', 'POST'])
def profile_update():
    if g.user is None:
        return redirect(url_for('signin'))
    
    name = g.user['username']
    user_id = session['user_id']
    user = get_user(user_id)
    if user is None:
        return redirect(url_for('signin'))

    visited = "You updated your profile"
    record_usage_history(user_id, visited)

    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        university_name = request.form.get('university_name')
        profile_image = request.files.get('profile_image')

        if profile_image:
            # Save the uploaded profile image
            filename = secure_filename(profile_image.filename)
            profile_image.save(os.path.join(IMAGE, filename))
            user['profile_image'] = filename

            # Update user profile with image data
            query = "UPDATE users SET first_name = ?, last_name = ?, username = ?, email = ?, university_name = ?, profile_image = ? WHERE id = ?"
            args = (first_name, last_name, username, email, university_name, user['profile_image'], user_id)
            db_connection = get_db()
            cur = db_connection.cursor()
            cur.execute(query, args)
            db_connection.commit()

        user = get_user(user_id)
        
        # Retrieve the image data and store it in session['image']
        query = "SELECT profile_image FROM users WHERE username = ?"
        args = (name,)
        image_row = db_query(query, args)[0]
        session['image'] = dict(image_row)

        return redirect('/profile')
    
    # Retrieve the image data and store it in session['image']
    query = "SELECT profile_image FROM users WHERE username = ?"
    args = (name,)
    image_row = db_query(query, args)[0]
    session['image'] = dict(image_row)

    return render_template('profile.html', user=user, image=session['image'])



# community route
@app.route('/community', methods=['GET', 'POST'])
def group_chat():
    if g.user is None:
        return redirect(url_for('signin'))

    user_id = session['user_id']
    user = get_user(user_id)
    if user is None:
        return redirect(url_for('signin'))

    visited = "You visited the community group chat"
    record_usage_history(user_id, visited)

    if request.method == 'POST':
        message = request.form['message']

        name = g.user['username']
        date = datetime.datetime.now()
        timestamp = date.strftime('%H:%M')

        query = "INSERT INTO community_chat (username, content, timestamp) VALUES (?, ?, ?)"
        args = (name, message, timestamp)
        db_connection = get_db()
        cur = db_connection.cursor()
        cur.execute(query, args)
        db_connection.commit()

    query = "SELECT * FROM community_chat"
    messages = db_query(query, ())

    return render_template('community.html', messages=messages)


@app.route('/news')
def news():
    if g.user is None:
        return redirect(url_for('signin'))
    
    # this makes an API request to retrieve news articles related to mental health
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'mental health',
        'apiKey': 'ea769aa48ea34019afac1ed0dc22f7b3'
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = data['articles']

    return render_template('news.html', articles=articles)

youtube_api_key = os.environ.get('YOUTUBE_API_KEY')
@app.route('/stress')
def video_list():
    if g.user is None:
        return redirect(url_for('signin'))

    visited = "used the relaxation page"
    user_id = session['user_id']
    record_usage_history(user_id, visited)

    med_files = ['Lm4-VgILXJ0', 'wzznoOyQs68', 'rIsW6jlRngk', 'YbF-GvP4rxY', 'EbVRkWxpUHg',
                 'yeaHIYIdaLE', 'FFeSZr6Shzg', 'muhppUlYRXE', '2rSd5clsbyE', 'LumA2LorU7M', '6zsvGtNjhX8']
    pers_files = ['xLd6PBx6xUI', 'vTUmLL8f_74', 'a8tQOuGPO3I', 'w6qSTR1p0IY', 'NqbSnkG8PyA']
    relax_files = ['FXcfQ0atNK4', 'BF06BBqpDas', '160DBDwZlH0', 'CEtmDvGLZWc',
                   'aMuHqQAwx_s', 'HHiRQ3CQCRA', 'a4VDQTaVhAM', 'mqa9pn7GsN4', 'ucmTkcS2XyA', 'oDEkTz9wLRI']
    return render_template('mental.html', meditations=med_files, personalize=pers_files, relax=relax_files, api_key=youtube_api_key)


@app.route('/videos/<path:filename>')
def serve_video(filename):
    video_directory = os.path.join(app.root_path, 'static', 'video')
    cache_timeout = 3600

    return send_from_directory(video_directory, filename, cache_timeout=cache_timeout)

   

youtube_api_key = os.environ.get('YOUTUBE_API_KEY')

@app.route('/stres')
def stres():
    med_files = ['Lm4-VgILXJ0', 'wzznoOyQs68', 'rIsW6jlRngk', 'YbF-GvP4rxY', 'EbVRkWxpUHg',
                 'yeaHIYIdaLE', 'FFeSZr6Shzg', 'muhppUlYRXE', '2rSd5clsbyE', 'LumA2LorU7M', '6zsvGtNjhX8']
    pers_files = ['xLd6PBx6xUI', 'vTUmLL8f_74', 'a8tQOuGPO3I', 'w6qSTR1p0IY', 'NqbSnkG8PyA']
    relax_files = ['FXcfQ0atNK4', 'BF06BBqpDas', '160DBDwZlH0', 'CEtmDvGLZWc',
                   'aMuHqQAwx_s', 'HHiRQ3CQCRA', 'a4VDQTaVhAM', 'mqa9pn7GsN4', 'ucmTkcS2XyA', 'oDEkTz9wLRI']
    return render_template('ment.html', meditations=med_files, personalize=pers_files, relax=relax_files, api_key=youtube_api_key)


if __name__ == '__main__':
    app.run(debug=True)
