#!/bin/bash

# Function to display help message
display_help() {
  echo "Usage: $0 -c <conn-id> -t <conn-type> -u <conn-url> -p <conn-password>"
  echo "Options:"
  echo "  -c, --conn-id       Connection ID"
  echo "  -t, --conn-type     Connection type"
  echo "  -u, --conn-url      Connection URL"
  echo "  -p, --conn-password Connection password"
  exit 1
}

# Function to check if a command is available
command_exists() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Error: Required command '$1' not found. Please make sure it is installed."
    exit 1
  fi
}

# Check if the 'airflow' command is available
command_exists "airflow"

# Declare an array to hold missing arguments
missing_args=()

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
    -c|--conn-id)
      conn_id="$2"
      shift
      shift
      ;;
    -t|--conn-type)
      conn_type="$2"
      shift
      shift
      ;;
    -u|--conn-url)
      conn_url="$2"
      shift
      shift
      ;;
    -p|--conn-password)
      conn_password="$2"
      shift
      shift
      ;;
    -h|--help)
      display_help
      ;;
    *)
      echo "Error: Invalid argument: $key"
      display_help
      ;;
  esac
done

# Check for missing arguments
check_missing_arg "$conn_id" "Connection ID"
check_missing_arg "$conn_type" "Connection type"
check_missing_arg "$conn_url" "Connection URL"
check_missing_arg "$conn_password" "Connection password"

# If any required argument is missing, display error message
if [[ ${#missing_args[@]} -gt 0 ]]; then
  echo "Error: Missing required arguments: ${missing_args[*]}"
  display_help
fi

# Use the arguments to create the Airflow connection
create_airflow_connection() {
  echo "Creating Airflow connection:"
  echo "Connection ID: $conn_id"
  echo "Connection Type: $conn_type"
  echo "Connection URL: $conn_url"
  echo "Connection Password: $conn_password"
  airflow connections add "$conn_id" --conn-type "$conn_type" --conn-uri "$conn_url" --conn-password "$conn_password"
}

# Call the function to create the Airflow connection
create_airflow_connection