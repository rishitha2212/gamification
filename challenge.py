from flask import Flask, render_template, request, jsonify, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

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

@app.route('/challenge', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('admin.html')

@app.route('/challengepage')
def challenge_page():
    return render_template('challenge.html')

@app.route('/insert', methods=['POST'])  # This will be called from UI
def math_operation():

    if (request.method=='POST'):
        challenge=str(request.form['challenge'])
        start_date = str(request.form['start_date'])
        expiry_date = str(request.form['expiry_date'])
        target = str(request.form['target'])
        reward = str(request.form['reward'])
        connection = mysql.connector.connect(user='root', password='', host='localhost',database='gamification')
        cursor = connection.cursor()
        cursor.execute("insert into challenges (challenge,start_date,expiry_date,target,reward) values (%s,%s,%s,%s,%s)",(challenge,start_date,expiry_date,target,reward))
        connection.commit()
        return "registered"

@app.route('/table', methods=['GET'])  # This will be called from UI
def example(): 
    conn = mysql.connector.connect(user='root', password='', host='localhost',database='gamification') 
    cursor = conn.cursor() 
    cursor.execute("select * from challenges") 
    data = cursor.fetchall() #data from database 
    return render_template("table.html", value=data) 

@app.route('/delete/<int:score>', methods=['GET'])  # This will be called from UI
def delete(score): 
    conn = mysql.connector.connect(user='root', password='', host='localhost',database='gamification') 
    cursor1 = conn.cursor() 
    print(score)
    cursor1.execute(f"delete from challenges where id = {score}") 
    data1 = cursor1.fetchall() #data from database 
    conn.commit()
    return redirect('/table') 

@app.route('/updatec')  # This will be called from UI
def update():
    return render_template('update.html')

@app.route('/update',methods=['POST'])
def change():
    id1=int(request.form['id1'])
    challenge=str(request.form['challenge'])
    start_date = str(request.form['start_date'])
    expiry_date = str(request.form['expiry_date'])
    target = str(request.form['target'])
    reward = str(request.form['reward'])
    connection = mysql.connector.connect(user='root', password='', host='localhost',database='gamification')
    cursor = connection.cursor()
    cursor.execute(f"update challenges set challenge='%s',start_date='%s', expiry_date='%s', target='%s', reward='%s' where id ={id1}"% (challenge,start_date,expiry_date,target,reward))
    connection.commit()
    return redirect('/table')

if __name__ == '__main__':
    app.run(debug=True)
