from flask.cli import FlaskGroup

from app import app
from resourses.database import Database
from resourses.parser import Parser
cli = FlaskGroup(app)

""" This command is created in order to drop tables if they exists and create new ones. 
    Parse necessary data such as products and reviews and save them to database.
    You should start working with app with it.
"""


@cli.command("parse_and_save")
def parse_and_save():
    Database.initialize()
    Parser.save_products()
    Parser.save_reviews()


if __name__ == "__main__":
    cli()
