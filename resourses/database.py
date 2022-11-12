from flask_sqlalchemy import SQLAlchemy

import app

db = SQLAlchemy()


class Database(object):

    @staticmethod
    def initialize():
        with app.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.commit()

    @staticmethod
    def insert(instances):
        with app.app.app_context():
            db.session.add_all(instances)
            db.session.commit()

    @staticmethod
    def find_all_products():
        from resourses.models import Product
        with app.app.app_context():
            query = Product.query.all()
        return query

    @staticmethod
    def get_reviews_by_id(ident, page, per_page):
        from resourses.models import Review, Product
        with app.app.app_context():
            reviews = db.session.query(Product.asin, Product.title, Review.review).outerjoin(
                Product, Product.asin == Review.asin).where(
                Product.id == ident).paginate(page=page, per_page=per_page)
        return reviews

    @staticmethod
    def create_review(asin, title, review, product_id):
        from resourses.models import Review
        with app.app.app_context():
            new_review = Review(
                asin=asin,
                title=title,
                review=review,
                product_id=product_id
            )
            db.session.add(new_review)
            db.session.commit()
        return '201 -created'




