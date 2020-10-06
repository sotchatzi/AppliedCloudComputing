from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://sotiris:1234@localhost/myvhost')


@app.task
def add(x, y):
    return x + y
