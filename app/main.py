from cassandra.cluster import Cluster

from .config.database import CASSANDRA_HOST, CASSANDRA_KEYSPACE
from app.api import serve_api
from cassandra.cqlengine.management import sync_table
from app.models import *
from cassandra.cqlengine.connection import setup


def setup_db():
    # cluster = Cluster()
    # session = cluster.connect(CASSANDRA_KEYSPACE)
    # session.set_keyspace(CASSANDRA_KEYSPACE)
    setup(['127.0.0.1'], CASSANDRA_KEYSPACE, retry_connect=True)
    sync_table(UserAccount)
    sync_table(UserAccTransaction)
    sync_table(ShopTransaction)


def run_app():
    setup_db()
    serve_api()