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


# Using INNER JOIN because we only want cases that have both patient and drug info
demo_drug = pd.merge(demo, drug, on = "primaryid", how = "inner")
# Again using INNER JOIN to ensure we include only complete reports with a reaction listed
demo_drug_reac = pd.merge(demo_drug, reac, on = "primaryid", how = "inner")


# Selecting meaningful fields for analysis and Tableau export
columns = [                  
    "primaryid",                                                 # unique report ID
    "caseid",                                                    # case ID (sometimes reused across reports)
    "age", "age_cod", "sex",                                     # patient details
    "drugname", "drug_seq", "role_cod",                          # drug details
    "pt"                                                         # 'preferred term' – the reported adverse reaction
]
final_df = demo_drug_reac[columns]



# Initialising the output path to export cleaned dataset to a CSV file for further use (SQL, Tableau, etc.).
output_path = "/Users/a.avira/Pet/Portfolio_Projects/Rx_Risk_Radar/data/processed/faers_joined_20Q4.csv"

# Save the file
final_df.to_csv(output_path, index=False)


print("✅ Exported cleaned FAERS data to:", output_path)


