"""Flask app controller"""

from sqlite3 import Error
from functools import wraps

from flask import session, redirect, request, flash, jsonify, g
from datetime import datetime


def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            print('ds')
            return redirect('/signin')
        return f(*args, **kwargs)

    return decorated_function


def assert_fields(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print('ds')
        if request.method == 'POST':
            error = None
            print('Heloo')
            for name in request.form:
                # print(name)
                # print(request.form[name])
                if not request.form[name]:
                    flash(f'Field {name} is empty.')
                    return redirect(request.environ['REMOTE_ADDR'])
        return f(*args, **kwargs)

    return decorated_function


def jsonify_response(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = jsonify(f(*args, **kwargs))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    return decorated_function


def editTransaction(id, name, amount, note, date, tag):
    try:
        g.db.execute(
            f'UPDATE transactions SET transaction_name = {name}, transaction_amount = {amount}, transaction_note = {note}, transaction_date = {date}, tag_id = {tag}'
        )
        g.db.commit()
        return True
    except Error:
        return False


#WORKS
def deleteTransaction(id):
    try:
        g.db.execute(f'DELETE FROM transactions WHERE transaction_id = {id}')
        g.db.commit()
        return True
    except Error:
        return False


#WORKS
def deleteTag(id):
    try:
        g.db.execute(f'DELETE FROM tags WHERE tag_id = {id}')
        g.db.commit()
        return True
    except Error:
        raise (Error)
        return False


#WORKS
def deleteTodo(id):
    try:
        g.db.execute(f'DELETE FROM todos WHERE todo_id = {id}')
        g.db.commit()
        return True
    except Error:
        return False


# def quickStats():
#     try:
#         info = g.db.execute(
#             f'SELECT * FROM transactions WHERE user_id = {session["user"]["id"]}'
#         ).fetchall()
#
#         currentYear = datetime.now().year
#         currentMonth = datetime.now().month
#         currentDay = datetime.now().day
#
#         money = dict()
#         money["day"] = 0
#         money["month"] = 0
#         money["year"] = 0
#
#         for item in info:
#             date = item['transaction_date'].split("-")
#             year = int(date[0])
#             month = int(date[1])
#             day = int(date[2])
#
#             if year == currentYear:
#                 money["year"] += item['transaction_amount']
#                 if month == currentMonth:
#                     money["month"] += item['transaction_amount']
#                     if month == currentDay:
#                         money["day"] += item['transaction_amount']
#
#
#         return True
#     except Error:
#         return False
