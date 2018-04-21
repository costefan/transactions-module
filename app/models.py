from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from datetime import datetime

from app.config.currency import UKRAINIAN_CURENCY


class UserAccTransaction(Model):
    user_id = columns.Integer(primary_key=True)
    transaction_ts = columns.TimeUUID(primary_key=True, clustering_order='DESC')  # Clustering key
    shop_id = columns.Integer()
    amount = columns.Float(required=True)
    currency = columns.Text(required=True, default=UKRAINIAN_CURENCY)
    timestamp = columns.DateTime(default=datetime.now())


class ShopTransaction(Model):
    shop_id = columns.Integer(primary_key=True)
    name = columns.Text(static=True)
    type = columns.Text(static=True)
    product_type = columns.Text(primary_key=True)  # Clustering key
    transaction_ts = columns.TimeUUID(primary_key=True, clustering_order='DESC')  # Clustering key
    currency = columns.Text()
