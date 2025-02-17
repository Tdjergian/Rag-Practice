from flask import Flask, request
from routeHandlers.test import LogStuff
from RagFunctions.contribute import addSession



app = Flask(__name__)



@app.route('/', methods=['GET'])
def get():
    return "Hello, client!"

@app.route('/', methods=['POST'])
def post():
    return addSession(request)



if __name__ == '__main__':
    app.run(debug=True)




