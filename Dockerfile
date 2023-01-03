#Create a directory to work in
mkdir Transelectrica
cd Transelectrica

#create an exampele file - maybe to the git pull here?
touch somefile.txt

#build an image using the current directory as context, and a docker file passed through stdin
docker build -t transimage:latest -f-
FROM ubuntu:latest
COPY somefile.txt ./
RUN cat /somefile.txt