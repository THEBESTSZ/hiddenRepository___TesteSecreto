## DEEP ESG Data Processing Technical Challenge

#### Work done by:

- William Felipe Tsubota 

### Initial considerations

- The repository name `hiddenRepository___TesteSecreto` it was to make searches more difficult.

### The algorithm

The functioning of the algorithm is entirely command-line based.

In addition to the main file (main.py), there are 3 other files, each containing a class, each of which has functions related to its given scope. 

In the program we have 4 menus (Main menu, Test Menu, Xlsx Menu and Sql Menu).

In the Main menu we have the options to process data through two xlsx files, process data through an sql file, or generate random tests. Choosing the option to process data through Xlsx files we enter in the Xlsx menu, choosing the option to process data through an sql file we enter in the Sql menu, and choosing the option to generate random tests we enter in the Main menu.

In the Xlsx menu we have a single option to populate a chart file. In this option we have as input the two xlsx files (general_ledger and chart_of_accounts), and as output the populated chart file.

In the Sql menu we have two options, one to populate a chart file and another to get data from the chart_of_accounts and ledger_ledger tables from a ".sql" file. Choosing the option "populate" we have as input a ".sql" file containing two tables (general_ledger and chart_of_accounts) which are later converted to python tuples, and as a output one archive ".xlsx" a chart file populated in the output folder. choosing the option to get data we have as input a ".sql" file containing two tables (general_ledger and chart_of_accounts) which are later converted to python tuples, and as a output their information displayed in command line.

In the test menu we can generate the input files.

### Decisions 

- The data type used to store the general_ledger was tuple, because it allows the repetition of values.

- To populate a chart_of_accounts file it is checked if the accounts in the general_ledger file match with the accounts in the chart_of_accounts file.

- Due to the complexity of the project, sqlite was used.

- The data type used to store the sums of the values of each general_ledger account was the dictionary, because it does not allow key repetition, and this made it easier to compare with the chart_of_accounts.

- In the test generator, there is a 75% chance to generate each account with at least one dot ("."). First the general_ledger is generated, then the chart_of_accounts is extracted from it.

- In the thest genrator, in the generateRandomLedger function we have the parameters quantity (limit of accounts to be generated), limitAccount (as a default value 50, only accounts from 1 to 50.50.50.50.50.50 can be generated), limitComma (the dot limit on the account is 5), limitValue (maximum value for each account).

### How to execute

Make sure you have [python 3.x or greater](https://www.python.org/downloads/) and some of your libraries: [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html) and [sqlite3](https://pypi.org/project/db-sqlite3/). Then clone the project to some folder of interest with the command: 

```Terminal
   git clone https://github.com/THEBESTSZ/hiddenRepository___TesteSecreto.git
```

Just browse to the folder `hiddenRepository___TesteSecreto` and run:

```Terminal
   python3 main.py
```
