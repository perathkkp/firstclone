# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

# RUN apt-get update && apt-get install --quiet --assume-yes unzip wget
# 0. Install essential packages
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
    && rm -rf /var/lib/apt/lists/*

# 1. Install Chrome (root image is debian)
# See https://stackoverflow.com/questions/49132615/installing-chrome-in-docker-file
ARG CHROME_VERSION="google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    ${CHROME_VERSION:-google-chrome-stable} \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# 2. Install Chrome driver used by Selenium
RUN LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget --output-document /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver_linux64.zip -d /opt && \
    ln -s /opt/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver

ENV PATH="/usr/local/bin/chromedriver:${PATH}"

# 3. Install selenium in Python
# RUN pip install -U selenium
RUN pip install -U playwright
# RUN pip install -U pyppeteer

RUN python -m playwright install

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot