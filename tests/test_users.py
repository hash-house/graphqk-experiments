from datetime import datetime
from gql import gql
from pytest import fixture
import json


@fixture
def create_mutation():
    return gql("""
    mutation createUser ($names: AWSJSON!, $email: String!, $created_at: AWSTimestamp!, $created_by: String!, $updated_at: AWSTimestamp!, $updated_by: String!) {
        createUser(input: {created_at: $created_at, created_by: $created_by, email: $email, names: $names, updated_at: $updated_at, updated_by: $updated_by}) {
            email
            names
            id
        }
    }
    """)


@fixture
def delete_mutation():
    return gql("""
    mutation deleteUser ($id: ID!) {
        deleteUser(input: {id: $id}) {
            id
            email
            names
        }
    }
    """)


@fixture
def email():
    return 'test@test.tst'


@fixture
def get_query():
    return gql("""
    query getUser ($id: ID!) {
        getUser(id: $id) {
            names
            email
        }
    }
    """)


@fixture
def list_query():
    return gql("""
    query listUsers {
        items {
            id
            names
        }
    }
    """)


@fixture
def names():
    return json.dumps({'first': 'Furst', 'last': 'Lazt', 'hash': 'HashittyHashHash'})


@fixture
def now():
    return int(datetime.now().timestamp())


@fixture
def replacement_email():
    return 'new@email.com'


@fixture
def update_mutation():
    return gql("""
    mutation updateUser ($id: ID!, $names: AWSJSON, $email: String, $created_at: AWSTimestamp, $created_by: String, $updated_at: AWSTimestamp!, $updated_by: String!) {
        updateUser (input: {created_at: $created_at, created_by: $created_by, email: $email, id: $id, names: $names, updated_at: $updated_at, updated_by: $updated_by}) {
            id
            names
            email
        }
    }
    """)


@fixture
def user(client, create_mutation, delete_mutation, email, names, now):
    user_attrs = {'email': email, 'names': names, 'created_at': now, 'created_by': now, 'updated_at': now, 'updated_by': now}
    result = client.execute(create_mutation, variable_values=user_attrs)['createUser']
    yield result
    client.execute(delete_mutation, variable_values={'id': result['id']})


def test_create(client, create_mutation, email, names, now):
    user_attrs = {'email': email, 'names': names, 'created_at': now, 'created_by': now, 'updated_at': now, 'updated_by': now}
    response = client.execute(create_mutation, variable_values=user_attrs)
    result = response['createUser']
    assert result['email'] == email


def test_get(client, get_query, user):
    response = client.execute(get_query, variable_values={'id': user['id']})
    result = response['getUser']
    assert result == user


def test_update(client, now, replacement_email, update_mutation, user):
    update_values = {'id': user['id'], 'email': replacement_email, 'updated_at': now, 'updated_by': 'test'}
    response = client.execute(update_mutation, variable_values=update_values)
    result = response['updateUser']
    assert result['email'] == replacement_email
