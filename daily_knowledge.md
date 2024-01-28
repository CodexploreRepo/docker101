# Daily Knowledge

## Day 3

### `ENTRYPOINT` vs `CMD`

- `ENTRYPOINT` specifies a command that will always be executed when the container starts.
- The `CMD` specifies arguments that will be fed to the ENTRYPOINT.
  - If entrypoint can be omited, the default entrypoint will be `/bin/sh -c bash`
- Case 1: Only `ENTRYPOINT` in the Dockerfile
  - The container will run the command `echo "Hello Docker"` by default, and if you specify more argument in the `docker run` command, it will receive as well
- Case 2: `ENTRYPOINT` + `CMD`
  - `CMD` to **provide default arguments** to the entrypoint
- Case 3: Only `CMD`, so the default entrypoint will be `/bin/sh -c bash`

```Dockerfile
#============================CASE 1==============================
# FROM python:3.9-slim

ENTRYPOINT ["echo", "Hello Docker"]

# docker run image_name hahaha
# returns: Hello Docker hahaha

#============================CASE 2==============================
FROM python:3.9-slim
ENTRYPOINT ["echo"]
CMD ["Hello Docker"]

# docker run image_name hahaha
# returns: hahaha

#============================CASE 3==============================
# Entrypoint can be omited, the default entrypoint will be /bin/sh -c bash
# We often use this case :)
FROM python:3.9-slim

CMD ["echo", "Hello Docker"]

# docker run image_name
# returns: Hello Docker
```

### Container's Health Check

- The `HEALTHCHECK` instruction specifies a command for Docker to run inside the container to check if your app is healthy
- The health check makes an HTTP call to the `/health` endpoint, which the API provides to test if the app is healthy.
  - Using the `-f` or `--fail` parameter means the `curl` command will pass the status code on to Docker
    - If the request succeeds, it returns the number `0`, which Docker reads as a successful check.
    - If it fails, it returns **a number other than 0**, which means the health check failed.

```YAML
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost"]
  interval: 1m30s
  timeout: 10s
  retries: 3
  start_period: 2m
```

- Specify `test`
  - `CMD`: must be a list of commands `["CMD", "curl", "-f", "http://localhost"]`
  - `CMD-SHELL`: must be a command string `["CMD-SHELL", "curl -f http://localhost || exit 1"]`
- `interval` is the time between checks--in this case five seconds.
- `timeout` is how long the check should be allowed to run before it’s considered a failure.
- `retries` is the number of consecutive failures allowed before the container is flagged as unhealthy.
- `start_period` is the amount of time to wait before triggering the health check, which lets you give your app some startup time before health checks run.

### Dockerfile

#### `apt-get`

- When there are multiple apps needed to install via `apt-get` and require the answer YES, we should place the `-y` flag before `install`
- WORKING: `apt-get -y install curl libpq-dev gcc`
- NOT WORKING: `apt-get install -y curl libpq-dev gcc`, only working if there is 1 app to install `apt-get install -y iputils-ping`

### Image & Container OS information

- `docker manifest inspect` display an image manifest, or manifest list

```shell
docker manifest inspect --verbose golang:1.17.1

# sample output
[
  {
    "Ref": "docker.io/library/golang:1.17.1@sha256:232a180dbcbcfa7250917507f3827d88a9ae89bb1cdd8fe3ac4db7b764ebb25a",
    "Descriptor": {
      "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
      "digest": "sha256:232a180dbcbcfa7250917507f3827d88a9ae89bb1cdd8fe3ac4db7b764ebb25a", # digest
      "size": 1796,
      "platform": {
        "architecture": "amd64",    # arch
        "os": "linux"               # os
      }
    },
```

- Run the docker container in the interactive mode & `cat /etc/os-release`

```shell
docker run -ti mlflow-server:2.9.2 bash
root@c40b84e986bd:/mlflow# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

### Docker Architecture

- Docker uses a **client-server** architecture.
- Docker **client**: talks to the Docker **daemon**, which does the heavy lifting of building, running, and distributing your Docker containers.
  - Another Docker client is Docker **Compose**, that lets you work with applications consisting of a set of containers.

#### Docker Daemon `dockerd`

- The Docker daemon (`dockerd`) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes.
- A daemon can also communicate with other daemons to manage Docker services.

##### Daemon’s socket `/var/run/docker.sock`

- Reference: [var/run/docker.sock](https://www.educative.io/answers/var-run-dockersock)
- By default, a Docker daemon on a Docker platform listens on the `/var/run/docker.sock` Unix socket.
- It is also a tool used to communicate with the Docker daemon from within a container.
  - Note: containers need to **bind mount** the `/var/run/docker.sock` file.

##### Bind mounting the daemon’s socket into the container

- Mounting the Docker daemon socket gives the control of the daemon to the container.
- Note: this process should only be used with trusted containers when necessary.
  - For example: Jenkins in container can bind mount with the daemon's socket, so that the Jenkins container can build the docker images

### Jenkins: setting up Jenkins in Docker to run Docker

- To set up Jenkins in Docker to be able to run Docker (specifically: build, run, and push an image):
  - Step 1: Create a custom Jenkins Docker image from the official `jenkins` image + install Docker CLI
  - Step 2: bind-mount the container to the host system daemon
    - To do this, connect the Docker CLI in the Jenkins container to the Docker daemon on the host machine by bind mounting the **daemon’s socket** into the container with the `-v` flag. When running the image add this argument: `/var/run/docker.sock:/var/run/docker.sock`.

## Day 2

- Retrieve the command history:

```shell
history | grep "docker run"
  725  docker run --name postgres16 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:16.1-alpine
  726  docker run --name postgres16 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:16.1-alpine

```

### Pull an image by digest (immutable identifier) `name@digest`

- A common thing that happens with a `tag` is that it could be reused.
  - For example an image pulled using `golang:latest` today may be completely different from an image pulled in 6 months.
  - Tags that look like version numbers can have the same behavior. There is no guarantee that an image pulled using `golang:1.17.1` today (on say `linux/amd64`) will be the same when pulled 6 months later (again on `linux/amd64`).
  - If you pull an image specifying the **digest**, you have a guarantee that the image you’re using is always the same.
- To know the digest of an image, pull the image first. Let's pull the latest `ubuntu:22.04` image from Docker Hub:

```shell
docker pull ubuntu:22.04

22.04: Pulling from library/ubuntu
125a6e411906: Pull complete
Digest: sha256:26c68657ccce2cb0a31b330cb0be2b5e108d467f641c62e13ab40cbec258c68d # digest
Status: Downloaded newer image for ubuntu:22.04
docker.io/library/ubuntu:22.04
```

- Docker prints the digest of the image after the pull has finished. In the example above, the digest of the image is: `sha256:26c68657ccce2cb0a31b330cb0be2b5e108d467f641c62e13ab40cbec258c68d`
- Pull an image by a digest

```shell
docker pull ubuntu@sha256:26c68657ccce2cb0a31b330cb0be2b5e108d467f641c62e13ab40cbec258c68d
```

- Digest can also be used in the `FROM` of a **Dockerfile**, for example:

```Dockerfile
FROM ubuntu@sha256:26c68657ccce2cb0a31b330cb0be2b5e108d467f641c62e13ab40cbec258c68d
```

### Docker Image Layers

```shell
docker image pull debian

Using default tag: latest
latest: Pulling from library/debian
e756f3fdd6a3: Pull complete # image layer
Digest: sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510
Status: Downloaded newer image for debian:latest
docker.io/library/debian:latest
```

- Docker images can consist of multiple layers.
  - In the example above, the image consists of a single layer: `e756f3fdd6a3`.
- Layers can be reused by images.
  - For example, the debian:bookworm image shares its layer with the `debian:latest`, which is `e756f3fdd6a3`
  - Pulling the `debian:bookworm` image therefore **only pulls its metadata**, but not its layers, because the layer `e756f3fdd6a3` is already present locally:

```shell
docker image pull debian:bookworm

bookworm: Pulling from library/debian
Digest: sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510
Status: Downloaded newer image for debian:bookworm
docker.io/library/debian:bookworm
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
