# Base project to develop an API with Flask and Swagger

## Requirements:

1. Docker and docker-compose

## Instructions:

This project has been created to have a basic point to start creating an API with Flask, SqlAlchemy and Alembic to handle the migrations.

    ### Setting up the environment

We could set the following environment variables:

1. **DB_URI**: This variable is used to configured the variable **SQLALCHEMY_DATABASE_URI** used by SqlAlchemy to interact with the database. It currently is only supported the engines SQLite and MySQL.

2. **DEBUG**: This variable is set to True by default. To handle a local environment.