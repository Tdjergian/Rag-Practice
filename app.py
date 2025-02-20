from flask import Flask, request
from RagFunctions.contribute import addSession
from RagFunctions.search import get_sessions_text
from AIFunctions.askQuestion import askQuestion

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return "Hello, client!"

@app.route('/', methods=['POST'])
def postSession():
    return addSession(request)

@app.route('/search', methods=['POST'])
def searchSession():
    return get_sessions_text(request)


@app.route('/ask', methods=['POST'])
def ask():
    return askQuestion(request)

if __name__ == '__main__':
    app.run(debug=True)




