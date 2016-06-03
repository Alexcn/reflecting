#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


from app import app
from flask.ext.script import Manager
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
