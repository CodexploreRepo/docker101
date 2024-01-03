# Docker Images: Name, Tag, Digest

## Introduction

Docker image has the following 3 parts:

- `Name` (required, user-specified at build time)
- `Tag` (optional, user-specified at build time)
- `Digest` (automatically generated at build time)

## Pull an image using `name`

- Use `docker image pull` (or the `docker pull` shorthand).
  - If no tag is provided, Docker Engine uses the `:latest` tag as a default.

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
  - For example, the `debian:bookworm` image shares its layer with the `debian:latest`, which is `e756f3fdd6a3`
  - Pulling the `debian:bookworm` image therefore **only pulls its metadata**, but not its layers, because the layer `e756f3fdd6a3` is already present locally:

```shell
docker image pull debian:bookworm

bookworm: Pulling from library/debian
Digest: sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510
Status: Downloaded newer image for debian:bookworm
docker.io/library/debian:bookworm
```

- To see which images are present locally, use the docker images command:

```shell
docker images

REPOSITORY   TAG        IMAGE ID       CREATED        SIZE
debian       bookworm   4eacea30377a   8 days ago     124MB
debian       latest     4eacea30377a   8 days ago     124MB
```

## Pull an image using `name:tag`

```shell
docker pull golang:1.17.1
```

- An image like `golang:1.17.1` is available for multiple os/arch, example: `windows/amd64`, `linux/amd64`, etc.
- In such cases, docker automatically pulls the appropriate image for the os/arch the pull command is run on.

## Pull an image by digest (immutable identifier) `name@digest`

- A common thing that happens with a `tag` is that it could be reused.
  - For example an image pulled using `golang:latest` today may be completely different from an image pulled in 6 months.
  - Tags that look like version numbers can have the same behavior. There is no guarantee that an image pulled using `golang:1.17.1` today (on say `linux/amd64`) will be the same when pulled 6 months later (again on `linux/amd64`).
  - If you pull an image specifying the **digest**, you have a guarantee that the image you’re using is always the same.
- A `digest` is an id that is automatically created during build time and cannot be changed (**immutable**).
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

- Also can view the image `manifest` to obtain the `digest`
  - The below command returns a JSON response. Look for the digest in the `Descriptor`.

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
