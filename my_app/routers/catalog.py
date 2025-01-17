from flask import Blueprint, jsonify, request, render_template

from models import Product, Category
from backend.db import db

product_bp = Blueprint('products', __name__, template_folder="templates")
category_bp = Blueprint('categories', __name__, template_folder="templates")
main_bp = Blueprint('main', __name__, template_folder="templates")
about_bp = Blueprint('about', __name__, template_folder="templates")
states_bp = Blueprint('states', __name__, template_folder='../templates')


@category_bp.route('/categories', methods=['Post'])
def create_category():
    data = request.get_json()
    new_category = Category(
        name=data['name'],
        slug=data["slug"]
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message": "Категория успешно создана!"}), 201


@product_bp.route('/products', methods=['Post'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        price=data['price'],
        image=data['image'],
        description=data['description'],
        slug=data["slug"]
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Продукт успешно создан!"}), 201


@product_bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category.query.get(category_id)
    if category:
        return jsonify({
            "id": category.id,
            "name": category.name,
            "slug": category.slug

        }), 200
    return jsonify({"message": "Категория не найдена"}), 404


@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "image": product.image,
            "slug": product.slug

        }), 200
    return jsonify({"message": "Продукт не найден"}), 404


@main_bp.route('/', methods=['GET'])
def home():
    return render_template('catalog/home.html')


@category_bp.route('/catalog', methods=['GET'])
def catalog():
    return render_template('catalog/showcase.html')


@about_bp.route("/about")
def about():
    with open('static/about.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        return render_template('catalog/about.html', content=content)


@states_bp.route("/states")
def states():
    return render_template('states/state.html')
