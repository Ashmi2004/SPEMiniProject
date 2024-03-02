FROM ubuntu:latest
FROM nginx:alpine
#FROM python:latest


#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
#RUN apt-get -y update
#RUN apt-get install -y google-chrome-stable

# Install specific version of chromedriver
#RUN CHROMEDRIVER_VERSION=94.0.4606.61 && \
#    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
#    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
#    rm /tmp/chromedriver.zip

# Install Selenium and other required packages
#RUN pip install selenium


COPY index.html /app/index.html
COPY style.css /app/style.css
COPY testing/test.py /app/test.py
COPY index.html /usr/share/nginx/html/index.html
COPY style.css /usr/share/nginx/html/style.css
#CMD [ "python", "./test.py" ]
