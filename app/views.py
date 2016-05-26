from app import app
from flask import jsonify, abort
from flask import make_response
from flask import render_template


# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'nickname': 'Miguel'}
#     return '''
#     <html>
#         <header>
#             <title>Home Page</title>
#         </header>
#         <body>
#                 <h1>Hello, ''' + user['nickname'] + ''' </h1>
#             </body>
#         </html>
#         '''
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel' }
    return render_template('index.html',
                           title = 'Home',
                           user = user)



tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_tasks2(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Fuond'}), 404)