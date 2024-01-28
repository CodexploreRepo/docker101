# Frequently-Used Commands

## Docker

### `docker image`

| Command         | Description                    |
| --------------- | ------------------------------ |
| `docker images` | list down all available images |

### `docker container`

| Command                                                | Description                                                                                                       |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `docker ps`                                            | :star: list down all running containers                                                                           |
| `docker ps -a` &#8594; `docker rm <container_name/id>` | list down all containers (even stopped ones) &#8594; using `docker rm` to remove the stopped containers           |
|                                                        |                                                                                                                   |
| `docker stop <container_name/id>`                      | stop a running container                                                                                          |
| `docker start <container_name/id>`                     | to start the stopped container without specify flags or env variables if the container is still in `docker ps -a` |
| `docker logs <container_name/id>`                      | get the container's log                                                                                           |
| `docker exec -it <container_name> /bin/sh`             | access Linux Shell                                                                                                |

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
    .
    .
    .

```

### `docker exec`

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

- Access other application's CLI via exec:
  - Ex1: `docker exec -it <name_of_container> psql -U root` this is to open the postgres CLI via `psql` command
  - Ex2: `docker exec -it postgres16 createdb --username=root --owner=root simple_bank` this is to create a new db called `simple_bank` via `createdb` command

## Docker Compose
