## How to create a own image Example
- OS - ubuntu
- Update apt repo
- Install dependencies using apt
- Install python dependencies using pip
- Copy Sources Code to /opt/ folder
- Run the web server using flask command

##### DockerFile Example
From Ubuntu

RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/soruce-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run

`Every thing in Caps are instructions to the docker image creation`

#### To build docker image

- docker build -t image_name:tag_name DockerFile
- docker push image_name:tag_name  -- Push to docker repository

### Layered Architecture 
- Every instruction passed to the docker file is a layer in that docker image
- `docker history image_name` - To view size of each layer in the docker image


### Failure
- All the layers are cached by when running a docker build command
- If any steps fails, when re-run it will take it from the cache and start building from the failure stage

### Environment Variables
- `docker run -e ENV_VARIABLE=Value image_name` - To run docker image with variable name
- We can get details of environment variables given in docker inspect command under Congfig section.
