# FROM ubuntu:latest
FROM python:latest
FROM django:latest

# update apt-get
RUN apt-get update
# RUN pip install --upgrade pip

# copy app files
COPY /app /home/app

# install requirements
COPY requirements.txt /
# RUN pip install -r requirements.txt && rm requirements.txt

# note workdir
WORKDIR /home/app

# set port
EXPOSE $PORT

# run app
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
