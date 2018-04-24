from cassandra.cluster import Cluster

from .config.database import CASSANDRA_HOST, CASSANDRA_KEYSPACE
from app.api import serve_api


def setup_db():
    cluster = Cluster()
    session = cluster.connect(CASSANDRA_KEYSPACE)
    serve_api()


if __name__ == '__main__':
    setup_db()