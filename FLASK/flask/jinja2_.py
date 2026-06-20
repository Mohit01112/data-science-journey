## building url dynamically
## jinja 2 template engine
## variable rule
## jinja2 template engine


''' 
{{}} expressions to print output in htl
{{%...}} conditions,for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request


##wsgi application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><H1>welcome to best flask course.this should be an amzing course</H1></html>"

@app.route("/index",)
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello {name} welcome"
    return render_template("form.html")

@app.route("/success/<int:score>")
def success(score):
    res=''
    if score>=50:
        res="pass"
    else:
        res="fail"  
    return render_template('result.html',results=res)

# vriable rule
app.route("/successres/<int:score>")
def successres(score):
    res=''
    if score>=50:
        res="pass"
    else:
        res="fail"  
    exp={'score':score,'res':res}
    return render_template('result1.html',results=exp)


if __name__ == '__main__':
    app.run(debug=True)