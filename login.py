from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error
import hashlib

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('login.html')

# http://localhost:5000/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'user_id' in request.form and 'password' in request.form:
        # Create variables for easy access
        user_id = request.form['user_id']
        password = request.form['password']
        # Check if account exists using MySQL
        connection = mysql.connector.connect(user='root', password='', host='localhost',database='gamification')
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        cursor1.execute("SELECT admin_id,password FROM admin_table WHERE admin_id = %s AND password = %s", (user_id, password,))
        account = cursor1.fetchall()
        cursor2.execute("SELECT seller_id,password FROM seller_table WHERE seller_id = %s AND password = %s", (user_id, password,))
        account2 = cursor2.fetchall()
        connection.commit()
        # If account exists in accounts table in out database
        if account:
            return render_template('admin.html')
        elif account2:
            return "Seller logged in successfully!"
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
