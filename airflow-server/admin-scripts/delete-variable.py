import argparse
from airflow.models import Variable


# Delete the Airflow variable
def delete_airflow_variable(key: str):
    print(f"Deleting Airflow variable: {key}")

    # Retrieve the current value of the variable (optional)
    value = Variable.get(key)
    print(f"Value of key: {value}")

    # Delete the variable
    Variable.delete(key)
    print("Variable deleted successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple script for deleting an Airflow variable.')
    parser.add_argument('-k', '--key', help='Key', required=True)
    args = parser.parse_args()

    delete_airflow_variable(args.key)