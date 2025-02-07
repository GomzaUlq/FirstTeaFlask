from flask import Blueprint, jsonify, request, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from backend.db import db

user_bp = Blueprint('user', __name__, template_folder="templates")


@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Пользователь с таким email уже существует!"}), 400

    new_user = User(
        username=data['username'],
        first_name=data['first_name'],
        email=data['email'],
        password_hash=generate_password_hash(data['password']),
        slug=data["slug"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Пользователь успешно зарегистрирован!"}), 201


@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        return jsonify({"message": "Успешный вход!"}), 200
    return jsonify({"message": "Неверный email или пароль!"}), 401


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "email": user.email,
            "slug": user.slug,

        }), 200
    return jsonify({"message": "Пользователь не найден"}), 404


@user_bp.route('/register', methods=['GET'])
def show_register():
    return render_template('users/registration_page.html')


@user_bp.route('/login', methods=['GET'])
def show_login():
    return render_template('users/login.html')


@user_bp.route('/logout', methods=['POST'])
def log_out():
    session.pop('user_id', None)
    return jsonify({"message": "Вы успешно вышли из системы!"}), 200
