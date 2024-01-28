# Supporting Reliability with Health Checks

## Introduction

- Docker monitors the health of your app at a basic level every time you run a container.
- The `HEALTHCHECK` instruction specifies a command for Docker to run inside the container to check if your app is healthy
- The health check makes an HTTP call to the `/health` endpoint, which the API provides to test if the app is healthy.
  - Using the `-f` or `--fail` parameter means the `curl` command will pass the status code on to Docker
    - If the request succeeds, it returns the number `0`, which Docker reads as a successful check.
    - If it fails, it returns **a number other than 0**, which means the health check failed.
- Example 1: `HEALTHCHECK` instruction in Dockerfile

```Dockerfile
 FROM python3.9

 HEALTHCHECK CMD curl --fail http://localhost/health

 WORKDIR /app
 COPY --from=builder /out/ .
```

- Example 2: `HEALTHCHECK` instruction in `docker-compose`

```YAML
version: "3.8"
services:

  mlflow:
    restart: always
    build:
      context: mlflow/
      args:
        MLFLOW_VERSION: ${MLFLOW_VERSION}
    image: haquan/mlflow_server:${MLFLOW_VERSION}
    container_name: mlflow_server_container
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 10s
      timeout: 10s
      retries: 5
      start_period: 10s

```
