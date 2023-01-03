#Specify the parent image from which we build
FROM python:latest

#Set the working directory

WORKDIR /app

#Copy files from host

COPY GetFromTransElectrica.py .

RUN pip install beautifulsoup4

#BUILD the aplication

# Run the application

RUN python GetFromTransElectrica.py
