# Health and Dependency Check for Docker Container

## Requirements

Some applications use resources consistently, so that the initial dependency check and the ongoing health check are testing the same thing. That’s the case with this lab. It’s an app that simulates a memory hog--it just keeps allocating and holding on to more memory as long as its running. It’s a Node.js app and it needs some checks:

- At startup it should check that there’s enough memory for it to work; if not, it should exit.
- During runtime it should check every 5 seconds to see if it has allocated more memory than it is allowed; if it has, it needs to flag that it’s unhealthy.
- The test logic is already written in the `memory-check.js` script. It just needs to be wired into the **Dockerfile**.

## Usage

You can build the solution from my Dockerfile:

```
docker image build -t diamol/ch08-lab:solution .
```

And run the container interactively; the app will print out its (fake) memory allocations:

```
docker container run diamol/ch08-lab:solution
```

> Check the container list after a while to see the health, and inspect the container to see the health check output

## Dependency check

At startup the container should run the `memory-check.js` script to see there's enough memory for the app to run. If there is then the app can start, if not the container should exit.

You can do this in a cross-platform way in the `CMD` instruction:

```
CMD node memory-check.js && \
    node memory-hog.js
```

## Health check

At five-second intervals the same `memory-check.js` script can be run in a health check to ensure the app hasn't breached its memory limit:

```
HEALTHCHECK --interval=5s \
 CMD node memory-check.js
```
