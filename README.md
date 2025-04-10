# Wolt data analyst internship assignment

For this assignment we were given two tasks. The first tasks is to create tables and queries according to the pdf provided. The second task is to create a whole report with visualizations based on the csv file provided named `dataset_for_datascience_assignment.csv`.

## Directory tree

```bash
├── Data Science Internship Assignment - 2025.pdf
├── README.md
├── task1
│   ├── db
│   │   ├── dbCreation.py
│   └── sql
│       ├── queries
│       │   ├── query1.sql
│       │   ├── query2.sql
│       │   ├── query3a.sql
│       │   └── query3b.sql
│       └── schema
│           └── tables.sql
└── task2
    ├── conversionOs.py
    ├── dataset_for_datascience_assignment.csv
    ├── firstPurchase.py
    ├── __init__.py
    ├── notebook.ipynb
    ├── osCountry.py
    ├── osSpending.py
    ├── parsing.py
    └── task2.py
```

## TASK 1

For the first task you will find that we have no mock data to test our queries and tables. Therefore I devised a script to create some mock database to test them. The directory tree shows us that `task1` has two other directories: `sql` and `db`. The `dbCreation.py` script is contained within the `db` directory. For this task I designed my queries to comply with SQLite3, since it is friendlier towards a small project, such as this one.

Execute the script with the following line:

```bash
python3 dbCreation.py
```

This line creates the database named `wolt_mock.db` using the tables from `tables.sql` inside `task1/sql/schema/`. Afterwards you can test the queries using the following commands (considering that you are in the same directory as the db)

```bash
sqlite3 wolt_mock.db < ../sql/queries/query1.sql
sqlite3 wolt_mock.db < ../sql/queries/query2.sql
sqlite3 wolt_mock.db < ../sql/queries/query3a.sql
sqlite3 wolt_mock.db < ../sql/queries/query3b.sql
```

## TASK 2

### Required packages

For this script to work, you need to install pandas and numpy

```bash
sudo apt install python3-pandas
sudo apt install python3-numpy
sudo apt install python3-matplotlib
```


