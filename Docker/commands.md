`docker run image_name` - to start a docker container- images is pulled from local or ducker hub
`docker ps` - to list the containers running
`docker ps -a` - to list all containers running & stopped
`docker stop container_id/name` - to stop running container
`docker rm` - to remove a stopped container
`docker images` - to list images
`docker rmi image_name` - to remove a docker image (must stop & delete running or stopped container)
`docker pull image_name` - to just download the docker image
`docker exec` - to execute command in a docker container
`docker run -d image_name` - to run docker container in detached mode
`docker attach container_id/name` - to attach a running container

`docker rum image_name:tag_name` - by default if tag_name not provided the latest tag is taken.
`docker run -i image_name` - for interactive run docker container
`docker run -t image_name` - will attach docker container terminal 
`docker run -itd -p 8080:80 image_name` - run a docker container with host port 8080 & docker port 80.

We cannot map 2 same host port for 2 docker containers.

`docker run -v /opt/datadir:/var/lib/mysql` - run a docker container with volume attached to host. host volume: /opt/datadir & docker volume /var/lib/mysql
`docker inspect container_id/name` - to get all details of a docker container in json format
`docker logs container_id/name` - to view logs for a docker container