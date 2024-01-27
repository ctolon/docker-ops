#!/bin/bash
# Simple bash script for deleting airflow variable.

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
  echo "Usage: $0 -k <key>"
  echo "Options:"
  echo "  -k, --key     Key"
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
  esac
done


# Check for missing arguments
check_missing_arg "$key" "-k|--key"

# If any required argument is missing, display error message
if [[ ${#missing_args[@]} -gt 0 ]]; then
  echo "Error: Missing required arguments: ${missing_args[*]}"
  display_help
fi


delete_airflow_variable() {
  echo "Deleting Airflow role: $key"
  echo "Value of key: "
  airflow variables get "$key"
  airflow variables delete "$key"
}

delete_airflow_variable