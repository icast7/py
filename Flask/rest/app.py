#!/Users/icastillejos/Documents/py/flaskenv/bin/python
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

tasks = [
	{
	'id' : 1,
	'title': u'Buy groceries',
	'description': u'Milk, Cheese, Pizza, Fruit',
	'done': False
	},
	{
	'id' : 2,
	'title': u'Learn Python',
	'description': u'Need to find a good python rest tutorial',
	'done': False
	}
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
	return jsonify({'tasks':tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	task = filter(lambda t: t['id'] == task_id, tasks)
	if len(task) == 0:
		abort(404)
	return jsonify({'task' : task[0]})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found!'}), 404)

@app.route('/')
def index():
	return "Hello World! Tutorial de Miguel!"

if __name__ == '__main__':
	app.run(debug=True)