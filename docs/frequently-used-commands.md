# Frequently-Used Commands

## Docker

| Command                                                | Description                                                                                             |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| `docker images`                                        | list down all available images                                                                          |
| `docker ps`                                            | list down all running containers                                                                        |
| `docker ps -a` &#8594; `docker rm <container_name/id>` | list down all containers (even stopped ones) &#8594; using `docker rm` to remove the stopped containers |
| `docker stop <container_name/id>`                      | stop a running container                                                                                |
| `docker start <container_name/id>`                     | to start the stopped container without specify flags or env variables                                   |
| `docker logs <container_name/id>`                      | get the container's log                                                                                 |

## Docker Compose
