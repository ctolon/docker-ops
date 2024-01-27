"""MLFlow auth_config.ini generator script for experiment level permission management

@author: Cevat Batuhan Tolon
@contact: cevat.batuhan.tolon@cern.ch
"""

import dotenv
from pathlib import Path
from pprint import pprint

# dotenv file path
current_path = Path(__file__).parent.resolve()
dotenv_path = Path(__file__).parent.parent.resolve() / ".env"

print(f"Working Path: {current_path}")
print(f"dotenv file path: {dotenv_path}")

if not dotenv_path.is_file():
    raise FileNotFoundError(f".env file not found!: {dotenv_path}")

config = dotenv.dotenv_values(dotenv_path)

print(".env file config:")
pprint(config)

database_uri = config.get("MLFLOW_TRACKING_URI")
admin_username = config.get("MLFLOW_TRACKING_USERNAME")
admin_password = config.get("MLFLOW_TRACKING_PASSWORD")
permission_level = config.get("PERM_LEVEL")


auth_ini_template = f"""
[mlflow]
default_permission={permission_level}
database_uri={database_uri}
admin_username={admin_username}
admin_password={admin_password}
"""

print("auth.ini template will be generated as:")
print(auth_ini_template)

with open('auth_config.ini', 'w') as f:
    f.write(auth_ini_template)

print("auth_config.ini created.")


