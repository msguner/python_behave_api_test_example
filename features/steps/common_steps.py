import requests
from assertpy import assert_that
from behave import step, given, when, then

"""Common api steps"""


@step('a request url is "{url}"')
def step_impl(context, url):
    context.url = url


@step('add path "{path}"')
def step_impl(context, path):
    if not hasattr(context, 'path'):
        context.path = ""
    context.path += "/" + str(path)


@step('add parameter {key} = {val}')
def step_impl(context, key, val):
    if not hasattr(context, 'parameters'):
        context.parameters = {}

    if str(key) not in context.parameters.keys():
        context.parameters[str(key)] = str(val)


@step('add header key="{key}" and value="{val}"')
def step_impl(context, key, val):
    if not hasattr(context, 'headers'):
        context.headers = {}

    if str(key) not in context.headers.keys():
        context.headers[str(key)] = str(val)


@step('the response status code is "{status}"')
def step_impl(context, status):
    assert_that(context.response.status_code).is_equal_to(int(status))


@step("send get request")
def step_impl(context):
    context.response = requests.get(
        url=context.url + get_path(context),
        headers=get_headers(context),
        params=get_parameters(context),
        timeout=30)

    print("[GET] request -> %s" % context.response.url)


def get_parameters(context):
    return context.parameters if hasattr(context, 'parameters') else {}


def get_headers(context):
    return context.headers if hasattr(context, 'headers') else {}


def get_path(context):
    return context.path if hasattr(context, 'path') else ""
