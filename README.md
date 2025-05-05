# Restaurant data

For this assignment we were given two tasks. The first tasks is to create tables and queries according to the pdf provided. The second task is to create a whole report with visualizations based on the csv file provided named `dataset_for_datascience_assignment.csv`.

## Directory tree

```bash
├── README.md
├── requirements.txt
├── task1
│   ├── db
│   │   └── dbCreation.py
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
    ├── firstAndLast.py
    ├── firstPurchase.py
    ├── __init__.py
    ├── notebook.ipynb
    ├── osCountry.py
    ├── osSpending.py
    ├── parsing.py
    ├── task2.py
    └── Wolt-data-presentation.pptx
```

## HOWTO

### Task one

For the first task you will find that we have no mock data to test our queries and tables. Therefore I devised a script to create some mock database to test them. The directory tree shows us that `task1` has two other directories: `sql` and `db`. The `dbCreation.py` script is contained within the `db` directory. For this task I designed my queries to comply with SQLite3, since it is friendlier towards a small project, such as this one.

Execute the script with the following line:

```bash
python3 dbCreation.py
```

This line creates the database named `wolt_mock.db` using the tables from `tables.sql` inside `task1/sql/schema/`. Afterwards you can test the queries using the following commands (considering that you are in the same directory as the db)

Be sure to have SQLite3 installed on your device. If you are using Linux Ubuntu, you can use the following line:

```bash
sudo apt install sqlite3
```

If you are using mac, you may use homebrew:

```bash
brew install sqlite3 
```

After that, execute the following lines in CLI:

```bash
sqlite3 wolt_mock.db < ../sql/queries/query1.sql
sqlite3 wolt_mock.db < ../sql/queries/query2.sql
sqlite3 wolt_mock.db < ../sql/queries/query3a.sql
sqlite3 wolt_mock.db < ../sql/queries/query3b.sql
```

___

### Task two

Before going further, you may want to create a python virtual environment to run this project:

```bash
python3 -m venv <your-virtual-environment>
```

After creating the virtual environment, you may run it by using the following line:

```bash
source <your-virtual-environment>/bin/activate
```

To deactivate the virtual environment later, just run this line:

```bash
deactivate
```

If you managed to start the virtual environment, install the required packages in `requirements.txt`:

```bash
pip install -r requirements.txt
```

After running the requirements our virtual environment should contain `pandas`, `matplotlib`, `numpy`, and `jupyter notebook`. The notebook is the most important part for the next parts.

Now run the following line to open up the notebook:

```bash
jupyter notebook
```

As you run this line, your web browser should open up a tab and you will be able to see the directories of this project. Navigate into `task2` directory and open the notebook named `notebook.ipynb`. After this, you should be able to see the rendered notebook and view the extracted and wrangled data.

The codeblocks inside the notebook can be interacted with, which means that you can change the code inside it for a number of reasons - e.g. change the parameters of functions to choose specific countries.

After running changes, you have to press the "run" button to apply the changes from any code blocks into the notebook.

### About the data

All data comes the csv file called `dataset_for_datascience_assignment.csv` which was provided by Wolt. The dataset here has no relation with task one.

### About the structure of the project

The python files contained in (deciding folder structure still) contain a main() in `task2.py` which is purely made for testing. Extra visualizations were made for tables that are already displayed in the notebook, and the function are available commented inside the blocks of code in the notebook.
