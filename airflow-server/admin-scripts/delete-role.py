import argparse
from airflow.www.security import Role
from airflow import settings
from sqlalchemy.orm import sessionmaker


# Delete the Airflow role
def delete_airflow_role(rolename: str):
    print(f"Deleting Airflow role: {rolename}")

    # Create a session
    Session = sessionmaker(bind=settings.engine)
    session = Session()

    # Retrieve the role from the database
    role = session.query(Role).filter_by(name=rolename).first()
    if role:
        session.delete(role)
        session.commit()
        print("Role deleted successfully")
    else:
        print("Role not found")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple script for deleting an Airflow role.')
    parser.add_argument('-r', '--rolename', help='Role name', required=True)
    args = parser.parse_args()

    delete_airflow_role(args.rolename)