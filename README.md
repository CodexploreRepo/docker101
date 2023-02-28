# Docker & Kubernetes 101
## Docker Command
### Container
- Clear container: `docker container rm -f $(docker container ls -aq)`
- Run container: `docker container run -d -p computer_port:docker_port --name container_name link_to_container_at_docker_hub`
  - `-d`, `--detach`: run in the background 
## Docker Compose Command
- Example: [Link](./code/docker_compose_example)
- To start an app (in detach mode): `docker-compose up -d`
  - Start a specific component: `docker-compose up <name_of_component>`  
- To check the log of an app: `docker-compose logs`
- To stop an app: `docker-compose down -v`
  - `-v`: to remove the volumn mounted
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
