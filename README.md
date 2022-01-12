# recipe-app-api
Recipe-app-api using django rest framework
docker-compose up

docker-compose run app sh -c "python manage.py test"
docker-compose run --rm app sh -c "python manage.py test"

docker-compose run --rm app sh -c "python manage.py startapp user"