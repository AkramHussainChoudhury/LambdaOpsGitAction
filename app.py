from flask import Flask,jsonify,request
import awsgi

app = Flask(__name__)


@app.route('/greet',methods=['GET'])
def greet():
    return jsonify({'message':'Hello from Lambda application'})



def handler(event, context):
    response = awsgi.handle(app, event, context)
    print(f"Returning response: {response}") # Log the outgoing response
    return response
