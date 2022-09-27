`kubectl apply -f deployment.yaml`

- Port forward the `8080` port of the Pod to `80` of the container

`kubectl port-forward deploy/ch02-lab 8080:80`

`curl http://localhost:8080`

> "I'm ch02-lab-5789ff74bd-db4pg running on Linux 5.10.104-linuxkit #1 SMP Thu Mar 17 17:08:06 UTC 2022"

`kubectl get pods -o custom-columns=NAME:metadata.name`

> ch02-lab-5789ff74bd-db4pg

`kubectl exec deploy/ch02-lab -- sh -c 'hostname'`

> ch02-lab-5789ff74bd-db4pg
