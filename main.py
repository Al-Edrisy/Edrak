import datetime

from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

#Requests code....

comments = requests.get("https://api.npoint.io/a1825a0b3bf1ab62f38e").json()["people"]
comments = list(comments)


@app.route("/")
def Home_Cennter():
    year = datetime.datetime.now().year

    return render_template("index.html", now_year=year, commenter=comments)


if __name__ == "__main__":

    app.run(debug=True)