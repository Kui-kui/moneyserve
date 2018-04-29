## Installation

```
git clone git@github.com:Kui-kui/moneyserve.git && cd moneyserve
docker-compose run --rm server pip install -r requirements.txt --user --upgrade
docker-compose up -d server
```

## Accessing containers

Require Docker >= 1.3

```shell
# use 'docker ps' to see the list of your containers
docker exec -it moneyserve_db_1 psql -Upostgres
docker exec -it fmoneyserve_server_1 bash
```
