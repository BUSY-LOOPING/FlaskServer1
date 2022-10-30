import sys
if sys.version_info[0:2] != (3, 9):
    raise Exception('Requires python 3.9')

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def return_ascii() :
    dct = {}
    inputChar = str(request.args['query'])
    ans = str(ord(inputChar))
    dct['output'] = ans
    return dct

if __name__ == "__main__" :
    app.run()