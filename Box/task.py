from celery import Celery
from DropBox.celery import app
from Box.models import *


@app.task
def del_file(x):
    data = user_files.objects.filter(Filename=x)
    data.delete()