#!/bin/bash
# Simple bash script for creating airflow user.

set -e

# Function to check if a command is available
command_exists() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Error: Required command '$1' not found. Please make sure installed $1."
    exit 1
  fi
}

# Check if the 'airflow' command is available
command_exists "airflow"

# Declare an array to hold missing arguments
missing_args=()

# Function to display help message
display_help() {
  echo "Usage: $0 -f <firstname> -l <lastname> -r <rolename> -u <username> -p <password> -e <email>"
  echo "Options:"
  echo "  -f, --firstname    First name"
  echo "  -l, --lastname     Last name"
  echo "  -r, --rolename     Role name"
  echo "  -u, --username     Username"
  echo "  -p, --password     Password"
  echo "  -e, --email        Email"
  exit 1
}


# Check if any required argument is missing
check_missing_arg() {
  if [[ -z $1 ]]; then
    missing_args+=("$2")
  fi
}


# Parse command line arguments
while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    -f|--firstname)
      firstname="$2"
      shift
      shift
      ;;
    -l|--lastname)
      lastname="$2"
      shift
      shift
      ;;
    -r|--rolename)
      rolename="$2"
      shift
      shift
      ;;
    -u|--username)
      username="$2"
      shift
      shift
      ;;
    -p|--password)
      password="$2"
      shift
      shift
      ;;
    -e|--email)
      email="$2"
      shift
      shift
      ;;
    *)
      shift
      ;;
  esac
done


# Check for missing arguments
check_missing_arg "$firstname" "-f|--firstname"
check_missing_arg "$lastname" "-l|--lastname"
check_missing_arg "$rolename" "-r|--rolename"
check_missing_arg "$username" "-u|--username"
check_missing_arg "$password" "-p|--password"
check_missing_arg "$email" "-e|--email"

# If any required argument is missing, display error message
if [[ ${#missing_args[@]} -gt 0 ]]; then
  echo "Error: Missing required arguments: ${missing_args[*]}"
  display_help
fi


create_airflow_user() {
  echo "Creating Airflow user: $firstname $lastname"
  echo "Role: $rolename"
  echo "Username: $username"
  echo "Password: $password"
  echo "Email: $email"
  airflow users create -f "$firstname" -l "$lastname" -r "$rolename" -u "$username" -p "$password" -e "$email"
}

create_airflow_user