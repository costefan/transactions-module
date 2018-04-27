import json

from flask import request, make_response, jsonify

from app.config.api_config import API_PORT
from app.models import ShopTransaction, UserAccount, UserAccTransaction
from app import application


def _get_user(user_id):
    get_user_query = UserAccount.objects(user_id=int(user_id))
    return get_user_query[0] if get_user_query.count() > 0 else None


@application.route('/create_transaction/', methods=['POST'])
def create_transaction():
    data_dict = json.loads(request.data.decode('utf-8'))
    user_id = data_dict['attendee_id']
    product_id = data_dict['product_id']
    shop_id = data_dict['shop_id']
    user_obj = _get_user(user_id)
    amount = data_dict.get('amount', 10)
    if not user_obj:
        return make_response(jsonify({'success': False, 'message': 'Not Existing UserId'}), 422)
    elif user_obj.amount_available < amount:
        return make_response(jsonify({'success': False, 'message': 'Not Enough Money'}), 400)
    try:
        UserAccount.filter(user_id=user_id).update(amount_available=user_obj.amount_available - amount)
        UserAccTransaction.create(user_id=user_id,
                               shop_id = shop_id,
                               amount = amount,
                               product_id = product_id)
    except Exception as e:
        return make_response(jsonify({'success': False, 'message': str(e)}), 400)
    return make_response(jsonify({'success': True, 'message': 'Transaction Was Successful'}), 200)


@application.route('/create_user/', methods=['POST'])
def create_user():
    data_dict = json.loads(request.data.decode('utf-8'))
    user_id = data_dict['user_id']
    name = data_dict['user_name']
    initial_amount = float(data_dict.get('initial_amount', 0))
    try:
        UserAccount.create(user_id = user_id, user_name = name, amount_available = initial_amount)
    except Exception as e:
        return make_response(jsonify({'success': False, 'message': str(e)}), 505)
    return make_response(jsonify({'success': True, 'message': 'User Was Created'}), 200)


@application.route('/refill_account', methods=['POST'])
def refill_account():
    data_dict = json.loads(request.data.decode('utf-8'))
    user_id = data_dict['user_id']
    refill_amount = float(data_dict.get('amount', 0))
    current_balance = _get_user(user_id).get('amount_available', 0)
    try:
        UserAccount.iff(user_id = user_id, amount_available = current_balance + refill_amount)
    except Exception as e:
        return make_response(jsonify({'success': False, 'message': str(e)}), 505)
    return make_response(jsonify({'success': True, 'message': 'Account Was Refilled'}), 200)


@application.route('/alive/', methods=['GET'])
def test():
    return make_response(jsonify({'success': True, 'message': 'Alive'}), 200)


def serve_api():
    application.run(debug=True, port=API_PORT)


















