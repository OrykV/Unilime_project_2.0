# Unilime_project_2.0 - test task for position Python Developer(Flask).

First of all you should up your Docker container. After that you should initialize database and parse files with saveing them using command:
'docker-compose exec web python manage.py parse_and_save'

Next you should run flask server using command 'docker-compose exec python -m flask run ' for iteraction with endpoints:

'/initialize' - can drop existing database, create new one and insert items in it;

'/reviews/int:id' - get request which returns you such data as ASIN, Title and Reviews of perticular product(pagination is 2 elements per page, cached for 60 seconds);

'/review_create/int:id' - put request which allows you to add reviews for products by its ids.
