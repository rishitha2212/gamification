from flask import Flask, redirect, url_for, render_template, request, jsonify
import json
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)

@app.route('/')
def home():
    try:

        connection = mysql.connector.connect(user='root', password='', host='localhost',
                                                 database='gamification')
        sql_select_Query = "SELECT @n := @n + 1 n,seller_id,amount FROM new_data,(SELECT @n := 0) m ORDER BY amount DESC LIMIT 5"

        cursor = connection.cursor()
        cursor.execute(sql_select_Query)

        records = cursor.fetchall()

        return render_template('form.html',value=records)
    except Error as e:
        return "Error while connecting to MySQL"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)