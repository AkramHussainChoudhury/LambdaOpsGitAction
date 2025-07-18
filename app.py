from flask import Flask,jsonify,request

app = Flask(__name__)


@app.route('/greet',methods=['GET'])
def greet():
    return jsonify({'message':'Hello from Lambda application'})



def lambda_handler(event, context):
    return aws_serverless_wsgi.handle_request(app, event, context)
