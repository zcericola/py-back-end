# server.py
#request allows for http requests to be made
from flask import Flask, request
#returns json data
from flask import jsonify, Response
#imports CORS
from flask_cors import CORS

import requests

#creating an instance of flask server
app = Flask(__name__)
#Cors to allow request from port 3000 to port 5000 where my server is being run
CORS(app)

@app.route("/test", methods= ['GET'])
def hello():
    if request.method == 'GET':        
        return "Hello World!"

# Not getting anything back from the externalAPI yet..
@app.route("/api/getinfo", methods = ['GET'])
def get_info():
    if request.method == 'GET':
        info= requests.get('http swapi.co/api/planets/1')
        return info.json()

#needed but not sure why yet
if __name__ == "__main__":
    app.run()