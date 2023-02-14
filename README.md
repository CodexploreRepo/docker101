# Docker & Kubernetes 101
## Command
### Container
- Clear container: `docker container rm -f $(docker container ls -aq)`
- Run container: `docker container run -d -p computer_port:docker_port --name container_name link_to_container_at_docker_hub`
  - `-d`, `--detach`: run in the background 
## Docker Compose

- Example: [Link](./code/docker_compose_example)

## Docker Topics

### Container Reliability with Health Check & Dependency Check

- Example: [Link](./code/health_dependency_check_example)
- [Running multiple environments with Docker Compose](./code/todo_list/)

### Observability with Prometheus and Grafana

- Example: [Link](./code/prometheus_grafana_example/)

# Kubernetes

## Kubernetes Topic

### Deployment & Services

- Example: [Link](./code/kubernetes/deployment_yaml_example/)
