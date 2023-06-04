from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
#from registration import regisration_user_in_Database()
def regisration_user_in_Database(userid,name,second_name,birthday,login,email,password):
    path = '/Users/ilafedoseev/projects/TestDavidSait/TestSait_DataBase.db'
    with sqlite3.connect(path) as connection:
        cur = connection.cursor()

        cur.execute(f"""CREATE TABLE IF NOT EXISTS users(
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        second_name VARCHAR(255),
        birthday Date,
        login VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password TEXT);
        """)

        sql = f"""INSERT INTO users(name, second_name, birthday, login, email, password) 
            VALUES('{name}', '{second_name}', '{birthday}', '{login}', '{email}', '{password}');"""
        print(sql)
        cur.execute(sql)
        connection.commit()
        #all = cur.fetchall()

        #cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
        #    VALUES('00001', 'Alex', 'Smith', 'man');""")

def next_(id):
    path = r'/home/nubuk/Programming/Testsait/TestSait_DataBase.db'
    with sqlite3.connect(path) as connection:
        cur = connection.cursor()

        cur.execute("""SELECT MAX(userid) FROM users;""")
        object_with_max_userid = cur.fetchall()
        print(object_with_max_userid)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/succes_registration')
def succes_registration():
    return render_template('succes_registration.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration_sait():
    if request.method == 'GET':
        return render_template('registration.html')
    name = request.form['name']
    second_name = request.form['second_name']
    birthday = request.form['birthday']
    login = request.form['login']
    email = request.form['email']
    password = request.form['password']
    regisration_user_in_Database(0, name, second_name, birthday, login, email, password)
    #return render_template('succes_registration.html')
    return redirect('/succes_registration')

app.run()

#path = r'/home/nubuk/Programming/Testsait/TestSait_DataBase.db'
#with sqlite3.connect(path) as connection:
#    cur = connection.cursor()
#    cur.execute(f"""SELECT MAX(userid) FROM users;""")
#    print(cur.fetchall())
