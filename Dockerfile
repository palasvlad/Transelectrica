#Specify the parent image from which we build
FROM python:latest

#Set the working directory

WORKDIR /app

#Copy files from host
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

COPY scrape_transelectirca.py .

RUN chmod +x scrape_transelectirca.py


CMD["python","scrape_transelectirca.py"]
