"""
rx_create_sqlite.py

This script creates a SQLite database from a cleaned FAERS dataset.

🔹 What it does:
- Loads the joined and cleaned CSV file: `faers_joined_20Q4.csv`
- Connects to (or creates) a local SQLite database: `faers.db`
- Creates a SQL table named `faers_2020q4` and inserts the CSV data into it
- Replaces the table if it already exists

🔹 Why this is useful:
- Allows you to query FAERS data using SQL
- Enables exploration and visualization with tools like DBeaver or Tableau
- Makes analysis more efficient than repeatedly processing raw `.txt` files

Author: quatromod
"""