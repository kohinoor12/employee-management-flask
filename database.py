from flask import g
import sqlite3 

def connect_to_database():
    sql = sqlite3.connect('employeemanagement.db')
    sql.row_factory = sqlite3.Row
    return sql 


def get_database():
    if not hasattr(g, 'employeemanagement.db'):
        g.employeemanagement_db = connect_to_database()
    return g.employeemanagement_db


