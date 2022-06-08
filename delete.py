from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__) 

@app.route('/delete', methods=['GET'])  # This will be called from UI
def example(): 
    conn = mysql.connector.connect(user='root', password='', host='localhost',database='gamification') 
    cursor = conn.cursor() 
    cursor.execute("delete * from challenges") 
    data = cursor.fetchall() #data from database 
    return render_template("table.html", value=data) 

if __name__ == '__main__':
    app.run(debug=True)
