## fieldfinders-api
Flask api for fieldfinders data

following a tutorial found [here](https://nordicapis.com/how-to-create-an-api-from-a-dataset-using-python-and-flask/)

Raw data was downloaded from Seattle city open data project.

# Setup:
run:

```
python3 utiles/cleanse-raw-data.py
```
This creates a database `ParkFeatures` in sqlite3 and inserts park features from the csv into the database. TODO: make this so it only add stuff I'm interested in

# Run app:
`source venv/bin/activate` to activate virtual env
`flask run`

# Endpoint:
`/api/v1/resources/features/all` lists all features from the city of seattle
`/api/v1/resources/features/<feature>` allows to list by feature, only supports select list of sports