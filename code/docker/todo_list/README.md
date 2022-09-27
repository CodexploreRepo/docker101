# Todo Application

## Requirements

- Build your own set of environment definitions for the to-do app. You’re going to put together a development environment and a test environment, and make sure they can both run on the same machine.

The **development environment** should

- Use a local database file
- Publish to port `8089`
- Run `v2` of the to-do application

The **test environment** will need to be run with specific Docker Compose files and a project name. Its setup should

- Use a separate database container
- Use a volume for the database storage
- Publish to port `8080`
- Use the `latest` to-do application image

The main difference is the volume--the database container uses an environment variable called `PGDATA` to set where the data files should be written. You can use that along with a volume specification in your Compose files.

## Dev

```
docker-compose -f ./docker-compose.yml -f ./docker-compose-dev.yml -p todo-dev up -d
```

## Test

```
docker-compose -f .\docker-compose.yml -f .\docker-compose-test.yml -p todo-test up -d
```

> Data persists between `up` and `down` as the database container uses a volume.
