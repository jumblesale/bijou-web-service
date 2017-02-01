from flask import Flask, make_response
import json

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# set up the sqlite instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/bijou.db'
db = SQLAlchemy(app)


# define the db models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    discounted_price = db.Column(db.Integer)
    high_price = db.Column(db.Integer)
    item_number = db.Column(db.String(32), unique=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('products', lazy='dynamic'))

    def __init__(self, name, discounted_price, high_price, item_number, category):
        self.name = name
        self.discounted_price = discounted_price
        self.high_price = high_price
        self.item_number = item_number
        self.category = category

    def __repr__(self):
        return '<Product {0}>'.format(self.name)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Category {0}>'.format(self.title)


def import_from_json(json):
    """
    Import data into the database from a JSON file
    :param json: a json string represting categories and products
    :return: Nothing
    """
    pass


@app.route('/')
def hello():
    return json_response({'message': 'hello'})


def json_response(obj, status=200):
    return make_response((
        json.dumps(obj), status, {'Content-Type': 'application/json'}
    ))

if __name__ == "__main__":
    app.run()
