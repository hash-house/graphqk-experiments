from gql import gql
from gql_query_builder import GqlQuery
from typing import List
from lib.generic import entry


def clean(client, name: str):
    for entry_id in list_contents(client, name):
        entry.delete(client, name, id_=entry_id)


def empty(client, name: str) -> bool:
    return list_contents(client, name) is []


def list_contents(client, name: str) -> List:
    name = f"list{name}s"
    fields = ['id']
    item_sub_fields = GqlQuery().fields(fields, name='items').generate()
    request = GqlQuery().fields([item_sub_fields, 'nextToken']).query(name).operation(name=name).generate()
    response = client.execute(gql(request))
    items = response[name]['items']
    return items
