## Networking in Kubernetes

- Node Ip-address
- Ip-address is assigned to a pod
- Kubernetes cluster creates it private network with 10.244.0.0

## Cluster Networking
- We need to configure networking
- All containers/PODs can communicate to one another without NAT
- All nodes can communicate with all containers and vice-versa without NAT

## Software to configure networking
- Cisco
- VMware NSX
- Cilium
- Flannel
