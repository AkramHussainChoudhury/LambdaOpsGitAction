from flask import Flask,jsonify,request

app = Flask(__name__)


@app.route('/greet',methods=['GET'])
def greet():
    return jsonify({'message':'Hello from Lambda application'})

