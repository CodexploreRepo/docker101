# Docker Compose Example

- **Task**: Create Compose definitions to run the to-do web app more reliably in a test, dev, production environment:
- **Reference**:
  - DIAMOL Chapter 7 Lab - Sample Solution
  - Docker’s reference documentation: https://docs.docker.com/compose/compose-file

## Dev environment

This configuration uses Sqlite for data storage and published the web app to port `8020`.

Run from this directory with:

```
docker-compose -f docker-compose-dev.yml up -d
```

## Test environment

- Requirements:
  - The application containers will restart if the machine reboots, or if the Docker engine restarts.
  - The database container will use a bind mount to store files, so you can bring the app down and up again but retain your data.
  - The web application should listen on standard port 80 for test.

```
mkdir -p /data/postgres

docker-compose -f docker-compose-test.yml up -d
```

## Production environment

- This one is automatically refer to `docker-compose.yml`

```
docker-compose up -d
```
