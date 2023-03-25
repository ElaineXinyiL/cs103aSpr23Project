'''
A Python class Transaction which will store financial transactions with the fields. 
It has an __init__ method where you pass in the filename for the database to be used (e.g. tracker.db) 
and each transaction has the following fields stored in a SQL table called transactions.

'item #',
'amount',
'category',
'date',
'description'

It will allows the user to read and update the database as need.
'''

import sqlite3


class Transaction:
    def __init__(self, db_file) -> None:
        '''
        Initialize the database file and create the table if it does not exist.
        Auther: Ruihao Shen
        '''
        self.db_file = db_file
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions (
            item INTEGER PRIMARY KEY,
            amount REAL,
            category TEXT,
            date TEXT,
            description TEXT
        )''')

    def run_query(self, query, parameters=()):
        '''
        Run a query on the database and return the result.
        Auther: Ruihao Shen
        '''
        with sqlite3.connect(self.db_file) as con:
            cursor = con.cursor()
            cursor.execute(query, parameters)
            result = cursor.fetchall()
            con.commit()
        return result