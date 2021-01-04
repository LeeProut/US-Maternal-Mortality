from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'sqlite:///maternal.sqlite')

db = SQLAlchemy(app)

class MMR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String)
    State_Code = db.Column(db.Integer)
    Year = db.Column(db.Integer)
    Deaths = db.Column(db.Integer)
    Births = db.Column(db.Integer)
    Maternal_Mortality_Ratio = db.Column(db.Integer)
    Population = db.Column(db.Integer)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cdc-mmr') 
def  cdcPostGres():
    mmr = db.session.query(MMR)
    data = []

    for mmr in mmr: 
        item = {
             'id': mmr.id, 
             'State': mmr.State,
             'State_Code': mmr.State_Code, 
             'Year': mmr.Year, 
             'Deaths': mmr.Deaths, 
             'Births': mmr.Births,
             'Maternal_Mortality_Ratio': mmr.Maternal_Mortality_Ratio,
             'Population': mmr.Population
        }
        data.append(item)
    return jsonify(data)

@app.route('/api/cdc-mmr', methods=('POST',))
def createMMR():
    data = json.loads(request.data)
    mmr = MMR(State=data['State'])

    db.session.add(mmr)
    db.session.commit()
    return data  

@app.route('/api/cdc-mmr/<id>', methods=('DELETE',))
def deleteState(id):
    mmr = db.session.query(MMR).get(id)
    db.session.delete(mmr) 
    db.session.commit()
    return id  

if __name__ == '__main__':
    app.run(debug=True)



