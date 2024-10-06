#Raw data was downloaded from Seattle city open data project. Run script to convert data into usable json 

import csv, sqlite3, time

csvFilePath = r'Seattle_Parks_and_Recreation_Parks_Features.csv'

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

start = time.perf_counter()

cur.executemany("INSERT INTO ParkFeatures (name, feature_desc, hours, xpos, ypos, location) VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()
cur.close()

finish = time.perf_counter()


print(f"Converted csv raw data to {resultCount} json rows successfully in {finish - start:0.4f} seconds")