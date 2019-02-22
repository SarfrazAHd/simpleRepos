					



 Docker   is  an   OS-level   virtualiztion    platform  that  provide  to a doverloper or an IT  administrator  to  run and ship  			their application into  a container with all their dependency and library files.







# Docker Components





# Docker Engine 	 	  

Docker client and server communicate  to each other  Using   REST Api   and this  whole  system known  as 				Docker engine or docker daemon as well.  





# DockerFiles    	 	    

Docker  files are basic instruction written in text foramt to creat an image  





# Docker Image	  	

Docker image  are templates come in use to create Docker container 



# Docker repository	

Where the docker all   docker images place.





# Docker Container	

Docker container are set of executabale package that contain all library and dependency for a particular
application to running efficiently in different-different  environmenet.
And this is also known as, - Docker containers are running instance of docker image	 





# Docker Compose 		  

Docker-compose is a tool for defininng and running multi containe docker application.




# Docker volume		

Docker  voulme  preferred   as  mechanism  to  persist data  generated  and used by a container.




# Docker Swarm 	 	   

Docker swarm is a , clustering and scheduling tool  for docker container.  





# Downloading docker in ubuntu



 # step1  :    Updtae your system first

            >> sudo apt-get update



  # step2 :   Install docker by typing these commands -

            >> apt install docker.io                          
		


  # step3 :  After this Command check the download done or not
           
            >> ubuntu@ip-172-31-42-184:~$ docker --version
    
	    >> Docker version 17.03.2-ce, build f5ec1e2                          
	      
  
  
  and you are done !! Congrats docker has been succesfully installed in your system




				
					


# Working with DockerFile


Creating a docker file , Keywords::



# FROM       	 	   
Specfify image name




# MAINTAINER 		
Optional   Your name and   " < emailid@gmail.com > "



# CMD		

Command you want execute on your terminal After pulling the image.  



# RUN 

Command you want to Run at time of running this image.

and many more Keywords ..




# Building image from Dockerfile

	>>  docker  build  -t ''image name in lowercase" : "Tage" and  '' location of  Dockerfile"       		
			
	# -t for specifying Tag 



# linking Wordpress and Mysql


	>>   docker run --name qas-sql -e MYSQL_ROOT_PASSWORD=password -d mysql:latest


	>>   docker run  --name qas-wordpress --links qas-sql:mysql -p 8080:80 -d wordpress
