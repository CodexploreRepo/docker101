# Docker File

## `ENTRYPOINT` vs `CMD`

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

## Multi-Stage Build

- Stage 1: Build the image to install dependency only
- Stage 2: Copy code & define the logic to run

```Dockerfile
FROM python:3.9-slim AS compile-image

ARG MLFLOW_VERSION

# Define virtual env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN /opt/venv/bin/pip install mlflow==${MLFLOW_VERSION} psycopg2-binary charset-normalizer==2.1.0

FROM python:3.9-alpine AS runtime-image

LABEL maintainer="quandv"
LABEL organization="mlopsvn"

COPY --from=compile-image /opt/venv /opt/venv

WORKDIR /mlflow/

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 5000

# Ref: https://github.com/mlflow/mlflow/issues/6274#issuecomment-1196106372
CMD mlflow server \
    --backend-store-uri ${BACKEND_STORE_URI} \
    --serve-artifacts \
    --host 0.0.0.0 \
    --port 5000
```
