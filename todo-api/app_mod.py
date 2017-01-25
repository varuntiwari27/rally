#!flask/bin/python
from flask import Flask, jsonify, abort, request
import subprocess
import json
import parser
from subprocess import Popen, PIPE
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello, World!"

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/echo')
def get_echo():
 x = "pwd"
 return x

@app.route('/list')
def get_list():
    cmd = ["rally","verify","list"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route('/samplepost', methods=['POST'])
def samplepost():
    x = request.json
    y = json.loads(x)
#    print("value : ", x)
    cmd = ["rally","deployment","use","y['cloud_name']"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out  

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
