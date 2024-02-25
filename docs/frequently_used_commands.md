# Frequently-Used Commands

## Docker

### `docker image`

| Command                                                                                                      | Description                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docker images`                                                                                              | list down all available images                                                                                                                                            |
| `docker build -t <your_docker_hub_id>/mlflow-server:2.9.2 -f Dockerfile . --build-arg MLFLOW_VERSION=2.9.2 ` | - `your_docker_hub_id` to push to docker hub if required<br>- `.` means current folder<br>- `--build-arg` is the pass the arg as define in Dockerfile`ARG MLFLOW_VERSION` |
| `docker inspect <image_name>`                                                                                | to display detailed information on an image                                                                                                                               |
| `docker tag source_image new_image_name`                                                                     | to replicate the image                                                                                                                                                    |
| `docker rmi <image_name`                                                                                     | to remove the image                                                                                                                                                       |

- [Dive](https://github.com/wagoodman/dive) to inspect layers

### `docker container`

| Command                                                                                                                                            | Description                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docker ps`                                                                                                                                        | :star: list down all running containers                                                                                                                                                                                         |
| `docker ps -a` &#8594; `docker rm <container_name/id>`                                                                                             | list down all containers (even stopped ones) &#8594; using `docker rm` to remove the stopped containers                                                                                                                         |
|                                                                                                                                                    |                                                                                                                                                                                                                                 |
| `docker stop <container_name/id>`                                                                                                                  | stop a running container                                                                                                                                                                                                        |
| `docker rm <container_name/id>` or `docker remove <container_name/id>`                                                                             | to remove all stopped container                                                                                                                                                                                                 |
| `docker start <container_name/id>`                                                                                                                 | to start the stopped container without specify flags or env variables if the container is still in `docker ps -a`                                                                                                               |
| Run Container                                                                                                                                      |                                                                                                                                                                                                                                 |
| `docker run --help`                                                                                                                                | to read the document of docker run                                                                                                                                                                                              |
| `docker run -d -p 5002:5000 --name mlflow mlflow-server:2.9.2`                                                                                     | - `-d` detach mode<br>- `p 5002:5000` port forward the local port 5000 to 5002 (client outside will access via port 5002, and it will be mapped to the port 5000 inside docker)<br>- `--name` to set the name for the container |
| `docker run -v /host/path:/container/path --name container_name image_name`                                                                        | Usage case: many containers mount to the same data location in a local PC, so that it can share the same data                                                                                                                   |
| Debug Running Container                                                                                                                            |                                                                                                                                                                                                                                 |
| `docker logs <container_name/id>`                                                                                                                  | :star: get the container's running log                                                                                                                                                                                          |
| `docker inspect <container_name/id>`<br>Format output & specific type: `docker inspect --format '{{json .State.Health }}' mlflow_server_container` | :star: return low-level information on Docker objects (include the health check logs)                                                                                                                                           |
| `docker run -ti <image_name> bash`                                                                                                                 | run the image in the interactive mode and access with `bash` shell                                                                                                                                                              |
| `docker exec -it <container_name> /bin/sh`<br>`docker exec -it <container_name> bash`                                                              | :star: directly go in the running container with `sh` shell or `bash` shell                                                                                                                                                     |
| `ctop` to install `brew instal ctop`                                                                                                               | :star: top-like interface for container metrics - to view the memory usage of the container                                                                                                                                     |
| File Moving                                                                                                                                        |                                                                                                                                                                                                                                 |
| `docker cp mlflow_container:/mlflow/hehe.txt .`                                                                                                    | move the file `/mlflow/hehe.txt` in the mlflow_container to the host PC                                                                                                                                                         |
| `docker cp hehe.txt mlflow_container:/mlflow/haha.txt`                                                                                             | copy `hehe.txt` file from the host PC to the mlflow_container and rename as `haha.txt`                                                                                                                                          |
| Clear Up                                                                                                                                           |                                                                                                                                                                                                                                 |
| `docker system prune`                                                                                                                              | remove all unused containers, networks, images (both dangling and unused), and optionally, volumes.                                                                                                                             |

### Detailed Command Usage

#### `docker ps`

- `docker ps -a | awk 'NR>1 {print $1}'` to list down all the container_id
  - `NR>1` number of row > 1, to ignore the first row, which is CONTAINER_ID
  - `{print $1}` to select only the first column
- :star: `docker ps -a | awk 'NR>1 {print $1}' | xargs docker stop` to stop all the containers

#### `docker inspect`

- `docker inspect`

  - inspect image

  ```shell
  "Labels": {
                "maintainer": "quandv",
                "organization": "mlopsvn"
            }

  "Env": [
                  "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                  "LANG=C.UTF-8",
                  "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
                  "PYTHON_VERSION=3.9.18",
                  "PYTHON_PIP_VERSION=23.0.1",
                  "PYTHON_SETUPTOOLS_VERSION=58.1.0",
                  "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/4cfa4081d27285bda1220a62a5ebf5b4bd749cdb/public/get-pip.py",
                  "PYTHON_GET_PIP_SHA256=9cc01665956d22b3bf057ae8287b035827bfd895da235bcea200ab3b811790b6"
              ],
    "Cmd": [
                  "/bin/sh",
                  "-c",
                  "mlflow server     --backend-store-uri ${BACKEND_STORE_URI}     --serve-artifacts     --host 0.0.0.0     --port 5000"
            ],
  ```

  - inspect container

  ```shell
  docker inspect mlflow
  [
      {
          "Id": "92d0a7cefcbba23435580e4c1c31ca60e67331386e353dacfed8cf7496c96512",
          "Created": "2024-01-28T09:20:16.42030951Z",
          "Path": "/bin/sh",
          "Args": [
              "-c",
              "mlflow server     --backend-store-uri ${BACKEND_STORE_URI}     --serve-artifacts     --host 0.0.0.0     --port 5000"
          ],
          "State": {
              "Status": "running",
              "Running": true,
              ...
              "Health": {
                  "Status": "unhealthy",
                  "FailingStreak": 9,
                  "Log": [
                      {
                          "Start": "2024-01-28T09:22:53.999886972Z",
                          "End": "2024-01-28T09:22:54.038575264Z",
                          "ExitCode": -1,
                          "Output": "OCI runtime exec failed: exec failed: unable to start container process: exec: \"curl\": executable file not found in $PATH: unknown"
                      },
  ```

#### `docker manifest`

- `docker manifest` manage Docker image manifests and manifest lists
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

#### `docker exec`

- `docker exec` runs a new command in a running container.
  - `-it` `--interactive` and `--tty`
- Start an new shell session: `docker exec -it <container_name> /bin/sh`

  - For example:

  ```Shell
  docker exec -it postgres16 /bin/sh
  # inside the "postgres16" container, we can use createdb cmd to create a new database called simplebank
  /  createdb --username=root --owner=root simple_bank
  # login to simplebank db via "psql" command inside the container
  /  psql simple_bank
  psql (16.1)
  Type "help" for help.

  simple_bank= \q  # \q to exit psql terminal

  /  dropdb simple_bank
  /  exit
  ```

  - To get the os information of the image

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

- Access other application's CLI via exec:
  - Ex1 `docker exec -it <name_of_container> psql -U root` this is to open the postgres CLI via `psql` command
  - Ex2 `docker exec -it postgres16 createdb --username=root --owner=root simple_bank` this is to create a new db called `simple_bank` via `createdb` command

## Docker Compose

- To start all services: `docker compose up -d`
- To start one service: `docker compose up -d service_a`
- To re-build the images: `docker compose build`
- To get the log available: `docker compose logs`
