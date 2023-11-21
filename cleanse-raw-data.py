#Raw data was downloaded from Seattle city open data project. Run script to convert data into usable json 

import csv
import json
import time

import pandas as pd

csvFilePath = r'Seattle_Parks_and_Recreation_Parks_Features.csv'
jsonFilePath = r'park_features.json'

start = time.perf_counter()

jsonArray = []

df = pd.read_csv(csvFilePath)

print(df.iloc[0])
 
print("---------------")


finish = time.perf_counter()


print(f"Converted csv raw data to json successfully in {finish - start:0.4f} seconds")