from flask import Flask, render_template
from pymongo import Connection

app = Flask(__name__)
db = Connection(host='192.168.59.103').seam

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
