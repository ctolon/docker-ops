import argparse
from airflow.www.security import User
from airflow import settings
from sqlalchemy.orm import sessionmaker


# Delete the Airflow user
def delete_airflow_user(
    username: str,
):
    print(f"Deleting Airflow user: {username}")
    # Create a session
    Session = sessionmaker(bind=settings.engine)
    session = Session()

    # Retrieve the user from the database
    user = session.query(User).filter_by(username=username).first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully")
    else:
        print("User not found")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple script for deleting an Airflow user.')
    parser.add_argument('-u', '--username', help='Username', required=True)
    args = parser.parse_args()

    delete_airflow_user(
        args.username
    )