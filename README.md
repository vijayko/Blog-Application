# Blog Application in Django 
This repository contains a blog application built in Django with Docker. 

# Features Implemented 
- [x] A user can create, update, and delete a blog post.
- [x] A user can signup/login.
- [x] Only an author can edit/delete their post(s). 
- [x] A user can post comments in each post. 

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


