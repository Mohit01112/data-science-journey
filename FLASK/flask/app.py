from flask import Flask
'''
it creates an instance of the flask class
which will be your WSGI application.'''

##wsgi application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to best flask course.this should be an amzing course"

@app.route("/index")
def index():
    return "this is a index page ha haaaa........."

if __name__ == '__main__':
    app.run(debug=True)