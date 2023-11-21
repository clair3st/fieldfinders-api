# Importing flask and creating a flask application get 
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "Field Finders. This site is a prototype API for park facility data."

app.run()