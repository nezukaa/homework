from flask import Flask
from random import choice
app = Flask(__name__)
facts_list=["факт 1","факт 2"]
@app.route('/')
def start():
    return '<h1><a href="/facts"> Посмотреть слуаный факт </a> <br> <a href= "/coin"> Орел или решка </a> <h1>'
@app.route("/facts")
def facts():
    return f'<p>{choice(facts_list)}</p>'
@app.route("/coin")
def coin():
    return f'<p>{choice(["Орел","Решка"])}<p>'

app.run(debug=True)

