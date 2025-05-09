import pandas as pd
import os

# Set path to your raw data
data_path = "/Users/a.avira/Pet/Portfolio_Projects/Rx_Risk_Radar/data/raw"

# Converting "$" Separated .txt files and loading into  CSVs
demo = pd.read_csv(os.path.join(data_path, "DEMO20Q4.txt"), sep='$', encoding='latin1')
drug = pd.read_csv(os.path.join(data_path, "DRUG20Q4.txt"), sep='$', encoding='latin1')
reac = pd.read_csv(os.path.join(data_path, "REAC20Q4.txt"), sep='$', encoding='latin1')

# Quick check
print("Demo shape:", demo.shape)
print("Drug shape:", drug.shape)
print("Reac shape:", reac.shape)

# Optional preview
print(demo.head())
