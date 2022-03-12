from gql import gql


def delete(client, table: str, id_):
    request = (f"mutation delete ($id: ID!) "
               f"{{delete{table}(input: {{id: $id}}) {{ name }} }}")
    response = client.execute(gql(request), variable_values={'id': id_})
    return response


