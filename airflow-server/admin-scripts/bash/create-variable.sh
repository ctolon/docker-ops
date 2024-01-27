#!/bin/bash
# Simple bash script for creating airflow variable.

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
  echo "Usage: $0 -k <key> -v <value>"
  echo "Options:"
  echo "  -k, --key     Key"
  echo "  -v, --value   Value"
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
  index="$1"
  case $index in
    -k|--key)
      key="$2"
      shift
      shift
      ;;
    -v|--value)
      value="$2"
      shift
      shift
      ;;
  esac
done


# Check for missing arguments
check_missing_arg "$key" "-k|--key"
check_missing_arg "$value" "-v|--value"

# If any required argument is missing, display error message
if [[ ${#missing_args[@]} -gt 0 ]]; then
  echo "Error: Missing required arguments: ${missing_args[*]}"
  display_help
fi


create_airflow_variable() {
  echo "Creating Airflow variable: { $key : $value }"
  echo "key: $key"
  echo "value: $value"
  airflow variables set "$key" "$value"
}

create_airflow_variable