import firebase_admin
import flask
import pyfcm
from firebase_admin import credentials, messaging
from firebase_admin import firestore
from datetime import date
from datetime import datetime
from flask import request, jsonify
from pyfcm import FCMNotification

import urllib.request
import json
import time
import requests
import ast

firebase_admin.initialize_app()
db = firestore.client()

def hello_world(request):
    recdata = flask.request.json
    name=recdata['name']
    phone_no=recdata['phone_no']
    message="Hi "+name+", your phone number "+phone_no+" is registered now"
    status="True"

    response = {
        "status": status,
        "message": message
    }
return jsonify(response)