from flask import Flask, request, jsonify, Response
from flask_caching import Cache
from resourses.parser import Parser
from resourses.database import db, Database


app = Flask(__name__)

app.config.from_object("config.Config")
db.init_app(app)
cache = Cache(app)


@app.get('/initialize')
def initialize():
    Database.initialize()
    Parser.save_products()
    Parser.save_reviews()
    return Response(status=200)


@app.get('/reviews/<int:id>')
@cache.cached(timeout=60)
def get_reviews_by_id(id):
    data = []
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 2, type=int)
    reviews = Database.get_reviews_by_id(id, page, per_page)
    for r in reviews:
        data.append({
            'asin': r.asin,
            'title': r.title,
            'review': r.review,
        })

    meta = {
        'page': reviews.page,
        'pages': reviews.pages,
        'total_count': reviews.total,
        'prev_page': reviews.prev_num,
        'next_page': reviews.next_num,
        'has_next': reviews.has_next,
        'has_prev': reviews.has_prev,
    }
    return jsonify({'data': data, "meta": meta})


@app.put('/review_create/<int:product_id>')
def review_create(product_id):
    ids = {}
    request_data = request.get_json()
    products = Database.find_all_products()
    for product in products:
        ids[product.asin] = product.id
    for item in ids.items():
        if item[1] == product_id:
            asin = item[0]
    Database.create_review(asin, request_data['Title'], request_data['Review'], product_id)
    return Response(status=201)


if __name__ == '__main__':
    app.run()
