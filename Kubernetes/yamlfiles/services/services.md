## Services:
- Enable communication within and outside of the application
- Helps communication between frontend user, backend application and external sources
- Pods don't have a persistent ip-address. Services helps solve the issue and assign a static ip-address to reach pods
- Default type is ClusterIP
- NodePort & LoadBalancer works similar in virtual architecture or minikube. LoadBalancer are only configured in Cloud like AWS, Azure 

## Type of services:
- NodePort - Enables pod to be accessible on the Node 
- ClusterIp - Create a VIP within the cluster
- Loadbalancer - Creates a loadbalancer to distribute load


## NodePort
- Port on the pod - Target port
- Service(cluster ip of the service) - Port
- Nodde port (30000-32767)
 