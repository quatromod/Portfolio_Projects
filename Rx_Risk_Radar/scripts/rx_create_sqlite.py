import pandas as pd
import sqlite3          # built in Pythin library

# Paths
csv_path = "/Users/a.avira/Pet/Portfolio_Projects/Rx_Risk_Radar/data/processed/faers_joined_20Q4.csv"
db_path = "/Users/a.avira/Pet/Portfolio_Projects/Rx_Risk_Radar/data/processed/faers.db"

# Load the CSV
df = pd.read_csv(csv_path)

# Connect to SQLite and create the table
conn = sqlite3.connect(db_path)
df.to_sql("faers_2020q4", conn, if_exists="replace", index=False)
conn.close()

print(f"✅ SQLite database created at {db_path}")