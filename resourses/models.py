from resourses.database import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asin = db.Column(db.String(10), unique=True)
    title = db.Column(db.String(200))
    reviews = db.relationship("Review", back_populates="product", lazy="dynamic")

    def __repr__(self):
        return self.asin + ' ' + self.title


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asin = db.Column(db.String(10))
    title = db.Column(db.String(200))
    review = db.Column(db.String(10000))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship("Product", back_populates="reviews")

    def __repr__(self):
        return f"{self.title} {self.product_id}"