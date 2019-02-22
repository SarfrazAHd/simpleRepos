# Basic Commands for docker 


you can the get  description of  all commands by typing - " Docker --help "

 # it will  tell you the description of docker version

>> 1 -	 docker -v or docker --version    					



#  Description about docker engine 

>> 	docker version 								



# Login to Docker hub repository

>> 	docker login 								


#  it will run local image present in your docker system

>> 	docker run  " image id "						


# List out the all presented image in our system. 

>> 	docker image ls  or    docker image -a    				



# It will return you only image id of every image
>>  	docker image -q								


# ps for process- it will return  only Running 	containers

>>   docker ps 								



#  it will list out all container both running and non-running.

>>  docker ps -a 								



# this will execute your docker container

>>  	docker exec "container id/name"						



# it will start a  container	

>> docker start  " container id /Name "					



# it will stop a running acontainer		

>>	docker stop" container id /Name "					



# Removing one or more containers
>>	docker rm ''Container id  "						



# Removing one or more docker images

>>	dcocker rmi  " image  id "						

	
  
# It will build your custom image from your dockerfile

>>   dock build  "give name to your image " " location of docker file"	



 # Running a docker images like ubnut or something else
 
 >> 	docker run --name "give name to your cotainer" -it   "images"		



# Exposing port or deploying images the browser

>>	docker run -p 1010 (port) : 80 nginx (image )				



# this commmand will create a docker container

>> 	docker continer create "ur_container_name"				



# this command will execute you docker container in intercative mode	

>>    docker container exec -it "container id/name"				



# it will list out all docker volume

>> 	docker volume  ls  							



# ti will create a docker volume

>>	docker volume create	"Volume name"					



# will delete one volume

>> 	docker volume rm 							



# it will delete the all created volumes

>> docker volume prune							


