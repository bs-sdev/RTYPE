In order to run a MongoDB docker container, first pull the image from the docker hub:
	- docker pull mongo

Then, just run the container with port redirection to your host: 
	- docker run --name some-mongo -p 27017:27017 -d mongo

Now you can access to your container threw this address (on your brower):
	- http://localhost:27017