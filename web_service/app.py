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

    def __str__(self):
        return str(self.__dict__)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Category {0}>'.format(self.title)

    def __str__(self):
        return str(self.__dict__)


def init_db():
    db.drop_all()
    db.create_all()


def import_from_json(json_data):
    """
    Import data into the database from a JSON file
    :param json: a json string representing categories and products
    :return: Nothing
    """
    parsed = json.loads(json_data)
    for category in parsed:
        category_model = Category(category['title'])
        for product in category['products']:
            product_model = Product(
                product['name'],
                product['discounted_price'],
                product['high_price'],
                product['item_number'],
                category_model
            )
            db.session.add(product_model)
        db.session.add(category_model)
    db.session.commit()


@app.route('/categories', methods=['GET'])
def get_categories():
    # produce json of the string representations of all the categories
    return json_response(list(map(str, Category.query.all())))


def json_response(obj, status=200):
    return make_response((
        json.dumps(obj), status, {'Content-Type': 'application/json'}
    ))

if __name__ == "__main__":
    app.run()
