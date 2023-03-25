'''
Test the Transaction class.
'''
import os
import sqlite3
import pytest

from transaction import Transaction

@pytest.fixture
def tuples():
    '''
    Create a list of tuples that can be used to create transactions.
    '''
    return [
        (1, 1.0, 'food', '01/01/2018', 'test'),
        (2, 2.0, 'food', '01/01/2018', 'test'),
        (3, 3.0, 'food', '01/01/2018', 'test'),
    ]

@pytest.fixture
def db_path(tmpdir):
    '''
    Create a temporary database file.
    '''
    yield os.path.join(tmpdir, 'test_transaction.db')

@pytest.fixture(autouse=True)
def transaction(db_path, tuples):
    '''
    Create and initialize the transaction database in /tmp.
    '''
    con = sqlite3.connect(db_path)
    con.execute('''CREATE TABLE IF NOT EXISTS transactions (
        item INTEGER PRIMARY KEY,
        amount REAL,
        category TEXT,
        date TEXT,
        description TEXT
    )''')
    con.executemany('INSERT INTO transactions VALUES (?, ?, ?, ?, ?)', tuples)
    con.commit()
    transaction = Transaction(db_path)
    yield transaction
    con.execute('DROP TABLE transactions')
    con.commit()


def test_select_all(transaction, tuples):
    '''
    Test that select_all returns the correct tuples.
    '''
    assert transaction.select_all() == tuples

def test_add_transaction(transaction, tuples):
    '''
    Test that add_transaction adds a transaction to the database.
    '''
    transaction.add_transaction(4.0, 'food', '01/01/2018', 'test')
    assert transaction.select_all() == tuples + [(4, 4.0, 'food', '01/01/2018', 'test')]