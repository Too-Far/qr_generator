'''Module to handle the flask app'''
import flask
from flask import Flask

app = Flask(__name__)

app@route('/')
def blah():
    return "Hello Dummy"


if __name__ == '__main__':
    app.run(debug=True)