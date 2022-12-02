import sqlite3 as sql
import config
from aiogram.utils.markdown import hlink
from datetime import datetime, time
from time import gmtime, strftime
import shutil
import random
import pandas as pd
count = 0
queue = []
def user(id):
    con = sql.connect("users.db")
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, login TEXT, Nick TEXT,stat INT, message TEXT)")
        x = []
        for i in range(11):
            x.append(i)
        if '@' not in str(id):
            info = cur.execute(f"SELECT * FROM users WHERE id=('{id}')")
        elif id[0] not in x:
            info = cur.execute(f"SELECT * FROM users WHERE Nick=('{id}')")
        else:
            info = cur.execute(f"SELECT * FROM users WHERE login=('{id[1:]}')")
        return info.fetchone()
    con.commit()
    cur.close()

#####################################################

def safemessage(id, Q1):
    con = sql.connect("users.db")
    info1= user(id)
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, login TEXT, Nick TEXT,stat INT, message TEXT)")
        cur.execute(f'UPDATE users SET message="{Q1}" WHERE id={id}')
    con.commit()
    cur.close()

#####################################################

def clean():
    queue.clear()

#####################################################

def makequeue(id):
    con = sql.connect("users.db")
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, login TEXT, Nick TEXT,stat INT, message TEXT)")
        cur.execute(f'SELECT Nick FROM users WHERE id=({id})')
        res = (cur.fetchall())
        print(res)
        queue.append(res)
    con.commit()
    cur.close()

#####################################################

def spisokid(id):
    if '@' in id:
        id=user(id)[0]
    con = sql.connect("users.db")
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `safequery` (Num INT,`id` INT, `Name` STRING)")
        info = cur.execute(f"SELECT * FROM safequery where id={id}")
        return info.fetchall()
    con.commit()
    cur.close()

#####################################################

def spisok(n):
    con = sql.connect("users.db")
    with con:
        if n==1:
            cur = con.cursor()
            cur.execute(f"SELECT id, Nick FROM users WHERE stat=(1)")
            results = (cur.fetchall())
            return results
        elif n==0:
            cur = con.cursor()
            cur.execute(f"SELECT id, Nick FROM users WHERE stat=(0)")
            results = (cur.fetchall())
            return results
    con.commit()
    cur.close()
#####################################################

def findgandona(id):
        con = sql.connect("users.db")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, login TEXT, Nick TEXT,stat INT, message TEXT)")
            cur.execute(f'SELECT Nick FROM users WHERE id=({id})')
            nick = (cur.fetchall())
            flaf = False
            for i in range(len(queue)):
                if nick == queue[i]:
                    flaf = True
        if flaf:
            return True
        else:
            return False
        con.commit()
        cur.close()
