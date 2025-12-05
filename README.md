## fieldfinders-api
Flask api for [Fieldfinders](https://github.com/clair3st/fieldfinders-react) data

Raw data was downloaded from Seattle city open data project.

Deployed to [pythonanywhere](http://clair3st.pythonanywhere.com/)

# Setup:
On first deployment, must set up the database and export data from csv to populate:

```
python3 utils/cleanse-raw-data.py
```
This creates a database `ParkFeatures` in sqlite3 and inserts park features from the csv into the database. 
TODO: make this so it only add stuff I'm interested in

# Run app locally:
`source venv/bin/activate` to activate virtual env
`pip install -r requirements.txt` to install required packages
`flask run`

# Endpoint:
`/features/all` lists all features from the city of Seattle
`/features/<feature>` allows listing by feature, only supports a select list of sports


# Resources:
Following a tutorial found [here](https://nordicapis.com/how-to-create-an-api-from-a-dataset-using-python-and-flask/)
