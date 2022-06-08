from flask import Flask, render_template, request, jsonify,redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__) 

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
