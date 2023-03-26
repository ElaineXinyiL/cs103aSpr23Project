## PA03 Finance Tracker - using SQL, pytest, and pylint

### Functions included:
1. Supports CRUD operations (Create, Read, Update, Delete) on expenses and aggregation(with SQLite3) 
2. Incorporated with automated testing (with pytest) 
3. Fields stored for transactions: 'item #', 'amount', 'category', 'date', 'description'


### pylint script:
1) tracker.py
```
PS C:\Users\Irislee\Desktop\22 Fall\SE fundamentals\sql-project\cs103aSpr23Project\pa03> pylint tracker.py
************* Module tracker
tracker.py:52:0: R0912: Too many branches (14/12) (too-many-branches)

------------------------------------------------------------------
Your code has been rated at 9.86/10 (previous run: 9.29/10, +0.57)
```
2) transactions.py
```
PS C:\Users\Irislee\Desktop\22 Fall\SE fundamentals\sql-project\cs103aSpr23Project\pa03> pylint transaction.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.70/10, +0.30)
```

### pytest script:
```
================================================================== test session starts ===================================================================
platform win32 -- Python 3.10.10, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\Irislee\Desktop\22 Fall\SE fundamentals\sql-project\cs103aSpr23Project\pa03
collected 8 items

test_transaction.py ........                                                                                                                        [100%]

=================================================================== 8 passed in 0.80s ====================================================================
```

### tracker.py script:
```
PS C:\Users\Irislee\Desktop\22 Fall\SE fundamentals\sql-project\cs103aSpr23Project\pa03> python3 tracker.py
command> help

        quit/exit: quit the program
        show: show transactions
        add: add transaction, usage: add amount category date description
                e.g. add 10.00 food 2020-01-01 lunch
        delete: delete transaction, usage: delete item #
                e.g. delete item 1
        summarize transactions by date: usage: sum_by_date
        summarize transactions by month: usage: sum_by_month
        summarize transactions by year: usage: sum_by_year
        summarize transactions by category: usage: sum_by_category
        help: print this menu

command> show
item    amount  category        date            description
1       4.32    food    2023-03-07      dunki
2       6.52    food    2023-03-01      mcdonald
3       5.29    food    2023-03-08      wendy
4       32.65   grocery 2023-03-15      Hannaford
5       54.16   grocery 2023-03-15      MB
6       10.29   grocery 2023-03-15      Walgreen
7       1.7     transportation  2023-03-06      bustoschool
8       3.2     transportation  2023-03-12      boston_subway
9       10.0    entertainment   2023-03-01      iceskating
10      13.5    entertainment   2023-03-17      movies
11      875.0   housing 2022-12-01      monthly_rent
12      875.0   housing 2022-01-01      monthly_rent
command> add  
Invalid number of arguments. Correct usage: add amount category date description
command> add 21.5 transportation 2022-12-28 uber 
command> show
item    amount  category        date            description
1       4.32    food    2023-03-07      dunki
2       6.52    food    2023-03-01      mcdonald
3       5.29    food    2023-03-08      wendy
4       32.65   grocery 2023-03-15      Hannaford
5       54.16   grocery 2023-03-15      MB
6       10.29   grocery 2023-03-15      Walgreen
7       1.7     transportation  2023-03-06      bustoschool
8       3.2     transportation  2023-03-12      boston_subway
9       10.0    entertainment   2023-03-01      iceskating
10      13.5    entertainment   2023-03-17      movies
11      875.0   housing 2022-12-01      monthly_rent
12      875.0   housing 2022-01-01      monthly_rent
13      21.5    transportation  2022-12-28      uber
command> delete item
Invalid number of arguments. Correct usage: delete item #
command> delete item 13
command> show
item    amount  category        date            description
1       4.32    food    2023-03-07      dunki
2       6.52    food    2023-03-01      mcdonald
3       5.29    food    2023-03-08      wendy
4       32.65   grocery 2023-03-15      Hannaford
5       54.16   grocery 2023-03-15      MB
6       10.29   grocery 2023-03-15      Walgreen
7       1.7     transportation  2023-03-06      bustoschool
8       3.2     transportation  2023-03-12      boston_subway
9       10.0    entertainment   2023-03-01      iceskating
10      13.5    entertainment   2023-03-17      movies
11      875.0   housing 2022-12-01      monthly_rent
12      875.0   housing 2022-01-01      monthly_rent
command> sum_by_date
[('2022-01-01', 875.0), ('2022-12-01', 875.0), ('2023-03-01', 16.52), ('2023-03-06', 1.7), ('2023-03-07', 4.32), ('2023-03-08', 5.29), ('2023-03-12', 3.2), ('2023-03-15', 97.1), ('2023-03-17', 13.5)]
command> sum_by_month
[('2022-01', 875.0), ('2022-12', 875.0), ('2023-03', 141.63)]
command> sum_by_year
[('2022', 1750.0), ('2023', 141.63)]
command> sum_by_category
[('entertainment', 23.5), ('food', 16.13), ('grocery', 97.1), ('housing', 1750.0), ('transportation', 4.9)]
command> random input
random input not implemented. Try 'help' for a list of commands.
command> exit
Bye!
```
