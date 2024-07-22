### Docker filesystem
- /var/lib/docker
    - aufs
    - containers
    - image
    - volumes



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
