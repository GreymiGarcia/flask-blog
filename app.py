from flask import Flask, render_template, url_for, flash
from forms import RegitrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a500575d5b701b4ce460418d796b36d8'

posts = [
    {
        'author': 'Greymi Garcia',
        'title': 'Blog Post 1',
        'content': ' First post content',
        'date_posted': 'November 19, 2022'
    },
    {
        'author': 'Greymi Garcia',
        'title': 'Blog Post 2',
        'content': ' Second post content',
        'date_posted': 'November 20, 2022'
    },
    {
        'author': 'Greymi Garcia',
        'title': 'Blog Post 3',
        'content': ' Third post content',
        'date_posted': 'November 21, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegitrationForm()
    return render_template("regisster.html", title="Rrgiter", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)