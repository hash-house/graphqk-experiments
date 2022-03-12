from gql import Client
from gql.transport.requests import RequestsHTTPTransport
import os


def build_client() -> Client:
    api_url = os.environ.get('api_url', None)
    api_key = os.environ.get('api_key', None)
    if api_url is None or api_key is None:
        print('api url and api key must be provided as env args')
        exit(1)
    transport = RequestsHTTPTransport(url=api_url, headers={'x-api-key': api_key})
    return Client(transport=transport, fetch_schema_from_transport=True)
