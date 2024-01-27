import argparse
import subprocess


def delete_airflow_connection(conname):
    command = ["airflow", "connections", "delete", conname]
    subprocess.run(command)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--connection-name", required=True, help="Connection name")
    args = parser.parse_args()

    conname = args.connection_name

    delete_airflow_connection(conname)


if __name__ == "__main__":
    main()