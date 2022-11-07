import csv
from resourses.models import Product, Review
from resourses.database import Database


def parse_products():
    products = []
    with open('Products.csv', mode='r') as csv_file:
        products_list = csv.DictReader(csv_file)
        for row in products_list:
            product = Product(asin=row['Asin'], title=row['Title'])
            products.append(product)
    return products


def parse_reviews():
    reviews = []
    with open('Reviews .csv', mode='r') as csv_file:
        reviews_list = csv.DictReader(csv_file)
        for row in reviews_list:
            review = Review(asin=row['Asin'], title=row['Title'], review=row['Review'])
            reviews.append(review)
    return reviews


def save_products():
    products = parse_products()
    Database.initialize()
    Database.insert(products)


def save_reviews():
    ids = {}
    reviews = parse_reviews()
    products = Database.find_all_products()
    for product in products:
        ids[product.asin] = product.id
    for review in reviews:
        if review.asin in ids:
            review.product_id = ids.get(review.asin)
    Database.insert(reviews)
