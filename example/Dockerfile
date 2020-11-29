## Base image to work, is good practice use the tag alpine
## alpine is a linux distro optimazed for containers.
FROM python:3.8-alpine

## Go to the work path in the container, is like command cd
WORKDIR /usr/src

## Copy requirements.txt of the host machine path to the container path,
## if we want specify the paths use COPY ['.', "/usr/src"],
## we first we copy the requirments.txt we make sure image not be rebuild
## if the code or something else change.
COPY requirements.txt .

## Run the command of the moment of build the container,
## in this case the command is to get the dependencies
## of the proyect
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip3.8 install -r requirements.txt

## Copy all the other files to the container, docker verify if the requirements.txt
## Changed or not, if change docker copy the file to the container.
COPY . .

## Set the environment variables for the container, in the run of the CMD
## will be used, this is bad practice, this is for practical purposes.
ENV port=8080
ENV host=0.0.0.0

## Make bindable the port to the host machine, don't expose the port
EXPOSE 8080

## The CMD is the command to run by default when the container start
CMD ["python3.8", "app.py"]