from gql import gql
from pytest import fixture


@fixture
def get_query():
    return gql("""
    query getSimple ($id: ID!) {
        getSimple(id: $id) {
            id
            name
        }
    }
    """)


@fixture
def list_query():
    return gql("""
    query listSimple {
        listSimples {
            items {
                id
                name
            }
            nextToken
        }
    }
    """)


def test_create(client, create_mutation, name):
    response = client.execute(create_mutation, variable_values={'name': name})
    record = response['createSimple']
    assert 'id' in record.keys()
    assert record['name'] == name


def test_get(client, get_query, name, simple):
    response = client.execute(get_query, variable_values={'id': simple['id']})
    record = response['getSimple']
    assert record['name'] == name


def test_list(client, list_query, name, simple):
    response = client.execute(list_query)
    result = response['listSimples']['items']
    assert result[0]['name'] == name
