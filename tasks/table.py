from invoke import Collection, task
from lib import build_client
from lib.generic import entry, table


@task
def clean(_c, table_name):
    client = build_client()
    table_ids = table.list_contents(client, table_name)
    count = len(table_ids)
    for row in table_ids:
        entry.delete(client, table_name, id_=row['id'])
    message = f"Removed {count} items from {table_name}"
    print(message)
    return message


@task
def contents(_c, table_name):
    client = build_client()
    content = table.list_contents(client, table_name)
    print(content)
    return content


table_tasks = Collection('table')
table_tasks.add_task(clean)
table_tasks.add_task(contents)
