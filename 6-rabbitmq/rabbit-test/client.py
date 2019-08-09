import os

from flask import Flask

from celery import Celery
import celery.states as states

celery = Celery('tasks')
celery.config_from_object('celeryconfig')

env = os.environ
app = Flask(__name__)


# Send two numbers to add
@app.route('/add/<int:param1>/<int:param2>')
def add(param1, param2):
    task = celery.send_task('mytasks.add', args=[param1, param2])
    return task.id


# Check the status of the task with the id found in the add function
@app.route('/check/<string:id>')
def check_task(id):
    res = celery.AsyncResult(id)
    return res.state if res.state == states.PENDING else str(res.result)


if __name__ == '__main__':
    app.run(debug=env.get('DEBUG', True),
            port=int(env.get('PORT', 5000)),
            host=env.get('HOST', '0.0.0.0'))
