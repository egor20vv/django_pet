FROM python:3.8

# upgrade pip
RUN apt-get update
RUN python -m pip install --upgrade pip

# install requirements
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt && rm requirements.txt

COPY . /home/app