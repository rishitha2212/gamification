from flask import Flask, redirect, url_for, render_template, request, jsonify
import json
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(user='root', password='', host='localhost',database='gamification')
sql_select_Query = "select * from new_data where amount > 10000"
cursor = connection.cursor(buffered=True, dictionary=True)
cursor.execute(sql_select_Query)

records = cursor.fetchall()

for row in records:
    print(row)
