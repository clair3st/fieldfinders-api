## fieldfinders-api
Flask api for fieldfinders data

following a tutorial found [here](https://nordicapis.com/how-to-create-an-api-from-a-dataset-using-python-and-flask/)

Raw data was downloaded from Seattle city open data project.

# Setup:
run:
```
python3 raw-data-to-json.py
```
This extracts desired data from csv file.

followed by:
```
python3 cleanse-raw-data.py
```
This creates a database `ParkFeatures` in sqlite3 and inserts park features into the database.

# Run app:
`source venv/bin/activate` to activate virtual env
`flask run`

# Endpoint:
`/api/v1/resources/features/all`