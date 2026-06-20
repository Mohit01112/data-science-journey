from flask import Flask,render_template,request
'''
it creates an instance of the flask class
which will be your WSGI application.'''

##wsgi application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><H1>welcome to best flask course.this should be an amzing course</H1></html>"

@app.route("/index",)
def index():
    return render_template("index.html")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello {name} welcome"
    return render_template("form.html")

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello {name} welcome"
    return render_template("form.html")

def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)