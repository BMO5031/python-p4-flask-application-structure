#!/usr/bin/env python3
#You start by importing the Flask module and creating an instance of the Flask application.

from flask import Flask

app = Flask(__name__)

# append to server/app.py
#You define a route '/' using the @app.route('/') decorator. When a user accesses the root URL of your application (e.g., http://yourdomain.com/), the index() function is called, and it returns a simple HTML message saying "Welcome to my page!".

@app.route('/')
def index():
    return '<h1>FUCK YOU UNANGAM!</h1>'

# append to server/app.py
#You define another route '/<username>' using the @app.route('/<username>') decorator. This route takes a parameter named username. When a user accesses a URL like http://yourdomain.com/johndoe, the user(username) function is called, and it returns an HTML message that includes the username in the header, e.g., "Profile for johndoe".
@app.route('/<username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# append to server/app.py

if __name__ == '__main__':
    app.run(port=5555, debug=True)



