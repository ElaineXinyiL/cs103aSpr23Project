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
        Author: Ruihao Shen
        '''
        self.db_file = db_file
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions (
            item INTEGER PRIMARY KEY,
            amount REAL,
            category TEXT,
            date TEXT,
            description TEXT
        )''')

    def select_all(self):
        '''
        Select all the transactions and return the result.
        Author: Ruihao Shen
        '''
        return self.run_query('SELECT * FROM transactions')

    def add_transaction(self, amount, category, date, description):
        '''
        Add a transaction to the database.
        Author: Ruihao Shen
        '''
        self.run_query('INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)',
        (amount, category, date, description))

    def delete_transaction(self, rowid):
        '''
        Delete a transaction in the database.
        Author: Hongqian Li
        '''
        self.run_query('DELETE FROM transactions WHERE rowid = (?)', (rowid,))

    def sum_by_category(self):
        '''
        Summarize transactions by category.
        Author: Hongqian Li
        '''
        return self.run_query('SELECT category, SUM(amount) FROM transactions GROUP BY category', ())

    def sum_by_year(self):
        '''
        Summarize transactions by year.
        Author: Yichun Huang
        '''
        query = '''
            SELECT strftime('%Y', date) as year, SUM(amount) 
            FROM transactions 
            GROUP BY year
            ORDER BY year
        '''
        result = self.run_query(query)
        return result
    
    def sum_by_date(self):
        '''
        Summarize transactions by date.
        Author: Yixuan He
        '''
        query = '''
            SELECT strftime('%Y-%m-%d', date) as date, SUM(amount) 
            FROM transactions
            GROUP BY date
            ORDER BY date
        '''
        result = self.run_query(query, ())
        return result

    def run_query(self, query, parameters=()):
        '''
        Run a query on the database and return the result.
        Author: Ruihao Shen
        '''
        with sqlite3.connect(self.db_file) as con:
            cursor = con.cursor()
            cursor.execute(query, parameters)
            result = cursor.fetchall()
            con.commit()
        return result
