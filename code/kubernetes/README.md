# Kubernetes

# `kubectl` commands

- You can add an alias of `kubectl` as `k` for shorter command in `.bashrc` file.

#### Command Flag

- `-A` means All
- `-o`, `--output`: output from the commands

#### `kubectl describe`

- `k describe` to list down everything is running
  - `k describe pods -A -l app=sleep-1 | grep Image: | sort | uniq -c | sort -nr` to grep running image, where:
    - `-l` is label of the pod, in this case the label is `app=sleep-1`
    - `uniq -c` to get the unique image & the count of the number of times each image being used

#### `kubectl get`

##### `svc` service

- `kubectl get svc <name-of-the-service` check the Service details

##### Output Format

###### JSON Output Format

- Syntax: `jsonpath='{.items[*].}'`

```Shell
# Get the Pod name of the Pod with label: app=sleep-1
k get pods -A -l app=sleep-1 -o jsonpath='{.items[*].metadata.name}'

# Check the Pod with label: app=sleep-2’s IP address:
k get pod -l app=sleep-2 --output jsonpath='{.items[0].status.podIP}'
```

###### Column Output Format

- Syntax: `custom-columns=COLUMN1_NAME:metadata.name,COLUMN2_NAME:metadata.labels`

```Shell
# list all Pods, showing the Pod name and labels:
kubectl get pods -o custom-columns=NAME:metadata.name,LABELS:metadata.labels
```
