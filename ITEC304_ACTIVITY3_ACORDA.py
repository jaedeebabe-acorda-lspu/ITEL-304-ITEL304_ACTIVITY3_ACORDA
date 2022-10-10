from lib2to3.pgen2.token import GREATER
from flask import Flask, request

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """<html><body>
                    <h1>HELLO</h1>
                    <form action='/greet'>
                        What's' your Name? <input type='text' name='name'><br>
                        Your Age? <input type='text' name='age'><br>
                        <input type='submit' value='Submit'>
              </body></html>
           """

@app.route('/greet')
def greet():
    name = request.args.get('name')
    age = request.args['age']
    if age == '':
        msg = ''
    else:
        msg = age

    return """
        <html><body>
                    <h2>{0} is {1}<h2>
              </body></html>
           """.format(name, msg)


# Launch the Flask dev server
app.run(host="localhost", debug=True)
