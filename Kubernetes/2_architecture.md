### Main Architecture
- Worker Nodes (Minions)  
- Master Nodes

Cluster is a set of nodes 
Master watches the nodes and is responsible for managing the whole cluster


### Components of K8s
- API server - frontend for k8s
- etcd - key-value store used by k8s data to manage the cluster (multiple nodes & master)
- controller - are the brain behind orchestration. notice and respond when a node goes down
- schedulers - to deploy new containers to cluster on nodes
- kubelet - agent which run on each node in the cluster
- container runtime - software use to run containers (docker)

### Work Nodes 
- Container runtime (docker)
- kubelet

### Master Node
- API Server
- etcd
- Controller
- Scheduler

`kubectl` - command line utility to interact with the K8s cluster

`kubectl run hello-minikube` - to run application in a cluster
`kubectl cluster-info` - to list info of the cluster
`kubectl get nodes` - to get worker node details
`kubectl get all` - to get all deployed resources in a cluster

https://github.com/dockersamples/example-voting-app/tree/main/k8s-specifications