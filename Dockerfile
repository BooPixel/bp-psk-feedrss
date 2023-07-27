ARG APP_PATH=/opt

FROM python:3.11-slim
ARG APP_PATH
WORKDIR $APP_PATH

RUN apt-get -y update
RUN apt-get install -y wget gnupg unzip

# ===== Chrome stuff =====
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get -y update && apt-get install -y google-chrome-stable

RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.16/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# ===== Chrome stuff =====

COPY . $APP_PATH

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "src/main.py"]
