#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask

# Create Flask application
application = Flask(__name__, instance_relative_config=True)

# Loads the appropriate configuration
ON_HEROKU = int(os.environ.get("HEROKU", 0)) == 1
if ON_HEROKU:
    # Deployment on Heroku
    application.config.from_pyfile("heroku.py", silent=False)
else:
    application.config.from_pyfile("production.py", silent=False)
