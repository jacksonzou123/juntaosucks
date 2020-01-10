"""Flask octa api endpoint"""

from flask import Blueprint, request, jsonify, session

from .controller import require_login

BP = Blueprint('octa', __name__, url_prefix='/octa')


@BP.route('/userinfo', methods=['POST'])
@require_login
def user_info():
    print('dsad')
    if request.method == 'POST':
        print('dsads')
        response = jsonify(session['user'])
        response.headers['Access-Control-Allow-Origin'] = '*'
        print(response)
        return response
