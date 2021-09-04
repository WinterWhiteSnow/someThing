from flask import Flask, render_template, request
import math
import random
from random import*

a = list(range(1,46))


app = Flask(__name__)

@app.route("/")
def main():
  return render_template("home.html")

@app.route("/random")
def random():
  b = sample(a,6)
  b.sort()  
  return render_template("index.html", result=b)


if __name__ == "__main__":
    app.run()	