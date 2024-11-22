#Raw data was downloaded from Seattle city open data project. Run script to convert data into usable json 

import csv, sqlite3, time, os
from dotenv import load_dotenv


csvFilePath = r'utils/Seattle_Parks_and_Recreation_Parks_Features.csv'

load_dotenv()
db_uri = os.environ.get("DB_URI")

con = sqlite3.connect("parks.db") # connect to database, will create if not exist
cur = con.cursor()
sql = ("CREATE TABLE IF NOT EXISTS ParkFeatures ("
		"id INTEGER PRIMARY KEY AUTOINCREMENT, "
		"name TEXT,"
		"feature_desc TEXT,"
		"hours TEXT, "
		"xpos REAL NOT NULL, "
		"ypos REAL NOT NULL, "
		"location TEXT);")


cur.execute(sql)


with open(csvFilePath, 'r') as fin:
	dr = csv.DictReader(fin)
	to_db = [(i['Name'], i['Feature_Desc'], i['hours'], i['xPos'], i['yPos'], i['Location 1']) for i in dr if i['xPos']]
	resultCount = len(to_db)

print(resultCount)
if(resultCount > 0):
	start = time.perf_counter()

	cur.executemany("INSERT INTO ParkFeatures (name, feature_desc, hours, xpos, ypos, location) VALUES (?, ?, ?, ?, ?, ?);", to_db)
	con.commit()
	cur.close()

	finish = time.perf_counter()

	print(f"Converted csv raw data to {resultCount} db rows successfully in {finish - start:0.4f} seconds")
else:
	print("no data")