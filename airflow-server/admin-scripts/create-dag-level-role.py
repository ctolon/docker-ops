"""Airflow DAG Level Role Creation Script with Permissions."""
from typing import List
import requests
import argparse
import configparser

def create_rbac_role_with_permissions(
    config: str, 
    new_role_name: str, 
    dag_names: List[str]=None,
):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    
    # Get Username - Password and airflow base url from config.ini
    settings = configparser.ConfigParser()
    settings.read(config)
    if len(settings.sections()) == 0:
        raise ValueError("Config file is empty!")
    airflow_url = settings.get("airflow", "url")
    username = settings.get("airflow", "username")
    password = settings.get("airflow", "password")

    read = "can_read"
    edit = "can_edit"
    delete = "can_delete"

    # add dag-specific permissions
    permissions = []
    for dag in dag_names:
        dag = "DAG:" + dag
        read_permissions = make_permissions(read,[dag])
        edit_permissions = make_permissions(edit, [dag])
        delete_permissions = make_permissions(delete, [dag])
    permissions += read_permissions + edit_permissions + delete_permissions
    
    data = {
        "actions": [
            *permissions
        ],
        "name": new_role_name
    }
    
    airflow_url += "/api/v1/roles"
    response = requests.post(airflow_url, json=data, headers=headers, auth=(username, password))

    if response.status_code == 403:
        raise PermissionError(f"Error 403 returned, please check if your AirFlow account is Op/Admin or verify the dags exist. \n {response.json()}")
    elif response.status_code == 401:
        raise PermissionError(f"Error 401 returned, please check the access token if the page is protected by an authentication")
    elif response.status_code == 200:
        print(f"Role `{new_role_name}` successfuly created.")
    else:
        raise ConnectionError(f"An error occured during role creation: {response.json()}")

def make_permissions(action, resources):
    permissions = []
    for perm in resources:
        permissions.append(make_permission(action, perm))
    return permissions

def make_permission(action, resource):
    return {
        "action": {"name": action},
        "resource": {"name": resource}
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", required=False, help="Path to config.ini file", default="./config/airflow.ini", type=str)
    parser.add_argument("-r", "--role-name", required=True, help="Name of the new created role")
    parser.add_argument("-d", "--dags", nargs="+", required=True, help="List of accessible dags for the role")

    args = parser.parse_args()
    create_rbac_role_with_permissions(
        args.config,
        args.role_name,
        args.dags,
    )