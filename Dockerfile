#Specify the parent image from which we build
FROM python:latest

#Set the working directory

WORKDIR /app

#Copy files from host

COPY GetFromTransElectrica.py .

RUN pip install beautifulsoup4 && \
    pip install selenium && \
    pip install webdriver-manager && \
    pip install PyMySQL

# Run the application

RUN python scrape_transelectirca.py
