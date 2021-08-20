import requests
from assertpy import assert_that
from behave import step, given, when, then

from features.utils.constants import NHTSA_API_URL
from features.utils.utils import split_text, compare_lists

""" Step definitions of NHTSA API """


@step("get all vehicle manufacturers from nhtsa api")
def step_impl(context):
    response = requests.get(url=f'{NHTSA_API_URL}/vehicles/getallmanufacturers',
                            params={"format": "json"},
                            headers={'Content-type': 'application/json'})

    context.response = response
    context.all_vehicle_manufacturers = response.json()["Results"]


@step('get filtered vehicle manufacturers by country "{country}"')
def step_impl(context, country):
    all_manufacturers = context.all_vehicle_manufacturers
    filtered_manufacturers = list()
    try:
        filtered_manufacturers = [manufacturer for manufacturer in all_manufacturers if manufacturer["Country"] == country]
    except:
        print("Manufacturers could not be filtered by country('%s')" % country)

    context.filtered_manufacturers_by_country = filtered_manufacturers
    context.filtered_manufacturers = filtered_manufacturers


@step('verify that there are "{count}" manufacturers')
def step_impl(context, count):
    assert_that(context.filtered_manufacturers).is_length(int(count))


@when('get filtered vehicle manufacturers by manufacturer common name "{common_name}"')
def step_impl(context, common_name):
    all_manufacturers = context.all_vehicle_manufacturers
    filtered_manufacturers = list()
    try:
        filtered_manufacturers = [manufacturer for manufacturer in all_manufacturers if manufacturer["Mfr_CommonName"] == common_name]
    except:
        print("Manufacturers could not be filtered by common name('%s')" % common_name)

    context.filtered_manufacturers_by_common_name = filtered_manufacturers
    context.filtered_manufacturers = filtered_manufacturers


@step('verify filtered manufacturers common names are "{common_names}"')
def step_impl(context, common_names):
    common_names_in_response = [manufacturer["Mfr_CommonName"] for manufacturer in context.filtered_manufacturers]
    assert_that(compare_lists(split_text(common_names), common_names_in_response)).is_true()
