# main.py

import pandas as pd
import numpy as np
import sqlite3

def load_data(path):
    """Load dataset from CSV"""
    return pd.read_csv(path)

def main():
    print("Starting project pipeline...")
    # Example loading
    # df = load_data('data/raw/sample.csv')
    # print(df.head())

if __name__ == "__main__":
    main()
