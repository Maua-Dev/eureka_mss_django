# eureka_api 💡
Repository for the Eureka backend microservice, programmed in Python using the Django Framework.

# Requirements 📋
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Django 4.2](https://docs.djangoproject.com/en/4.2/topics/install/#installing-official-release)
- [Docker](https://www.docker.com/products/docker-desktop/)

# Installation 👩‍💻
### Create virtual ambient in python (only first time) 🐍

###### Windows

    python -m venv venv

###### Linux

    virtualenv -p python3.11 venv

### Activate the venv 🗺

###### Windows:

    venv\Scripts\activate

###### Linux:

    source venv/bin/activate

### Install the requirements 😋

    pip install -r requirements.txt

### Compose the docker (only first time) 🐋

    docker-compose up -d

### To test in real time, put in your brownser 

    localhost:8000

### Run the tests for mock 🧪

    python manage.py test

### To run local set .env file according the .env.example file 🤗

    cp .env.example .env 

### Populate DB 
### Install DBeaver (recommended)
### Create a connection and select PostgressSQL as your DB  
### Put host as localhost, port as 5432, and the same user and password that it is in your .env file.
### Run the querrys that are in the populate_database directory

## Contributors 💰🤝💰

- Bruno Vilardi - [Brvilardi](https://github.com/Brvilardi) 👷‍♂️
- Hector Guerrini - [hectorguerrini](https://github.com/hectorguerrini) 🧙‍♂️
- João Branco - [JoaoVitorBranco](https://github.com/JoaoVitorBranco) 😎
- Vitor Soller - [VgsStudio](https://github.com/VgsStudio) ☀
- Luigi Trevisan - [LuigiTrevisan](https://github.com/LuigiTrevisan) 🍄
