from invoke import Collection
from .table import table_tasks


ns = Collection()
ns.add_collection(table_tasks, name='table')
