from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/quemsomos") 
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contato") 
def contato():
    return render_template("contato.html")

if __name__ == '__main__':
    app.run()