# Postgres

## Postgres interaction

```Bash
# Create the docker image
$ docker build .
# Run the docker image and connect to it
$ docker run -it <image_id> bash
# Enter to the database
psql postgres://root:root@192.168.208.2:5432/db
```
