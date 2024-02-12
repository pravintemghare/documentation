### Command
- CMD = command in docker image will run the command specified while starting the docker container
- CMD sleep 10 OR CMD ['sleep', '10']

### Entry Point
- ENTRYPOINT = will also run command while starting a container, it will take instruction from the command line, will get appended to entry point
- ENTRYPOINT ['sleep']
- CMD can be used to pass the instruction to the ENTRYPOINT