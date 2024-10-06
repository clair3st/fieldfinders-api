# Importing flask and creating a flask application get 
import flask
# import json
import sqlite3
from flask import request, jsonify
from flask_cors import CORS


app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app, orgins="*")


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
	return "Field Finders. This site is a prototype API for park facility data."

@app.route('/api/v1/resources/features/all', methods=['GET'])
def api_all():
	conn = sqlite3.connect('parks.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	data = cur.execute('SELECT * FROM ParkFeatures;').fetchall()
	return jsonify(data)

@app.route('/api/v1/resources/features/<feature>', methods=['GET'])
def api_feature(feature):
	print(feature)
	allowedSports = ['cricket', 'tennis', 'rugby', 'soccer', 'pool', 'boat', 'skate', 'track', 'golf','t-ball', 'softball', 'basketball', 'baseball', 'football']
	if (feature in allowedSports):
		conn = sqlite3.connect('parks.db')
		conn.row_factory = dict_factory
		cur = conn.cursor()
		data = cur.execute(f"SELECT xpos, ypos, name, feature_desc, location, id, hours from ParkFeatures where feature_desc like '%{feature}%' group by xpos;").fetchall()
		return jsonify(data)
	else:
		return'No sporting features for '.feature

@app.errorhandler(404)
def page_not_found(e):
    return "404. The resource could not be found.", 404


if __name__ == "__main__":
    app.run(port=8000, debug=True)