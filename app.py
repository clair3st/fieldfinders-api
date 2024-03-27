# Importing flask and creating a flask application get 
import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "Field Finders. This site is a prototype API for park facility data."

@app.route('/api/v1/resources/features/all', methods=['GET'])
def api_all():
	with app.open_resource('park_features.json') as f:
		data = json.load(f)
	return jsonify(data)

app.run()