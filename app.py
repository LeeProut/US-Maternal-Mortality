from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'sqlite:///maternal.sqlite')

db = SQLAlchemy(app)

class MMR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    State


@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)



