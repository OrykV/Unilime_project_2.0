from flask.cli import FlaskGroup

from app import app
from resourses.database import Database
from resourses.parser import Parser
cli = FlaskGroup(app)


@cli.command("parse_and_save")
def parse_and_save():
    Database.initialize()
    Parser.save_products()
    Parser.save_reviews()


if __name__ == "__main__":
    cli()
