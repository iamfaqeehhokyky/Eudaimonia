from flask import Flask, render_template, request, g, redirect, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)
app.secret_key='your'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)


@app.route('/')
def index():
    return 'Welcome to EUDAIMONIA web app. Let\'s get to building'













import sqlite3

DATABASE_FILE = 'database.db'

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

# @app.before_request
# def before_request():
#     g.user = None
#     if 'user_id' in session:
#         # Retrieve user from the database using session['user_id']
#         # and store it in g.user
#         g.user = get_user_from_database(session['user_id'])

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
        db_execute("INSERT INTO %s SELECT * FROM %s" % (new_table_name, table_name))

        print("Successfully replicated %s as %s" % (table_name, new_table_name))
    except sqlite3.Error as e:
        if str(e).startswith('table %s already exists' % new_table_name):
            print('Table %s already exists. Please choose a different name.' % new_table_name)
        else:
            print('Error replicating table:', e)

# Example usage: replicate_table('original_table_name', 'new_table_name')
def get_meal_from_db(table_name):
    query = "SELECT * FROM {}".format(table_name)
    results = db_query(query)
    if results:
        return results
    else:
        return None



@app.route('/input')
def input():
    return render_template ('input.html')

@app.route('/meal', methods=("GET", "POST"))
def meal():
        if request.method == "POST":    
            name=request.form['name']
            session['name'] = name
            Vegetarian=request.form['Vegetarian']
            # Allergies=request.form['Allergies']
            height=float(request.form['height'])
            weight=float(request.form['weight'])
            meal=request.form['meal']

            m = height*height
            kg= weight
            bmi = kg/m

            if bmi <= 18.5:        

                if Vegetarian == 'Yes':
                    if meal == 'two':
                        replicate_table('Vegetarian_UW2', name)
                    elif meal == 'three':
                        replicate_table('Vegetarian_UW3', name)
                elif Vegetarian == 'N0':
                    if meal == 'two':
                        replicate_table('Under_weight2', name)
                    elif meal == 'three':
                        replicate_table('Under_weight3', name)
                meal = get_meal_from_db(name)
                return render_template("meal.html", meal=meal)


            elif bmi > 18.5:
                if Vegetarian == 'Yes':
                    if meal == 'two':
                        replicate_table('Vegetarian_NW2', name)
                    elif meal == 'three':
                        replicate_table('Vegetarian_NW3', name)
                elif Vegetarian == 'N0':
                    if meal == 'two':
                        replicate_table('Normal_weight2', name)
                    elif meal == 'three':
                        replicate_table('Normal_weight3', name)
                meal = get_meal_from_db(name)
                return render_template("meal.html", meal=meal)
                
            elif bmi > 26.0:
                if Vegetarian == 'Yes':
                    if meal == 'two':
                        replicate_table('Vegetarian_OW2', name)
                    elif meal == 'three':
                        replicate_table('Vegetarian_OW3', name)
                elif Vegetarian == 'N0':
                    if meal == 'two':
                        replicate_table('Over_weight2', name)
                    elif meal == 'three':
                        replicate_table('Over_weight3', name)
                meal = get_meal_from_db(name)
                return render_template("meal.html", meal=meal)
        elif request.method == "GET":
            name = session.get('name')
            print(name)
            meal = get_meal_from_db(name)
            return render_template("meal.html", meal=meal)


if __name__ == '__main__':
    app.run(debug=True)
