# -*- coding: utf-8 -*-
from flask.ext.script import Manager
from seam.core import app

app.debug = True
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
