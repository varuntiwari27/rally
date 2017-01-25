#!flask/bin/python
from flask import Flask, jsonify, abort, request
import subprocess
import json
import parser
from subprocess import Popen, PIPE
app = Flask(__name__)


@app.route('/general', methods=['POST'])
def general():
    x = request.json
    print("action1 :", x["action1"])
    print("action2 :", x["action2"])
    cmd = ["rally",x['action1'],x['action2']]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out  

@app.route('/generic', methods=['POST'])
def generic():
    x = request.json
    print("action1 :", x["action1"])
    print("action2 :", x["action2"])
    print("cloud_name :", x["cloud_name"])
    cmd = ["rally",x['action1'],x['action2'],x['cloud_name']]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out  

   
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
