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

Docker allows solving problems of Build, Ship and Run software in diferent platforms, using the concept of containers, the containers is a way to group processes, this make it more versitile, eficient and more isolated processes of the host machine.


<div id='id2'/>

## Problems of the software development

At the time of working on a software project we can find with many problems, and we can group them in three categories:

- **Build:** Development dependencies, runtime versions, development environment equivalency, produccion environment equivalency and 3rd party providers compatibility.

- **Ship:** Heterogeneous build output, produccion servers access, Native VS Virtualized execution, serverless.

- **Run:** Aplication dependencies, OS compatibility, 3rd party services availability, hardware resources.

this problems are easily solved by docker.

<div id='id3'/>

## Instalation

For windows and mac, we need to download the docker's client, in this link https://www.docker.com/get-started we can find it, for linux is a bit diferent, [here](https://docs.docker.com/engine/install/ubuntu/) can find a tutorial of how install docker in linux (The instalation is for ubuntu).

<div id='id4'/>

## Hello word in Docker :whale:

to run the hello word in docker, we need to execute this command (The docker client must be on).

```
docker run hello-world
```

docker have a client-server arquitecture and use a deamon to comunicate the client with the containers.

<div id='id5'/>

## What is a container?

A container is a fundamental part in docker, the containers are a way to group processes without need a hardware simulations or virtual machines, the containers run natively (only native in linux servers) and this processes only live in the container's context and use only the resources defined for this container.

<div id='id6'/>

## Learn use the containers

### cheat sheet of commands

- **docker ps** => This command list the containers running.
- **docker ps -a** => This command list the all containers.
- **docker ps -aq** => This command list the container's ID.
- **docker inspect Container_ID** => Show the internal details of a container.
- **docker inspect -f '{{}}' Container_ID** => Get the atribute of a internal details of a container, [here](https://docs.docker.com/engine/reference/commandline/inspect/) for more uses of inspect format.
- **docker rm Container_ID** => Stop (if the container is running) and delete the container.
- **docker stop Container_ID** => Stop the container.
- **docker logs Container_ID** => Show the logs of the container.
- **docker container prune** => Delete all the stopped containers.
- **docker rename name1 name2** => Rename the container.
