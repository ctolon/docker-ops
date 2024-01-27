#!/bin/bash
# Simple bash script for deleting airflow connection

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
  echo "Usage: $0 -r <rolename>"
  echo "Options:"
  echo "  -c, --connection-name    Connection name"
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
    -c|--connection-name)
      conname="$2"
      shift
      shift
      ;;
  esac
done


# Check for missing arguments
check_missing_arg "$conname" "c-|--connection-name"

# If any required argument is missing, display error message
if [[ ${#missing_args[@]} -gt 0 ]]; then
  echo "Error: Missing required arguments: ${missing_args[*]}"
  display_help
fi


delete_airflow_connection() {
  echo "Deleting Airflow connection: $conname"
  echo "Connection Name: $conname"
  airflow connections delete "$conname"
}

delete_airflow_connection