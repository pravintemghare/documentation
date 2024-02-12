### Networking
When we install docker it automatically create three types of network
- bridge (default network)
- none
- host

`docker run --network=host image_name` - to run docker container into a specific network

### Bridge
This is a private network created by docker. It is a by default network assigned to a docker container. Mostly created with ip-address range 172.17.0.0 and assigns an internal ip-address to container
To access the container we need to map a host port to the container to access container application outside

### Host
This network assigns addred associated with the host network. In this we don't need to do port forwarding as the container itself is available with host network ip-address. Limitation we cannot run containers having same port numbers

### None
This is not attached to any network. It works in a isolated network

`docker network create --driver bridge --subnet 182.18.0.0/16 custom-isolated-network` - to create a new network
`docker network ls` - to list the network available

`docker inspect container_id` - to check the network details for a container

### Embedded DNS
All container in a docker host can resolve each other with a name of the container. Using the built-in DNS server