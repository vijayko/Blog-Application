# Django Project Boilerplate 
This repository contains a boilerplate to start any Django project with Docker. 

## Getting started 

Docker Installation: 
- You can find the [instructions](https://docs.docker.com/compose/install/) here to install Docker. 
- Please make sure that Docker is running (in the background) before you use the commands related to Docker. 

Steps: 
1. Clone/download this repository. 
2. Create a virtual environment using the command `python3 -m venv .venv`; activate the virtual environment using `source .venv/bin/activate`.
3. Run `pip install -r requirements.txt` to install dependencies. 
4. Deactivate the virtual environment using `deactivate` in the terminal. 
5. Configure your environment variables in docker-compose.yml file 
6. Run `docker-compose up -d --build` to install the dependencies in Docker container. 
7. Run `docker-compose exec web python manage.py rename <currentprojectname> <newprojectname>`

This project includes: 
1. Setting module with env variables. 
2. docker-compose.yml for env variables and Dockerfile 

Project Structure: 
<p align="left">
    <p align="left">
        <img src="https://github.com/vijayko/Django-Boiler-Plate/blob/main/project-structure.png" alt="Prject Structure" width="500">
    </p>
</p>    