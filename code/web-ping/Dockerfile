# Base Image
FROM diamol/node

# Multiple environment variables,
ENV TARGET="blog.sixeyed.com" \
    METHOD="HEAD" \ 
    INTERVAL="3000" 
# Creates a directory in the container image filesystem
# and sets that to be the current working directory. 
WORKDIR /web-ping

#Copies files or directories from the local filesystem into the container image. 
# The syntax is [source path] [target path]
COPY app.js .

# Specifies the command to run when Docker starts a container from the image.
CMD ["node", "/web-ping/app.js"]