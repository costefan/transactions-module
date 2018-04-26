import uuid

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from app.config.currency import UKRAINIAN_CURENCY
from app.config.database import CASSANDRA_KEYSPACE


class UserAccTransaction(Model):
    __keyspace__ = CASSANDRA_KEYSPACE
    user_id = columns.Integer(primary_key=True)
    transaction_ts = columns.TimeUUID(primary_key=True, clustering_order='DESC', default=uuid.uuid1())  # Clustering key
    shop_id = columns.Integer()
    amount = columns.Float(required=True)
    currency = columns.Text(required=True, default=UKRAINIAN_CURENCY)
    success = columns.Boolean(required=True, default=True)
    product_id = columns.Integer()


class ShopTransaction(Model):
    __keyspace__ = CASSANDRA_KEYSPACE
    shop_id = columns.Integer(primary_key=True)
    name = columns.Text(static=True)
    type = columns.Text(static=True)
    product_id = columns.Integer(primary_key=True)  # Clustering key
    transaction_ts = columns.TimeUUID(primary_key=True, clustering_order='DESC')  # Clustering key
    amount = columns.Float(required=True)
    currency = columns.Text()


class UserAccount(Model):
    __keyspace__ = CASSANDRA_KEYSPACE
    user_id = columns.Integer(primary_key=True)
    user_name = columns.Text()
    amount_available = columns.Float(required=True, default=0)
