## Migration process

```shell
# Prior to the first migration
docker-compose run --rm server python src/manage.py db init

# Create a new version of the database
docker-compose run --rm server python src/manage.py db migrate

# Upgrade your database to the last version
docker-compose run --rm server python src/manage.py db upgrade
```
