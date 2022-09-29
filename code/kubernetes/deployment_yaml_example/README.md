# Single Deployment Example

`kubectl apply -f deployment.yaml`

- Port forward the `8080` port of the Pod to `80` of the container

`kubectl port-forward deploy/ch02-lab 8080:80`

`curl http://localhost:8080`

> "I'm ch02-lab-5789ff74bd-db4pg running on Linux 5.10.104-linuxkit #1 SMP Thu Mar 17 17:08:06 UTC 2022"

`kubectl get pods -o custom-columns=NAME:metadata.name`

> ch02-lab-5789ff74bd-db4pg

`kubectl exec deploy/ch02-lab -- sh -c 'hostname'`

> ch02-lab-5789ff74bd-db4pg

# Multiple Deployment Example
```Shell
kubectl apply -f deployments.yaml

kubectl get pods
```
> There are two versions of the web app

[services.yaml](./services.yaml) defines a ClusterIP service for the API and a LoadBalancer service for the web app. The selector for the web service uses two labels to ensure only the v2 pod is included.

```
kubectl apply -f solution/services.yaml
```

> http://localhost:8088

![](./solution/numbers-web-v2.png)
