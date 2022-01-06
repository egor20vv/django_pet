# django_pet

The projects is based on this [tutorial](https://docs.djangoproject.com/en/4.0/intro/) and it is also dockerized.

### Description

Polls is a Django app to conduct Web-based polls. For each question, visitors can choose between a fixed number of answers.

## Before use

To run the application you should to create a file ".env" in the root directory of the project (/path_to_the_project/django_pet/.env) with the next content:

```
SECRET_KEY='YOUR_RANDOM_SECRET_KEY'
```

where YOUR_RANDOM_SECRET_KEY is you're random secret key


## Use Vanilla

To run the server use the next command:

```bash
python manage.py runserver 127.0.0.1:8000
```

To test the polls app use the next command:

```bash
python manage.py test polls.tests
```

## Usage via Docker

### Run server

Just to run the server, it will be enough to use the following command:

```bash
docker-compose up -d base_web web_run
```

### Attach db

But if you start the server for the first time you might need to attach a db to the application and run one of these two commands before.

If you want an empty one, just use the migration:

```bash
docker-compose up -d db_migrate
```

To use the prepared database run the next command:

```bash
docker-compose up -d db_init
```

### Interact with db

To interact with the db, primarily you need to run the server and use the next command:

```bash
docker exec -it django_pet_web_run_1 bash
```

This will create a new Bash session in the container where you can modify the db.
Modifications might be made via [shell](https://docs.djangoproject.com/en/4.0/intro/tutorial02/#playing-with-the-api) 
or [admin page](https://docs.djangoproject.com/en/4.0/intro/tutorial02/#playing-with-the-api) which you can find with this url http://127.0.0.1:8000/admin/
