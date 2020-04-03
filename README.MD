#PayType

Requirement:
- Python
- Django
- PostgreSQL

In PostreSQL:
	create user simple_user with password '1111';
    alter role user_name set client_encoding to 'utf8';
    alter role user_name set default_transaction_isolation to 'read committed';
    alter role user_name set timezone to 'UTC';
    create database paytype owner simple_user;

In terminal:
    pip install psycopg2    