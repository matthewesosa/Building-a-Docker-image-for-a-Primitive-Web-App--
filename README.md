# Task 1 - Installation of Docker and Docker-Compose:
    * apt install docker
    * apt install docker-compose

-- Which docker versions (client, server, API) have you installed?

    * docker version
    Client Version:    20.10.7
    API version:       1.41
    Server4 Version:   20.10.7

    * docker-compose version
    docker-compose version 1.25.0


# Task 2 - Primitive Web Server (with FLASK):
-- verify that Python is installed on your system 

    * python3 -V

-- create a virtual environment for the flask application by using the venv module

    * sudo apt install python3-venv

-- Create a new directory for the Flask application and switch into it

    * mkdir miniserver && cd miniserver
    * python3 -m venv venv
    * source venv/bin/activate

-- While inside the activated virtual environment (miniserver directory), use the Python package manager pip to install Flask

    * pip install Flask      
     (Within the virtual environment, you can use the command pip instead of pip3 and python instead of python3.)

-- Creating the minisever Application

    from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Service Management 2021. My name is Matthew Igbinehi'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=20221)


-- Save the file as miniserver.py and go back to the virtual environment in the terminal window.

    * export FLASK_APP=miniserver.py
    * flask run

-- Building a Docker image for the Flask Web App
In the same 'miniserver' directory, create a Docker file (Docker) and a Requirement file (requirements.txt)

Docker file:

# init a base image (Alpine is small Linux distro)
FROM python:3.8.10-alpine
# define the present working directory
WORKDIR /miniserver
# copy the contents into the working dir
ADD . /miniserver
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","miniserver.py"]

Requirement file:

Flask==2.0.2


-- Build the docker image
* docker image build -t miniserver .
* docker image ls
* docker run -p 20221:20221 -d miniserver

-- Stop and prune
* docker stop "the container id"
*docker system prune






