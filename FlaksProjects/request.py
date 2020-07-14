from flask import Flask,request,jsonify
import requests
import base64
import json 
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/',methods = ['GET','PUT'])
def rasp():
    with open('danone.jpeg', 'rb') as imgesFile:
        imagestr = base64.b64encode(imgesFile.read())
    
    if request.method == 'GET':
        return imagestr
@app.route('/11',methods = ['GET','PUT'])
def alo():

    data  = requests.get("http://192.168.88.147:8080/12").content

    return jsonify(data)


if __name__=="__main__":
    app.run(debug=True,host='localhost',port=6666)