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

@app.route('/input')
def input():
    return render_template ('input.html')

@app.route('/meal', methods=("GET", "POST"))
def meal():
    if request.method == "GET":    
        return render_template ('menu.html')
    
    elif request.method == "POST":
        name=request.form['name']
        Vegetarian=request.form['Vegetarian']
        Allergies=request.form['Allergies']
        height=float(request.form['height'])
        weight=float(request.form['weight'])
        meal=request.form['meal']

        m = height*height
        kg= weight
        bmi = kg/m

        if bmi <= 18.5:        

            if Vegetarian == 'Yes':
                if meal == 'two':
                    pass
                elif meal == 'three':
                    pass
            elif Vegetarian == 'N0':
                pass

        elif bmi > 18.5:
            if Vegetarian == 'Yes':
                if meal == 'two':
                    pass
                elif meal == 'three':
                    pass
            elif Vegetarian == 'N0':
                pass

        elif bmi > 18.5:
            if Vegetarian == 'Yes':
                if meal == 'two':
                    pass
                elif meal == 'three':
                    pass
            elif Vegetarian == 'N0':
                pass
            
        elif bmi > 26.0:
            if Vegetarian == 'Yes':
                if meal == 'two':
                    pass
                elif meal == 'three':
                    pass
            elif Vegetarian == 'N0':
                pass


if __name__ == '__main__':
    app.run(debug=True)
