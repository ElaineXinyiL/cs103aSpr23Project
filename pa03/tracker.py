'''
A Python script tracker.py which will allow the user to interact with the database.
It offers the user the following options and makes calls to the Transaction class to update the database.

0. quit
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''

from transaction import Transaction
import datetime
import sys


def print_usage():
    print('''
        quit: quit the program
        show: show transactions
        add: add transaction, usage: add amount category date description
        \te.g. add 10.00 food 2020-01-01 lunch
        delete: delete transaction, usage: delete item #
        \te.g. delete item 1
        7. summarize transactions by date
        summarize transactions by month: usage: sum_by_month
        summarize transactions by year: usage: sum_by_year
        summarize transactions by category: usage: sum_by_category
        help: print this menu
        ''')


def print_transaction(transactions):
    '''
    Print the transactions in a nice format.
    '''
    if len(transactions) == 0:
        print('No transactions found.')
        return
    print('item\tamount\tcategory\tdate\t\tdescription')
    for transaction in transactions:
        print('\t'.join([str(x) for x in transaction]))


def process_args(arglist):
    '''
    Process the arguments and call the corresponding functions.
    '''
    transaction = Transaction('tracker.db')
    if arglist == ['help']:
        print_usage()
    elif arglist == ['show']:
        print_transaction(transaction.select_all())
    elif arglist[0] == 'add':
        if len(arglist) != 5:
            print(
                'Invalid number of arguments. Correct usage: add amount category date description')
            return

        try:
            amount = float(arglist[1])
        except ValueError:
            print('Invalid amount. Please use a number.')
            return

        category = arglist[2]

        try:
            date = arglist[3]
            datetime.datetime.strptime(arglist[3], '%Y-%m-%d')
        except ValueError:
            print('Invalid date format. Please use YYYY-MM-DD.')
            return

        description = arglist[4]
        transaction.add_transaction(amount, category, date, description)
    elif arglist[0] == 'delete':
        if (len(arglist) != 3):
            print('Invalid number of arguments. Correct usage: delete item #')
            return
        try:
            id = int(arglist[2])
        except ValueError:
            print('Invalid id. Please specify an id number.')
            return
        transaction.delete_transaction(id)
    elif arglist[0] == 'sum_by_category':
        print(transaction.sum_by_category())
    elif arglist[0] == 'sum_by_year':
        print(transaction.sum_by_year())
    elif arglist[0] == 'sum_by_month':
        print(transaction.sum_by_month())
    else:
        print(' '.join(arglist), "not implemented. Try 'help' for a list of commands.")


def main():
    '''
    Main function of the program.
    Author: Ruihao Shen
    '''
    if len(sys.argv) == 1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        args = ''
        while True:
            args = input('command> ')
            if args == '':
                continue
            elif args == 'quit' or args == 'exit':
                break
            process_args(args.strip().split(' '))
        print('Bye!')
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)


if __name__ == '__main__':
    main()
