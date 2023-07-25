from json import load
import re
from flask import Flask, request, render_template, redirect, url_for, json
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS, cross_origin
import time

def login_db():
    
    # 連接 MySQL/MariaDB 資料庫
    connection = mysql.connector.connect(
    host='192.168.56.2',          # 主機名稱
    database='myDB', # 資料庫名稱
    user='userDB',        # 帳號
    password='password')  # 密碼
    
    if connection.is_connected():

        # 顯示資料庫版本
        db_Info = connection.get_server_info()
        print("資料庫版本：", db_Info)

        # 顯示目前使用的資料庫
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("目前使用的資料庫：", record)
    
    return connection

    
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def submit():
    name = ''
    if request.method == 'POST':
        
        if request.json['mode'] == 'insert':
            print('insert!!!!!!!!!!!!!!!!!!!')
            name = request.json['name']
            score = request.json['score']
            print("post : => ", name, "  ", score)

            
            DB = login_db()
            mycursor = DB.cursor()
            
            mycursor.execute("SELECT Name FROM ScoreBoard ORDER BY Score DESC;")
            results = mycursor.fetchall()
            
            for result in results:
                if name == result[0]:
                    print("Modify!!!!!!!!!!!!!!!!!!")
                    sql = f"UPDATE ScoreBoard SET Score={score} WHERE Name='{name}';"
                    mycursor.execute(sql)
                    DB.commit()
                    mycursor.close()
                    DB.close()
                    return app.response_class(response=json.dumps({'status': 0}), status=200, mimetype='application/json')

            if name != '':
                sql = "INSERT INTO ScoreBoard (Name, Score) VALUES (%s, %s);"
                val = (name, score)
                mycursor.execute(sql, val)
                DB.commit()
                mycursor.close()
                DB.close()

                return app.response_class(response=json.dumps({'status': 0}), status=200, mimetype='application/json')
            else:
                return app.response_class(response=json.dumps({'status': 1, 'msg': 'Please input user name!'}), status=400, mimetype='application/json')
        elif request.json['mode'] == 'clear':
            
            DB = login_db()
            mycursor = DB.cursor()
            sql = "DELETE FROM ScoreBoard"
            mycursor.execute(sql)
            DB.commit()
            mycursor.close()
            DB.close()
            return app.response_class(response=json.dumps({'status': 0}), status=200, mimetype='application/json')
    else:
        
        DB = login_db()
        mycursor = DB.cursor()
        time.sleep(0.5)
        mycursor.execute("SELECT Name, Score FROM ScoreBoard ORDER BY Score DESC;")
        result = mycursor.fetchall()

        mycursor.close()
        DB.close()
        return app.response_class(response=json.dumps({'status': 0, 'data': result}), status=200, mimetype='application/json')


@app.route('/success/<action>/<name>')
@cross_origin()
def success(name, action):
    return '{} : Welcome {} ~ !!!'.format(action, name)

if __name__ == '__main__':
    app.run()
