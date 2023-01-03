#Specify the parent image from which we build
FROM ubuntu:latest

#Set the working directory

WORKDIR /app

#Copy files from host

COPY GetFromTransElectrica.py .

#BUILD the aplication

# Run the application

CMD["python GetFromTranselectrica"]
