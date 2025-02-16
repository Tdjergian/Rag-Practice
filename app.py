from flask import Flask
from routeHandlers.test import LogStuff

app = Flask(__name__)

@app.route('/')
def home():
    LogStuff()
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)