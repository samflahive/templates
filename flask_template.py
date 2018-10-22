from flask import Flask, render_template, request, url_for, redirect, session
import os # only needed if session being used


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def home():
         return render_template("landing.html")

@app.route("/", methods=["GET", "POST"])
def login():
         # user is coming here from a post request
         if request.method == "POST":
                  # extract the value entered into the email field
                  email = request.form["email"]
                  # some logic here - database ?
                  # send page back with data inserted
                  return render_template("landing.html", username = email)
         else:
                  return render_template("login.html")

if __name__ == "__main__":
         app.run()
