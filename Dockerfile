FROM python:3.9-alpine
#Commande qui va s'executer à la construction de l'image : creation de la directory /home/app
RUN mkdir -p /home/app

#si WORKDIR /home/app => COPY . .

#copie de tous les fichiers courants dans /home/app
COPY . /home/app

#Commande qui sera executé lors de la création du conteneur
CMD ["python3" , "/home/app/main.py" , "-h"]

#Common idiom to keep the dokcontainer alive indefinetely
ENTRYPOINT ["tail", "-f", "/dev/null"]


#EXPOSE 443 pour mentionner le port par défaut 


#docker build -t infection . #creation de l'image
#docker run -d -p 80:80 --name container_named fraction:1.0    #Lancement du conteneur

#docker start name_container --si necessaire
#docker exec -it container_named /bin/sh  #pour avoir acces à la ligne de commande

#docker rmi image_id 