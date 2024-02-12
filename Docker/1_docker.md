Why we need docker

- Compatibility/Dependency
- Long setup time
- Different: Test/Dev/Prod environment


What can it do:
- Containerize application
- Run each service with its own Dependencies in seperate containers

Container:
Container are isolated environment for each application components. As they have there own processes and services, network interface,
mount points just like virtual machines, except they all share the same OS kernel.

Operating Systems:
- OS kernel
- softwares

Docker image is a package
Docker images run docker containers
Docker images can be pushed to docker hub for publicly available

Docker Editions:
    - Community Edition
    - Enterprise Edition

Docker Engine is refered as Docker software installed on a host
- Docker Deamon
- REST API
- Docker CLI

`docker -H=remote-docker-engine:2375 run image_name` - to run docker command from another docker CLI

## Containerization
Docker uses namespace to isolate workspace
- ProcessID
- Network
- Interprocess
- Unix Timesharing
- Mount

To restrict docker container Memory & CPU usage
- `docker run --cpu=.5 image_name`
- `docker run --memory=100m image_name`