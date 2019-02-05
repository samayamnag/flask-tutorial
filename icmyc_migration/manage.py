# manage.py


import unittest

from flask.cli import FlaskGroup

from src.app import create_app, db
from src.app.models import User, IcmycUser
from src.app.mongo_models import Profile, Channel, Role
import subprocess
import sys
from src.app.utils import fetch_icmyc_users, find_or_create_sm_user



app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def migrate_users():
    from_id = input("From user ID:")
    to_id = input("To user ID:")
    try:
        from_id = int(from_id)
        to_id = int(to_id)
        if from_id > 0 and to_id > 0:
            icmyc_users = fetch_icmyc_users(from_id, to_id)
            print("***************************")
            for icmyc_user in icmyc_users:
                user = find_or_create_sm_user(icmyc_user)
                print(f'Swachhata user Id: {user.id}')
            print("***************************")
        else:
            print("Input should be positive integer")
    except ValueError:
        print("Input should be an integer")


@cli.command()
def flake():
    """Runs flake8 on the project."""
    subprocess.run(["flake8", "src"])


if __name__ == "__main__":
    cli()
