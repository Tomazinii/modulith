import psycopg2
from .db_config import config

def connect():
    """ connect to the postgresql database server """

    conn = None

    # try:

    #     params = config()

    #     conn = psycopg2.connect(**params)

    #     cur = conn.cursor()

    #     cur.execute("SELECT version()")
