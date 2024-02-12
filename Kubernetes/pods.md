### Pods
- Containers are encaplusted in a pod in kubernetes
- A smallest unit in kubernetes cluster
- A pod can run multiple docker containers
- Create new pod for each docker container
- To scale up we deploy pod & to scale down we remove pods
- We can deploy helper container along with main container in a pod

`kubectl run image --image image_name` - Creates a pod and deploy a container image
`kubectl get pods` - to list pods in the cluster
`kubectl get pods -o wide` - to list pods in the cluster with more details
`kubectl delete pods image` to delete pods in the cluster
`kubectl describe pods image` - to get details of the running pod
`kubectl create -f filename.yaml` to create resources in K8s cluster
`kubectl replace -f filename.yaml` to update the resources in K8s cluster
`kubectl scale --replicas=6 -f filename.yaml` to update replica set to scale up
`kubectl scale --replicas=6 replicaset replicaset_name` to update replica set to scale up