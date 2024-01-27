"""Airflow General Role Creation Script with Permissions."""
import requests
import argparse
import configparser
import json

# Usage ex: python3 create-role.py -r user

def create_rbac_role_with_permissions(
    config: str, 
    new_role_name: str, 
    role_json: dict
):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    read = "can_read"
    edit = "can_edit"
    create = "can_create"
    delete = "can_delete"
    menu = "menu_access"
    
    # Get Username - Password and airflow base url from config.ini
    settings = configparser.ConfigParser()
    settings.read(config)
    if len(settings.sections()) == 0:
        raise ValueError("Config file is empty!")
    airflow_url = settings.get("airflow", "url")
    username = settings.get("airflow", "username")
    password = settings.get("airflow", "password")
    
    # add general permissions
    permissions = []
    if new_role_name == "user":
        read_permissions = make_permissions(read,role_json[new_role_name]["read_permissions"])
        menu_permissions = make_permissions(menu, role_json[new_role_name]["menu_permissions"])
        permissions = read_permissions + menu_permissions
    
    if new_role_name == "developer":
        read_permissions = make_permissions(read,role_json[new_role_name]["read_permissions"])
        edit_permissions = make_permissions(edit, role_json[new_role_name]["edit_permissions"])
        create_permissions = make_permissions(create, role_json[new_role_name]["create_permissions"])
        menu_permissions = make_permissions(menu, role_json[new_role_name]["menu_permissions"])
        permissions = read_permissions + edit_permissions + create_permissions + menu_permissions
        
    if new_role_name == "senior_developer":
        read_permissions = make_permissions(read,role_json[new_role_name]["read_permissions"])
        edit_permissions = make_permissions(edit, role_json[new_role_name]["edit_permissions"])
        create_permissions = make_permissions(create, role_json[new_role_name]["create_permissions"])
        delete_permissions = make_permissions(delete, role_json[new_role_name]["delete_permissions"])
        menu_permissions = make_permissions(menu, role_json[new_role_name]["menu_permissions"])
        permissions = read_permissions + edit_permissions + create_permissions + delete_permissions + menu_permissions
    
    data = {
        "actions": [
            *permissions
        ],
        "name": new_role_name
    }
    
    # Send request to airflow roles endpoint
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
    
    with open("./config/roles.json") as f:
        f = json.load(f)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", required=False, help="Path to config.ini file", default="./config/airflow.ini", type=str)
    parser.add_argument("-r", "--role-name", required=True, help="Name of the new created role", choices=f.keys())

    args = parser.parse_args()
    create_rbac_role_with_permissions(
        args.config,
        args.role_name,
        f
    )