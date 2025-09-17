Simulate Python Pandas Module

This project is a simple simulation of the Python Pandas module, built entirely with Python standard libraries. It mimics the basic functionality of Pandas DataFrame, including reading CSV files, accessing and modifying data, and performing simple operations.

📑 Modules

module.py → Core DataFrame Simulation

Implements a custom DataFrame class with support for:

Read CSV files into a DataFrame object.

Access data by row (df[1]).

Access data by column (df["Name"]).

Access individual cell (df[1]["Name"]).

Modify a whole column (df["Salary"] = [50000,60000,70000]).

Modify a single cell (df[1]["Salary"] = 65000).

Create new columns (df["Bonus"] = [2000,2500,3000]).

Display DataFrame (df.show()).

Save DataFrame to a file (df.save_to_file("new_emps.csv")).

Perform column operations:
df["Salary"].sum()
df["Salary"].max()
df["Salary"].min()

Handles invalid operations via Exception Handling.

main.py → Demonstration Script

Imports the custom module.

Demonstrates reading, displaying, and manipulating a dataset (emps.csv).

Performs column operations and saves results to new_emps.csv.

📂 Project Structure

Simulate-python-pandas-module


├── emps.csv          # Sample dataset

├── new_emps.csv      # Example of saved dataframe

├── module.py         # Core mini-Pandas simulation

├── main.py           # Demo script showing usage

├── README.md         # Project documentation

└── LICENSE           # License file

⚙️ Requirements

Python 3.8+

Works on Windows, macOS, and Linux

No external dependencies (only Python standard libraries like csv and os are used)
