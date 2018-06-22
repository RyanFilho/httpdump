from flask import Flask, request, send_file
from pprint import PrettyPrinter
import os

app = Flask(__name__)

@app.route('/')
def index():
	logFile = open(os.getcwd() + '/dump.txt', 'a')
	pp = PrettyPrinter(indent=4, stream=logFile)
	pp.pprint(request.__dict__)
	return ':)'

@app.route('/log', methods=['GET'])
def log():
    pw = request.args.get('password', type = str)
    if pw == 'jetix123':
    	return send_file(os.getcwd() +  '/httpdump.txt')
    else:
    	return 'Send correct password in params :P'
    
if __name__ == "__main__":
	app.run(port=33507, debug=True)