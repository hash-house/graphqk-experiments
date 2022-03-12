from gql import gql
from lib import build_client
from pytest import fixture
import os


@fixture
def api_key():
    try:
        os.environ['api_key']
    except KeyError:
        print('api_key must be set as an environment variable')


@fixture
def api_url():
    try:
        os.environ['api_url']
    except KeyError:
        print('api_url must be set as an environment variable')


@fixture
def client(api_key, api_url):
    return build_client()


@fixture
def create_mutation():
    return gql("""
    mutation CreateSimple ($name: String!) {
        createSimple(input: {name: $name}) {
            id
            name
        }
    }
    """)


@fixture
def delete_mutation():
    return gql("""
    mutation DeleteSimple ($id: ID!) {
        deleteSimple(input: {id: $id}) {
            id
            name
        }
    }
    """)


@fixture
def name():
    return 'simple'


@fixture
def simple(client, create_mutation, delete_mutation, name):
    response = client.execute(create_mutation, variable_values={'name': name})
    record = response['createSimple']
    yield record
    client.execute(delete_mutation, variable_values={'id': record['id']})
