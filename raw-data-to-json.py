#Raw data was downloaded from Seattle city open data project. Run script to convert data into usable json 

import csv
import json
import time

import pandas as pd

csvFilePath = r'Seattle_Parks_and_Recreation_Parks_Features.csv'
jsonFilePath = r'park_features.json'

start = time.perf_counter()

df = pd.read_csv(csvFilePath)

# Remove unwanted columns from the data
df = df.drop(columns=["PMAID", "Alt_Name", "Feature_ID", "CHILD_DESC","YOUTH_ONLY"])

# Filter data by sporting features 
filtered_df = df[df["Feature_Desc"].str.contains("Tennis|Soccer|Ball|rugby|pool|cricket|boat|skate|track|golf", case=False)]

# Convert to json
jsonData = filtered_df.to_json(orient='records')

with open(jsonFilePath, 'w', encoding='utf-8') as f:
	json.dump(jsonData, f, ensure_ascii=False, indent=4)

finish = time.perf_counter()


print(f"Converted csv raw data to {len(filtered_df.index)} json rows successfully in {finish - start:0.4f} seconds")