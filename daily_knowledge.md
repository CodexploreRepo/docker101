# Day 1

## Docker-compose

- `docker-compose down --volumes` remove the volumes which were set up to store the database.
- View the **log** to inspect what happening when initialising the container

## Postgres

- Error `PostgreSQL Database directory appears to contain a database; Skipping initialization`
  - &#8594; need to proactively remove the volumes which were set up to store the database.
- Error `ERROR:  syntax error at or near "AUTO_INCREMENT"`
  - There is no `auto_increment` in PostgreSQL. Use `serial` instead.
