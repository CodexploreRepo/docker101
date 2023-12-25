# Daily Knowledge

## Day 2

- Retrieve the command history:

```shell
history | grep "docker run"
  725  docker run --name postgres16 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:16.1-alpine
  726  docker run --name postgres16 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:16.1-alpine

```

## Day 1

### Postgres

- Access postgres container via exec: `docker exec -it <name_of_container> psql -U root`

  - Note: if access the running container via localhost, so the password is not required
  - `psql` running postgres sql commands
  - `-U root` running as root user

  ```shell
  docker exec -it postgres16 psql -U root
  -------------------------------
  psql (16.1)
  Type "help" for help.

  root: select now();
              now
  -------------------------------
  2023-12-23 14:58:15.391689+00
  (1 row)
  ```

  - Type `\q` to exit the **psql**

### Docker Hub Version

- Syntax: `docker pull <image>:<tag>`
- For example: postgres `docker pull postgres:16.1-alpine`
  - `16.1`: version
  - `alpine`: is a Small. Simple. Secure. Linux

### Secrect Binary File Handling

- Encoding & Decoding the secrect binary file (e.g. private key)
  - Encoding: The output of below command can be stored in the secrect manager, so later we can load into the docker file as the environmental variable

```bash
# encode
# -w 0 option specifies that the output lines should not be wrapped. It means that the base64-encoded output will be in a `single line`, without line breaks.
cat id_rsa | base64 -w 0
```

- Decoding:
  - This is to decode the encoded base64 string into the binary output

```bash
# Decoding
echo $ENCODED_BASE64_STRING | base64 -d > id_rsa.pem
chmod 600 id_rsa.pem # give READ WRITE access to the owner
```

### Dockerfile

- `WORKDIR` to change the working directory inside the docker image
- `COPY`
  - Entire folder: `COPY . /opt/docker101/` copy all the files available in current folder into `/opt/docker101/`

#### `RUN` vs (`ENTRYPOINT` & `CMD`)

- `RUN` to execute the Linux Command before the entrypoint of the Docker container

  - It is possible to combine multiple Linux command in the same `RUN`

    ```Dockerfile
    RUN mv nlp_ver1.zip /opt/docker101/data/model/ && \
        pwd && ls -ltr && \
        unzip /opt/docker101/data/model/nlp_ver1.zip -d /opt/docker101/data/model/ && \
        rm -rf /opt/docker101/data/model/nlp_ver1.zip
    ```

  - For example:
    - `RUN chmod -R 777 /opt/app-root/` applying the read, write, and execute permissions for the owner, group, and others to all files and subdirectories within `/opt/app-root/`
    - `RUN mkdir -p /opt/docker101/` creating the folder

- `ENTRYPOINT` & `CMD` to start the container
  - For example:
    - `ENTRYPOINT ["tail", "-f", "/dev/null"]`
    - `CMD ["/bin/sh", "opt/docker101/scripts/start.sh"]`
    - `CMD exec opt/docker101/scripts/start.sh`

### Docker Compose

- `docker-compose down --volumes` remove the volumes which were set up to store the database.
- View the **log** to inspect what happening when initialising the container

#### Network in Docker Compose

- Compose sets up a single network for your app. Each container for a service joins the default network and is both reachable by other containers on that network, and discoverable by them at a hostname identical to the container name

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres
    ports:
      - "8001:5432"
```

When you run `docker compose up`, the following happens:

1. A network called `myapp_default` is created.
2. A container is created using `web`’s configuration. It joins the network `myapp_default` under the name `web`.
3. A container is created using `db`’s configuration. It joins the network `myapp_default` under the name `db`.

Each container can now look up the hostname `web` or `db` and get back the appropriate container’s IP address.

- For example, `web`’s application code could connect to the URL `postgres://db:5432` and start using the Postgres database.

##### Distinction between `HOST_PORT` and `CONTAINER_PORT`

- For `db`, the `HOST_PORT` is `8001` and the container port is `5432` (postgres default). Networked service-to-service communication uses the `CONTAINER_PORT`. When `HOST_PORT` is defined, the service is accessible outside the swarm as well.

- Within the `web` container, your connection string to `db` would look like `postgres://db:5432`

- From the host machine, the connection string would look like `postgres://{DOCKER_IP}:8001`
  - For example `postgres://localhost:8001` if your container is running locally.

### Postgres

- Error `PostgreSQL Database directory appears to contain a database; Skipping initialization`
  - &#8594; need to proactively remove the volumes which were set up to store the database.
- Error `ERROR:  syntax error at or near "AUTO_INCREMENT"`
  - There is no `auto_increment` in PostgreSQL. Use `serial` instead.
