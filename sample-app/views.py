from flask import Flask, jsonify, render_template
from dbconnect import *
import os
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_database')
def Create_Database():
 mydb = Get_Connect_To_Mysql()
 try :
    cursor = mydb.cursor()
    result = cursor.execute("DROP DATABASE IF EXISTS inventory")
    result = cursor.execute("CREATE DATABASE inventory")
    response = {'status': True, 'message': "Created Successfully"}
    return jsonify(response)
 except Exception as e:
    response = {'status': False, 'message': str(e)}
    return jsonify(response)

@app.route('/create_a_table')
def create_a_table():
    mydb = Get_Connect_To_DatabaseMysql('inventory')
    try:
        cursor = mydb.cursor()
        cursor.execute("DROP TABLE IF EXISTS students")  # changed to match later usage
        cursor.execute("CREATE TABLE students (name VARCHAR(255), description VARCHAR(255))")
        cursor.close()
        response = {'status': True, 'message': "Table created successfully"}
    except Exception as e:
        response = {'status': False, 'error': str(e)}
    return jsonify(response)

@app.route('/insert_get_table_record')
def insert_get_table_record():
    mydb = Get_Connect_To_DatabaseMysql('inventory')
    try:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO students (name, description) VALUES ('Hanzlla', 'DevOps Engineer');")
        mydb.commit()
        cursor.execute("SELECT * FROM students")
        myresult = cursor.fetchall()
        cursor.close()
        response = {'status': True, 'data': myresult, 'message': "Fetched Successfully"}
    except Exception as e:
        response = {'status': False, 'message': str(e)}
    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)