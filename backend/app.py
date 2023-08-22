from flask import Flask, jsonify, request, redirect, url_for
# from database.db import db, User
import logging
from flask_login import login_user, logout_user, login_required
from chat.chat import chat_blueprint
from flask_cors import CORS

import os

app = Flask(__name__)
# This will enable CORS for all routes
CORS(app)

CORS(app, origins=["http://localhost:5173/"])


app.register_blueprint(chat_blueprint)

app.logger.setLevel(logging.DEBUG)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db/mydatabase'
# db.init_app(app)

@app.route('/')
def home():
    app.logger.debug("here")
    return jsonify(message="Hello, World!")

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     user = User.query.filter_by(username=username).first()
#     if user is None or not user.check_password(password):
#         return 'Invalid username or password'
#     login_user(user)
#     return redirect(url_for('index'))

# @app.route('/signup', methods=['POST'])
# def signup():
#     app.logger.debug(request)
#     username = request.form.get('username')
#     password = request.form.get('password')
#     user = User(username=username)
#     user.set_password(password)
#     db.session.add(user)
#     db.session.commit()
#     return redirect(url_for('login'))

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)

