# Docker Architecture

## Introduction

- Docker uses a **client-server** architecture.
- Docker **client**: talks to the Docker **daemon**, which does the heavy lifting of building, running, and distributing your Docker containers.
  - Another Docker client is Docker **Compose**, that lets you work with applications consisting of a set of containers.
- The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon.
- The Docker client and daemon communicate using a REST API, over **UNIX sockets** or a network interface.

<p align="center"><img width=400 src="../assets/img/docker-architecture.png"/></p>

### Docker Desktop

- Docker Desktop is an easy-to-install application
- Docker Desktop includes the Docker daemon (`dockerd`), the Docker client (`docker`), Docker Compose, Docker Content Trust, Kubernetes, and Credential Helper.

### Docker Daemon `dockerd`

- The Docker daemon (`dockerd`) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes.
- A daemon can also communicate with other daemons to manage Docker services.

### Docker Client

#### `docker`

- The Docker client (`docker`) is the primary way that many Docker users interact with Docker.
- When you use commands such as `docker run`, the client sends these commands to `dockerd`, which carries them out.
- The `docker` command uses the Docker API.
- Note: The Docker client can communicate with more than one daemon.

#### `docker compose`
