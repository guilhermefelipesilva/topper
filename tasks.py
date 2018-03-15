from __future__ import absolute_import, unicode_literals
from topper.worker import app

@app.task
def add(x, y):
    return x + y