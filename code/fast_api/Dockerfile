# take the latest python image
FROM python:latest

# set the working directory
WORKDIR /app

# install dependencies
# --no-cache-dir: The cache, like downloaded whl files, 
# is usually useless in a Docker image, 
# and you can definitely shrink the image size by disabling the cache.
COPY ./requirements.txt /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app

# start the server on port 80 of docker container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]