from copy import deepcopy
from invoke import Context
from pytest import fixture
from tasks import table


@fixture
def context():
    return Context()


def test_table_clean(api_key, api_url, context, simple):
    result = table.clean(context, 'Simple')
    assert result == 'Removed 1 items from Simple'


def test_table_contents(api_key, api_url, context, simple):
    result = table.contents(context, 'Simple')
    expected = deepcopy(simple)
    expected.pop('name')
    assert result == [expected]
