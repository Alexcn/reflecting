#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from flask import Blueprint


auth = Blueprint('auth', __name__)

from . import views
