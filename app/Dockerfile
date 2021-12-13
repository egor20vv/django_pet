FROM tiangolo/uvicorn-gunicorn

# upgrade pip
RUN python -m pip install --upgrade pip

# install requirements
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt && rm requirements.txt

# set docker env
ENV DOCKER 1

# copy app files
WORKDIR /home/app
COPY . .


