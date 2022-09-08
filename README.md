# Universium Test



## To build and start the project
```
docker-compose up -d --build
docker-compose up
```

# Contents
To access contents via web pages go to: http://127.0.0.1:8000

Available pages:
* /movies
* /actor_stats
* /actor_stats/<actor_id>


# Shell Contents
To import contents via shell:
```
docker exec -it universium_web_1 bash
python manage.py import_data `command`

Command line data import info:
* to import all data, pass `all` instead of `command`
* to import separate data, pass below content names instead of `command`:
**   actors
**   roles
**   directors
**   directors_genres
**   movies
**   movies_genres
**   movies_directors
* to truncate table contents pass `truncate` instead of `command`"
```