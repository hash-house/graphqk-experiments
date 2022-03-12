from lib.generic import entry, table
from pytest import mark, raises
from graphql.graphql import GraphQLError


def test_delete(client, name, simple):
    result = entry.delete(client, 'Simple', simple['id'])
    assert result['deleteSimple']['name'] == name


@mark.parametrize('table_name', ['Event', 'Kennel', 'Simple', 'Trail', 'TrailAssignment', 'User'])
def test_list_table(client, table_name):
    result = table.list_contents(client, table_name)
    assert True
    if result:
        for entry in result:
            assert '_version' not in entry.keys()


def test_list_table_does_not_exist(client):
    with raises(GraphQLError):
        table.list_contents(client, 'this-should_not_be_a_real_table_name')


@mark.parametrize('table_name', ['Event', 'Kennel', 'Simple', 'Trail', 'TrailAssignment', 'User'])
def test_list_table_all_versions(client, table_name):
    result = table.list_contents(client, table_name)
    assert True
    if result:
        for row in result:
            assert '_version' in row.keys()


def test_table_empty(client):
    assert not table.empty(client, 'Simple')
