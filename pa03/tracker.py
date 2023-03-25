'''
A Python script tracker.py which will allow the user to interact with the database.
It offers the user the following options and makes calls to the Transaction class to update the database.

0. quit
1. show categories
2. add category
3. modify category
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
        1. show categories
        2. add category
        3. modify category
        4. show transactions
        5. add transaction
        6. delete transaction
        7. summarize transactions by date
        8. summarize transactions by month
        9. summarize transactions by year
        10. summarize transactions by category
        help: print this menu
        ''')

def process_args(arglist):
    '''
    Process the arguments and call the corresponding functions.
    '''
    transaction = Transaction('tracker.db')
    if arglist == ['help']:
        print_usage()
    else:
        print(' '.join(arglist), "not implemented. Try 'help' for a list of commands.")

def main():
    '''
    Main function of the program.
    Auther: Ruihao Shen
    '''
    if len(sys.argv) == 1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        args = ''
        while True:
            args = input('command> ')
            if args == '':
                continue
            elif args == 'quit':
                break
            process_args(args.strip().split(' '))
        print('Bye!')
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        

if __name__ == '__main__':
    main()