from behave import *
import web_service.app as app
from os import path
import requests as r
from web_service.config import host


path_to_data = path.join(path.dirname(__file__), '..', '..', '..', 'data')


@given(u'I have imported example data from {file_name}')
def step_impl(context, file_name):
    app.init_db()
    json_file = path.join(path_to_data, '{0}.json'.format(file_name))
    with open(json_file, 'r') as contents:
        app.import_from_json(contents.read())


@when(u'I get all categories from the database')
def step_impl(context):
    response = r.get(host['url'] + '/categories')
    assert 200 == response.status_code
    context.response = response.json()


@then(u'I get the following list of categories')
def step_impl(context):
    expected_titles = [row['title'] for row in context.table]
    actual_titles = context.response
    print(context.response)