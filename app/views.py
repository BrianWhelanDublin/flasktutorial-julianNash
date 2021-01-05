from app import app
from flask import render_template, request, redirect
from datetime import datetime


@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


@app.route("/jinja")
def jinja():

    my_name = "Brian"

    age = 30

    langs = ["Python", "Javascript", "Html"]

    friends = {
        "Tom": 30,
        "Amy": 60,
        "Tony": 56,
        "Clarissa": 23
    }

    colours = ("Red", "Green")

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pulling repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote(
        name="Flask Jinja",
        description="Template design tutorial",
        url="https://github.com"
    )

    def repeat(x, qty):
        return x * qty

    date = datetime.utcnow()

    return render_template("public/jinja.html",
                           my_name=my_name, age=age, langs=langs,
                           friends=friends, colours=colours, cool=cool,
                           GitRemote=GitRemote, repeat=repeat,
                           my_remote=my_remote, date=date
                           )


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        print(req, username,
              email, password)

        return redirect(request.url)
    return render_template("public/sign_up.html")


users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}


@app.route("/profile/<username>")
def profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template("public/profile.html", user=user,
                           username=username)
