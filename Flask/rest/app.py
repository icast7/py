#!/Users/icastillejos/Documents/py/flaskenv/bin/python

from flask.ext.httpauth import HTTPBasicAuth
from flask import Flask, jsonify, abort, make_response, request, url_for


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


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'miguel':
		return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error':'Unauthorized access'}), 401)

def make_public_task(task):
	new_task = {}
	for field in task:
		if field == 'id':
			new_task['uri'] =  url_for('get_task', task_id = task['id'], _external = True)
		else:
			new_task[field] = task[field]
	return new_task

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
	task = filter(lambda t: t['id'] ==  task_id, tasks)
	if len(task) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'title' in request.json and type(request.json['title']) != unicode:
		abort(400)
	if 'description' in request.json and type(request.json['description']) is not unicode:
		abort(400)
	if 'done' in request.json and type(request.json['done']) is not bool:
		abort(400)
	task[0]['title'] =  request.json.get('title', task[0]['title'])
	task[0]['description'] =  request.json.get('description', task[0]['description'])
	task[0]['done'] =  request.json.get('done', task[0]['done'])
	return jsonify({'task' : make_public_task(task[0])})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
	task = filter(lambda t: t['id'] ==  task_id, tasks)
	if len(task) == 0:
		abort(404)
	tasks.remove(task[0])
	return jsonify({'result': True})

#Added HATEOAS
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
	if not request.json or not 'title' in request.json:
		abort(400)
	task = {
		'id' : tasks[-1]['id'] + 1,
		'title' : request.json['title'],
		'description' : request.json.get('description', ""),
		'done': False
	}
	tasks.append(task)
	return jsonify({'task': make_public_task(task)}), 201

#Added HATEOAS
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
	return jsonify({'tasks': map(make_public_task, tasks)})

#Added HATEOAS
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	task = filter(lambda t: t['id'] == task_id, tasks)
	if len(task) == 0:
		abort(404)
	return jsonify({'task' : make_public_task(task[0])})

#Error hadler
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found!'}), 404)

#Mapped root URI
@app.route('/')
def index():
	return "Hello World! Tutorial de Miguel!"

#Run application
if __name__ == '__main__':
	app.run(debug=True)
