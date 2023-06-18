from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
from registration import regisration_user_in_Database


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/succes_registration')
def succes_registration():
    return render_template('succes_registration.html')


@app.route('/users/<id>')
def profile(id):
    path = '../TestSait_DataBase.db'
    with sqlite3.connect(path) as connection:
        cur = connection.cursor()

        cur.execute(f"""SELECT * FROM users WHERE userid = {id}""")
        information = cur.fetchone()
        name = information[1]
        surname = information[2]
        birthday = information[3]
        login = information[4]
        email = information[5]
        password = information[6]
        return render_template('profile.html', 
                               name=name,
                                surname=surname,
                                  birthday=birthday,
                                    login=login,
                                      email=email,
                                        password=password,)






@app.route('/registration', methods=['GET', 'POST'])
def registration_sait():
    if request.method == 'GET':
        return render_template('registration.html')
    if request.method == 'POST':
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
