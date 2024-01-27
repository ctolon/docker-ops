#!/usr/bin/env python3
import argparse
import getpass
from airflow.www.security import User
from airflow import settings
from sqlalchemy.orm import sessionmaker
import os

# Check if an Airflow user already exists
def user_exists(username):
    Session = sessionmaker(bind=settings.engine)
    session = Session()
    user = session.query(User).filter(User.username == username).first()
    return user is not None


# Create the Airflow user
def create_airflow_user(
    firstname: str,
    lastname: str,
    rolename: str,
    username: str,
    password: str,
    email: str
):
    
    # Check if the user already exists
    if user_exists(username):
        print(f"User {username} already exists.")
        return

    print(f"Creating Airflow user: {firstname} {lastname}")
    print(f"Role: {rolename}")
    print(f"Username: {username}")
    print(f"Email: {email}")
    
    cmd_to_run = (f"airflow users create -f='{firstname}' -l='{lastname}' -r='{rolename}' -u='{username}' -p='{password}' -e='{email}'")
    print(f"command to run: {cmd_to_run}")
    os.system(cmd_to_run)

    # print(f"User: {username} created successfully")
    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Simple script for creating an Airflow user.')
    parser.add_argument('-f', '--firstname', help='First name', required=True)
    parser.add_argument('-l', '--lastname', help='Last name', required=True)
    parser.add_argument('-r', '--rolename', help='Role name', required=True)
    parser.add_argument('-u', '--username', help='Username', required=True)
    parser.add_argument('-p', '--password', help='Password', required=True)
    parser.add_argument('-e', '--email', help='Email', required=True)
    args = parser.parse_args()
    
    create_airflow_user(
        args.firstname,
        args.lastname,
        args.rolename,
        args.username,
        args.password,
        args.email
    )
