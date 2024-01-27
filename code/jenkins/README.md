# Jenkins

## Introduction

- Jenkins is a popular continuous integration and delivery (CI/CD) tool. Jenkins is open source and has a great developer community that maintains its existing software and builds plugins to increase its functionality.

## Setting up Jenkins in Docker to run Docker

- Reference: [Jenkins in Docker: Running Docker in a Jenkins Container](https://hackmamba.io/blog/2022/04/running-docker-in-a-jenkins-container/)
- To set up Jenkins in Docker to be able to run Docker (specifically: build, run, and push an image): Create a custom Jenkins Docker image and bind-mount the container to the host system daemon

### Creating a custom Jenkins image with Docker CLI

- Creating a custom Jenkins image from the official `jenkins` image + install Docker CLI

```Dockerfile
FROM jenkins/jenkins:lts
# Install docker CLI
USER root
RUN curl -fsSL https://get.docker.com -o get-docker.sh && /bin/sh get-docker.sh

USER jenkins
```

### Enabling the use of Docker daemon in the Jenkins container

- To do this, connect the Docker CLI in the Jenkins container to the Docker daemon on the host machine by bind mounting the **daemon’s socket** into the container with the `-v` flag. When running the image add this argument: `/var/run/docker.sock:/var/run/docker.sock`.
