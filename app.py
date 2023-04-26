from flask import Flask, render_template, request, g, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


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
    conn.close()
    return True

conn = sqlite3.connect('database.db')

def replicate_table(table_name, new_table_name):
    c = conn.cursor()

    # Retrieve column names and types for the original table
    c.execute("PRAGMA table_info(%s)" % table_name)
    column_data = c.fetchall()

    # Construct a new CREATE TABLE query with the same columns and types
    create_query = "CREATE TABLE %s (" % new_table_name
    for column in column_data:
        column_name = column[1]
        column_type = column[2]
        create_query += "%s %s, " % (column_name, column_type)
    create_query = create_query[:-2] + ")"

    # Execute the CREATE TABLE query for the new table
    c.execute(create_query)

    # Insert the data from the original table into the new table
    c.execute("INSERT INTO %s SELECT * FROM %s" % (new_table_name, table_name))

    conn.commit()
    print("Successfully replicated %s as %s" % (table_name, new_table_name))

# Example usage: replicate_table('original_table_name', 'new_table_name')
def get_meal_from_db(name):
    results = db_query("SELECT * FROM name = :name", {"name": name})
    if results:
        return results[0]
    else:
        return None

@app.route('/input')
def input():
    return render_template ('input.html')

@app.route('/meal', methods=("GET", "POST"))
def meal():
    
        name=request.form['name']
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


if __name__ == '__main__':
    app.run(debug=True)
