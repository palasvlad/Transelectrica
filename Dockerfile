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

RUN apt-get install -y chromium-browser
# from ze internet
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# install selenium
RUN pip install selenium

# END FROM ZE INTERNET


# Run the application

RUN python GetFromTransElectrica.py
