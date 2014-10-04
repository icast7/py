#http://flask.pocoo.org/docs/0.10/quickstart/#a-minimal-application
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello Sarah Smith!"

if __name__ == "__main__":
	app.run()