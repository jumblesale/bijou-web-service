# bijou-web-service

A tiny web service to retrieve categories and products.

## Endpoints

### `GET /categories`

Example response:

```
{
  "categories": [
    {
      "title": "Shirts"
    },
    {
      "title": "T-shirts"
    },
    {
      "title": "Polo Shirts"
    },
    {...}
  ]
}
```

### `GET /category/{title}`

Example response:

```
{
  "category": {
    "title": "Shirts"
  },
  "products": [
    {
      "name": "THE JENKINS LONG SLEEVE SHIRT",
      "discounted_price": "",
      "high_price": "55.00",
      "item_number": "F4KS70D6GP"
    },
    {
      "name": "THE MATLOCK LONG SLEEVE FLANNEL SHIRT",
      "discounted_price": "",
      "high_price": "42.00",
      "item_number": "F4WF50G0GP"
    },
    {
      "name": "THE BLYTHE POP-OVER SHORT SLEEVE SHIRT",
      "discounted_price": "",
      "high_price": "55.00",
      "item_number": "F4WS70A1GP"
    },
    {...}
  ]
}
```

### `GET /products`

Example response:

```
{
  "products": [
    {
      "name": "THE JENKINS LONG SLEEVE SHIRT",
      "discounted_price": "",
      "high_price": "55.00",
      "item_number": "F4KS70D6GP"
    },
    {
      "name": "THE MATLOCK LONG SLEEVE FLANNEL SHIRT",
      "discounted_price": "",
      "high_price": "42.00",
      "item_number": "F4WF50G0GP"
    },
    {
      "name": "THE BLYTHE POP-OVER SHORT SLEEVE SHIRT",
      "discounted_price": "",
      "high_price": "55.00",
      "item_number": "F4WS70A1GP"
    },
    {...}
  ]
}
```

## Requirements

* Python 3
* sqlite

## Building

Clone this repo then:

```
# create a virtual environment
python3 -m venv venv
# activate venv
source venv/bin/activate.sh
# install requirements
pip install -r requirements.txt
```

To start the webserver: `python web_service/app.py`

Now you can access it at `localhost:5000/products`

The db will appear in `/tmp/bijou.db` by default - you can change it in `app.py`
 if this is not appropriate.

If this url doesn't work for you, no problem, just change it in `web_service/config.py`

You can import data by starting a Python repl and passing in json:

```
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from web_service.app import import_from_json_file
>>> import_from_json_file('path/to/your/json/dump')
```

JSON dumps can be generated using the `bijou-scraper` service. Example
dumps are provided in `web_service/data`.

## Structure

The main motivation here was to have something really lean and instantly discoverable.
 This has been more or less achieved - the most verbose parts of the app
 are the model definitions and the method to import JSON data into the db.
 Everything important lives in `app.py` which just glues together a couple
 of `SQLAlchemy` models with a couple of really basic `GET` endpoints.

## Tests

The entire app is glue between Flask, SQLAlchemy and the data from the web
scraping service so unit tests felt like they would be extremely verbose for
no real value. Instead there's a suite of functional tests. You can run them
with `make tests`. They clear the db, import a JSON dump from the scraper
then test the API endpoints.

## Improvements

* The limitations of the system are mainly from the `bijou-scraper` service.
  Given more time there's plenty of other data that it would have been nice
  to have imported and having a better representation for prices would
  be a really nice thing to apply to the JSON responses.
* It might have been nice to have the models live in their own module
  so that it's immediately obvious what is functions and what is data.
  [This approach](http://stackoverflow.com/questions/9692962/flask-sqlalchemy-import-context-issue)
  looks like it would have separated these pretty nicely.

## What went well

* The functional testing is really nice, runs extremely quickly and was a
  pleasure to develop with. Having development driven by this outside-in
  approach led to some really satisfying moments where adding a few lines
  of controller code led to a feature going green.
