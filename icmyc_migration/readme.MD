## Migrate ICMYC users SWachh Manch ##

### Prerequisites ###

    *  Python >= 3.7
    *  pipenv >= 2018.11.26
    *  MongoDB >= 3.6

### Installation ###
    * run `cp .env.example .env`
    * configure .env
    * run `pipenv shell --python=3.7` to set up environment. --python argument is optional. This is to       specify specific python version 
    * run `pipenv install` to install dependencies

### Run the Application

```sh
>>> pipenv shell
>>> python manage.py migrate-users
```
