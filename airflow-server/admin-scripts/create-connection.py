
import logging
from airflow import settings
from airflow.models import Connection
import argparse

def create_conn(conn_id, conn_type, host, login, pwd, port, desc):
    conn = Connection(conn_id=conn_id,
                      conn_type=conn_type,
                      host=host,
                      login=login,
                      password=pwd,
                      port=port,
                      description=desc)
    session = settings.Session()
    conn_name = session.query(Connection).filter(Connection.conn_id == conn.conn_id).first()

    if str(conn_name) == str(conn.conn_id):
        logging.warning(f"Connection {conn.conn_id} already exists")
        return None

    session.add(conn)
    session.commit()
    logging.info(Connection.log_info(conn))
    logging.info(f'Connection {conn_id} is created')
    return conn

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a connection on airflow")
    parser.add_argument("-cid", "--conn-id", required=True, help="Connection ID", type=str)
    parser.add_argument("-ct", "--conn-type", required=True, help="Connection type", type=str)
    parser.add_argument("-h", "--host", required=True, help="Host", type=str)
    parser.add_argument("-l", "--login", required=True, help="login as username", type=str)
    parser.add_argument("-pw", "--password", required=True, help="List of accessible dags for the role", type=str)
    parser.add_argument("-p", "--port", required=True, help="List of accessible dags for the role", type=str)
    parser.add_argument("-d", "--description", required=True, help="List of accessible dags for the role", type=str)


    args = parser.parse_args()
    create_conn(
        args.conn_id,
        args.conn_type,
        args.host,
        args.login,
        args.password,
        args.port,
        args.description
    )