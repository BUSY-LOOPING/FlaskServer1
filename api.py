from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def return_ascii() :
    dct = {}
    inputChar = str(request.args['query'])
    ans = str(ord(inputChar))
    dct['output'] = ans
    return dct

if __name__ == "__main__" :
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port=port)