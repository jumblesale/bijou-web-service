from behave import *
import web_service.app as app
from os import path


path_to_data = path.join(path.dirname(__file__), '..', '..', '..', 'data')


@given(u'I have imported example data from {file_name}')
def step_impl(context, file_name):
    app.init_db()
    json_file = path.join(path_to_data, '{0}.json'.format(file_name))
    with open(json_file, 'r') as contents:
        app.import_from_json(contents.read())


@when(u'I get all categories from the database')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I get all categories from the database')


@then(u'I get the following list of categories')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get the following list of categories')
