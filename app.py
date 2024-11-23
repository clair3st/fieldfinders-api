# Importing flask and creating a flask application get 
import flask, json, sqlite3, os
from dotenv import load_dotenv
from flask import request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

load_dotenv()
db_uri = os.environ.get("DB_URI")

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app, orgins="*")

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
	return "Field Finders. This site is a prototype API for park facility data."

@app.route('/features/all', methods=['GET'])
def api_all():
	conn = sqlite3.connect(db_uri)
	conn.row_factory = dict_factory
	cur = conn.cursor()
	data = cur.execute('SELECT * FROM ParkFeatures;').fetchall()
	return jsonify(data)

@app.route('/features/<feature>', methods=['GET'])
def api_feature(feature):
	conn = sqlite3.connect(db_uri)
	conn.row_factory = dict_factory
	cur = conn.cursor()
	data = cur.execute(f"SELECT xpos, ypos, name, feature_desc, location, id, hours from ParkFeatures where feature_desc like '%{feature}%' group by xpos;").fetchall()
	return jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
    return "404. The resource could not be found.", 404


if __name__ == "__main__":
    app.run(port=8000, debug=True)