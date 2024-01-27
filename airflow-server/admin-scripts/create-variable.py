#!/usr/bin/env python3
import argparse
from airflow import models, settings
from sqlalchemy.orm import sessionmaker

# Create the Airflow variable
def create_airflow_variable(key: str, value: str, description: str = None):

    print(f"Creating Airflow variable: {{ {key} : {value} }}")
    print(f"Key: {key}")
    print(f"Value: {value}")

    # Create a session
    Session = sessionmaker(bind=settings.engine)
    session = Session()

    # Create or update the variable
    variable = session.query(models.Variable).filter_by(key=key).first()
    if variable:
        variable.set_val(value)
    else:
        variable = models.Variable(key=key, val=value, description=description)
        session.add(variable)

    session.commit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple script for creating an Airflow variable.')
    parser.add_argument('-k', '--key', help='Key', required=True)
    parser.add_argument('-v', '--value', help='Value', required=True)
    parser.add_argument('-d', '--description', help='Description', required=False)
    args = parser.parse_args()

    create_airflow_variable(
        args.key,
        args.value,
        args.description
    )
