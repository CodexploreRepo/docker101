# Docker Compose

## Build Args and Run Args

### Build Args

- To provide the **build args** from `docker-compose` to `Dockerfile`

  - In the docker-compose file, the build args is provided under `build` &#8594; `args`

  ```yaml
  version: "3.8"

  services:
  mlflow:
    build:
    # Dockerfile is stored in "mlflow" folder
    context: mlflow/
    args:
      MLFLOW_VERSION: ${MLFLOW_VERSION} # will read from .env file
  ```

  - In the Dockerfile, the build args neeed to be defined using `ARG` and can be used subsquently

  ```Dockerfile
  # define the build arg
  ARG MLFLOW_VERSION
  # use the build arg via ${}
  RUN pip install --no-cache-dir mlflow==${MLFLOW_VERSION}
  ```

### Run Args

- In order to pass the run arg to the python script, for example `ingestion.py`

```Python
# ingestion.py
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--table", help="Table name to write/update")
    parser.add_argument("-u", "--url", help="URL data source")

# Run the script locally: python ingestion.py -t yellow_taxi -u www.kaggle.com
```

- In the Dockerfile, we use `ENTRYPOINT` to define the script running command

```Dockerfile
ENTRYPOINT [ "python", "ingestion.py"]
```

- The `run args` will be passed either
  - docker run: `docker run sql_ingestion -t yellow_taxi -u www.kaggle.com`
  - docker compose: you can specify it in `command` tag

```yaml
version: "3.8"
services:
  sql_ingestor:
    build:
      context: .
    image: sql_ingestion
    container_name: sql_ingestion_cont
    env_file: .env
    command: -t yellow_taxi -u www.kaggle.com # add here
```

## Environment Variables

- The environment variables can be stored in the `.env` file, placed the same folder as `docker-compose` file and can be injected to the docker container either via `env_file` (Method 1) or `environments` tag (Method 2)

```yaml
version: "3.8"
services:
  nytaxi_db:
    restart: always
    image: postgres:latest
    container_name: nytaxi_db_cont
    # Method 1: no need to specify each environ variable
    env_file: .env
    # Method 2:
    environment:
      POSTGRES_USER: ${DB_USERNAME}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
```
