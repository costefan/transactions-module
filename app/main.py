from cassandra.cluster import Cluster

from .config.database import CASSANDRA_HOST, CASSANDRA_KEYSPACE


def setup_db():
    cluster = Cluster()
    session = cluster.connect(CASSANDRA_KEYSPACE)
    