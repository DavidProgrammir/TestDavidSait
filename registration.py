from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
def regisration_user_in_Database(userid,name,second_name,birthday,login,email,password):
    path = '../TestSait_DataBase.db'
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