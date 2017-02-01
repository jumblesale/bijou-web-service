from flask import Flask, make_response
import json

app = Flask(__name__)




@app.route('/')
def hello():
    return json_response({'message': 'hello'})


def json_response(obj, status=200):
    return make_response((
        json.dumps(obj), status, {'Content-Type': 'application/json'}
    ))

if __name__ == "__main__":
    app.run()
