# Unilime_project_2.0 - test task for position Python Developer(Flask).

First of all you should up your Docker container. After that you should initialize database and parse files with saveing them using endpoint:

'/initialize'

For with other endpoints use:

'/reviews/int:id' - get request which returns you such data as ASIN, Title and Reviews of perticular product(pagination is 2 elements per page, cached for 60 seconds)

'/review_create/int:id' - put request which allows you to add reviews for products by its ids.
