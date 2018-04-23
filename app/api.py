import json

from cassandra.cluster import Cluster
from flask import Flask, request, make_response, jsonify

from app.config.database import CASSANDRA_KEYSPACE
from app.models import ShopTransaction, UserAccount

app = Flask(__name__)


class TransactionAPI(object):

    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect(CASSANDRA_KEYSPACE)

    def _get_user(self, user_id):
        get_user_query = UserAccount.objects(user_id=int(user_id))
        return get_user_query[0] if get_user_query.count > 0 else None

    def _send_statistics(self, products):
        pass

    @app.route('/create_transaction/', methods=['POST'])
    def create_transaction(self):
        data_dict = json.loads(request.data)
        user_id = data_dict['user_id']
        amount = data_dict['total_amount']
        user_obj = self._get_user(user_id)

        if not user_obj:
            return make_response(jsonify({'success': False, 'message': 'Not Existing UserId'}), 422)
        elif user_obj.amount_available < amount:
            return make_response(jsonify({'success': False, 'message': 'Not Enough Money'}), 505)

        try:
            UserAccount.iff(user_id=user_id).update(amount_available=user_obj.amount_avaliable - amount)
            ShopTransaction.create(user_id=user_id,
                                   shop_id = data_dict['shop_id'],
                                   name = data_dict['shop_name'],
                                   amount = data_dict['amount'])
        except Exception as e:
            return make_response(jsonify({'success': False, 'message': str(e)}), 505)

        return make_response(jsonify({'success': True, 'message': 'Transaction Was Successful'}), 200)

    @app.route('/create_user/', methods=['POST'])
    def create_transaction(self):
        data_dict = json.loads(request.data)
        name = data_dict['user_name']
        initial_amount = float(data_dict.get('initial_amount', 0))


        try:
            UserAccount.create(name = name, amount_available = initial_amount)
        except Exception as e:
            return make_response(jsonify({'success': False, 'message': str(e)}), 505)

        return make_response(jsonify({'success': True, 'message': 'User Was Created'}), 200)

    @app.route('/refill_account/', methods=['POST'])
    def create_transaction(self):
        data_dict = json.loads(request.data)
        user_id = data_dict['user_id']
        refill_amount = float(data_dict.get('amount', 0))

        current_balance = self._get_user(user_id).get('amount_available', 0)

        try:
            UserAccount.iff(user_id = user_id, amount_available = current_balance + refill_amount)
        except Exception as e:
            return make_response(jsonify({'success': False, 'message': str(e)}), 505)

        return make_response(jsonify({'success': True, 'message': 'Account Was Refilled'}), 200)


def serve_api():
    api = TransactionAPI()


















