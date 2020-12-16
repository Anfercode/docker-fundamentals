# Docker Fundamentals :whale:

This repository is intended to show the Docker fundamentals from my point of view.

## Index :file_folder:

1. [What is Docker?](#id1)
2. [Problems of the software development](#id2)
3. [Instalation](#id3)
4. [Hello word in Docker](#id4)
5. [What is a container?](#id5)

<div id='id1'/>

## What is Docker?

Docker allows solving problems of Build, Ship and Run software in different platforms, using the concept of containers, the containers are a way to group processes, this make it more versitile, efficient and more isolated processes of the host machine.

<div id='id2'/>

## Problems of the software development

At the time of working on a software project we can find with many problems, and we can group them in three categories:

- **Build:** Development dependencies, runtime versions, development environment equivalency, produccion environment equivalency and 3rd party providers compatibility.

- **Ship:** Heterogeneous build output, produccion servers access, Native VS Virtualized execution, serverless.

- **Run:** Aplication dependencies, OS compatibility, 3rd party services availability, hardware resources.

this problems are easily solved by docker.

<div id='id3'/>

## Instalation

For windows and mac, we need to download the docker's client, in this link <https://www.docker.com/get-started> we can find it, for linux is a bit diferent, [here](https://docs.docker.com/engine/install/ubuntu/) can find a tutorial of how install docker in linux (The instalation is for ubuntu).

<div id='id4'/>

## Hello word in Docker :whale:

to run the hello word in docker, we need to execute this command (The docker client must be on).

```
docker run hello-world
```

docker have a client-server arquitecture and use a deamon to comunicate the client with the containers.

<div id='id5'/>

## What is a container?

A container is a fundamental part in docker, the containers are a way to group processes without need a hardware simulation or a virtual machine, the containers run natively (only native in linux servers) and these processes only live in the container's context and only use the resources defined for this container.

### Containers life cycle

The containers, when is created, run many processes, but, the container only will run if the main process of the container is running.

<div id='id6'/>

## Learn use the containers

### Cheat sheet of commands

- **docker run [image-name]** => Run a container with the image named.
- **docker run -it [image-name]** => Run a container with the image named in interactive mode.
- **docker ps** => This command list the containers running.
- **docker ps -a** => This command list the all containers.
- **docker ps -aq** => This command list the container's ID.
- **docker inspect [Container_ID]** => Show the internal details of a container.
- **docker inspect -f '{{}}' [Container_ID]** => Get the atribute of a internal details of a container, [here](https://docs.docker.com/engine/reference/commandline/inspect/) for more uses of inspect format.
- **docker rm [Container_ID]** => Stop (if the container is running) and delete the container.
- **docker stop [Container_ID]** => Stop the container.
- **docker logs [Container_ID]** => Show the container logs.
- **docker logs -f [Container_ID]** => Show the container follow up logs.
- **docker container prune** => Delete all the stopped containers.
- **docker rename [name] [new-name]** => Rename the container.
- **docker exec -it [Container_ID] [command]** => Run command in a running container.
- **docker kill [Container_ID]** => Kill the main process of the container, when the main process of the cointainer is killed, the container stop running.
- **docker run -d --name [container-name] -p 8080:00 [image_name]** => the command -p is for redirect the port of the docker container to another port of the host machine.

## Data in docker

### Bind mounts

If you want run a container to manage data, like a database, when you delete the container, the data inside of it will be deleted too, to avoid this exist the Bind mounts, is a way to manage data in docker and we can using adding the command -v, here an example **docker run -d --name [container-name] -v [host-machine-path]:[container-path] [container_img]**, this command make a mount of the container to the host machine, all the changes make in the path of the container or the path of the host machine, they will be listened to each other.

### Volumes

The volumes is the way to persist data in docker, in the last section we the bind mounts to make the forwarding the container path to the host machine path, but if we want to persist data of a database is'nt the good way to do this, because the file system of the host machine can do changes of the file system of the container, this can generate future issues, the good way the manage the volumes this cases is creating a volumes, the volumes are managed by docker and the data is'nt easy accessible, here is the commands we should know to use the volumes:

**docker create volume [volume-name]:** this command create a docker volume.

**docker run -d --name [container-name] --mount src=[volume-name] dst=[container-path]:** this is the good way to run the volume of a container, because we dont need interact to the container file system, this make them more secure to work.

**docker volume ls:** this command show us the all volumes we have.

**docker volume prune:** this command delete all the free volumes.

if we want get a file/path on a container or put data in the container from the host machine, this command help us:

**docker cp [file/path] [container]:[file/path]:** If we want put information on the container

**docker cp [container]:[file/path] [file/path]:** If we want get information on the container

and a extra tip, docker can connect the volumes of a diferent device, like a S3 machine, to the own device, [here](https://docs.docker.com/storage/) is the docker documentation of how to manage data.

## Images

The images are a important component of docker, are the templates of the containers, the images are immutable, that means, the image cannot be changed once the image is built, the images are managed by layers, this layers system is like git, where each layer is a change of the image, when a image is downloaded, docker gets only the changes of this image (if the image exists now in the host machine).

### image cheatsheet

- **docker pull [image:tag]:** download the image of docker hub (if you not specify the tag, docker download the last version of the image :latest).
- **docker push [dockerhub-usr]/[repository:tag]:** push an image to dockerhub.
- **docker tag [repository:tag] [new-repository:tag]:** Rename the tag of an image.
- **docker image ls:** list all images of the host machine.
- **docker image rm -f [image_name]:** Deletes the image of the host machine.
- **docker prune -a:** Deletes all unused images.

### building own images

to build own images, we create a file named `Dockerfile`, this file is the recipe to create new images, the dockerfile, always start with a `FROM` the from is the base image of the custom images, that means, if we want a container runs django, in the dockerfile specify the base image, for example, a ubuntu image, and we add the other tools to have the django image, adding python and other django dependencies, to add the other dependencies in time of build, the command `RUN` runs an especific command, for example `RUN touch file.txt`, will be an example of the Dockerfile in the root of this repository.

Thanks to the Dockerfile, we can see the layers of an image, but in the case of don't have the Dockerfile, exists a command `docker history image`, this command help us to see the layers of an image, but the information can be hard to read with this command, [dive](https://github.com/wagoodman/dive) is a CLI app that help us to see the layers of the images more detailed, to use dive, run the command `dive image-name`.

## Develop with docker

In the folder `example` of this repository we can find a example to how develop a little python app using the `Dockerfile`, clarification, docker always prioritizes the commands that are executed in the `docker run` than those of the `dockerfile` CMD.

## Networking in docker

The networking in docker is the way to connect the containers such as connect the container of the code lives with the container where the database live, the containers of the network don't know there are other containers, They assume they are other machines, docker have three types of networks available in docker.

- **Bridge:** Is the default network a containers gets attached to.
- **Host:** This takes out any network isolation between the docker host and the docker containers, For example, if you were to run a web server on port 5000 in a web-app container attached to the host network, it is automatically accessible on the same port externally, without requiring to publish the port using the -p option.
- **None:** The containers are not attached to any network and does not have access to the external network or other containers. It is isolated from all other networks.

### Network cheatsheet

- **docker network ls:** List all the networks in docker.
- **docker network create --attachable [name]:** create a new network, the command `--attachable` to allow others containers to connect to the network.
- **docker network inspect [network-name]:** show the setting of the network.
- **docker network inspect -f '{{}}' [network-name]:** Get a especific configuration of the network, this using Go templates.
- **docker network connect [network-name] [container-name]:** connect a container to a network.

## Docker compose

All we learn about docker, the container are usefull, but now are a new problem, configurate the conteiners, volumes and networks are so tedius with the things we learn until now, docker compose is a tool can help us to run the containers, create and configurate the volumes and networks with one file `docker-compose.yml`, to see how to use the docker compose, in the folder example can we see it, to run the docker compose file, use the command `docker-compose up`.

### Docker compose cheatsheet

- **docker-compose ps** => Show the all services running.
- **docker-compose up** => Inicialize the services defined in the docker compose file.
- **docker-compose up -d** => Inicialize the services in dettach mode.
- **docker-compose build** => Build the services in the docker compose file.
- **docker-compose up --build** => Build and run the docker compose file.ß
- **docker-compose down** => Down all the services in the docker compose file.
- **docker-compose logs** => Show all the logs of the service in the docker compose file.
- **docker-compose logs -f** => Show the logs in follow mode.
- **docker-compose logs [service-name]** => Show the logs of a specific service.
- **docker-compose logs --tail=[number] [service-name]** => Show the number of last lines of the log.
- **docker-compose exec [service-name] [command]** => Run a command in the specific service.
- **docker-compose run --rm [service-name] [command]** => Run a container of a specific service.
- **docker-compose run --rm --service-ports [service-name] [command]** => Run a container of a specific service exposing the ports.

### Docker compose override

The docker compose override is a docker compose tool that makes development easier, works creating a file named `docker-compose.override.yml` this file works with the same structure of the docker `docker-compose.yml` but all diferences of the diferences will be merged or override, this help us to make changes to docker compose without modify the `docker-compose.yml` file.

## References

This documentation it is based mostly by the [Docker course of platzi](https://platzi.com/cursos/docker/) 💚 💚 💚, but i used complements of other sources to complement the information, next you can see te urls of the complement material:

- [Docker for Python Development?](https://towardsdatascience.com/docker-for-python-development-83ae714468ac).
- [How to Develop Your Python Docker Applications Faster](https://dzone.com/articles/how-to-develop-your-python-docker-applications-fas).
- [Docker 101: Fundamentals & The Dockerfile](https://itnext.io/docker-101-fundamentals-the-dockerfile-b33b59d0f14b).
- [Networking Docker Containers](https://codeburst.io/networking-docker-containers-c4f48339a0df).
- [Getting Network Information from Docker](https://www.baeldung.com/ops/docker-network-information).
- [How to Docker Compose a developer environment: an open source example](https://www.codementor.io/@daniellebrero/how-to-docker-compose-a-developer-environment-an-open-source-example-m1grxv19d).
- [20 Docker commands use cases for developers](https://dev.to/alex_barashkov/20-docker-commands-use-cases-for-developers-2d9g).
- [Making sense of Docker Compose overrides](https://medium.com/it-dead-inside/making-sense-of-docker-compose-overrides-efb757460d64).
- [Docker-compose Override - V2M](https://www.youtube.com/watch?v=TPmbwAgN4ZA&t=0s).
- [CÓMO escribir LOS MEJORES Dockerfiles](https://www.youtube.com/watch?v=QXlQDV9FZhI&t=2s).
- [Demystifying Docker Compose](https://dev.to/geekgalgroks/demystifying-docker-compose-b62).
- [Don't just "docker-compose up"](https://dev.to/kbariotis/dont-just-docker-compose-up-gff).
- [10 docker-compose and docker commands that are useful for active development](https://dev.to/aduranil/10-docker-compose-and-docker-commands-that-are-useful-for-active-development-22f9).
- [How to run docker container with external volumes](https://codebeamer.com/cb/wiki/5713519).

Make with 💚 by Anfercode.