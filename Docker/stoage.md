### Docker filesystem
- /var/lib/docker
    - aufs
    - containers
    - image
    - volumes

### Layered Architecture of a sample image
Layer1 - Base Ubuntu layer
Layer2 - Changes in apt packages
Layer3 - Changes in pip packages
Layer4 - Source Code
Layer5 - Update Entrypoint with flask command
Layer6 - Container Layer - This layer is only until the lifecycle of a container

### Volumes
`docker volume create vol_name` - to create volume for docker container. This will create a new folder under /var/lib/docker/volumes/data_volume
`docker run -v vol_name:/var/lib/mysql mysql` to create a container for mysql with /var/lib/mysql pointing to docker volume to store data this is called a volumne mount
`docker run -v /data/mysql:/var/lib/mysql mysql` to create container for mysql with host volumne /data/mysql to /var/lib/mysql this is called a bind mount.
`docker run --mount type=bind,soruce=/data/mysql,target=/var/lib/mysql mysql` new command to mount volumne with more specifications

### Storage Drivers
- AUFS
- ZFS
- BTRFS
- Device Mapper
- Overlay
- Overlay2

The selection driver depends on the host system OS. The docker will chose the best storage drivers based on the OS.
