import os
import psycopg2

class DBClient:
    def __init__(self, db_conf):
        try:
            self._conn = psycopg2.connect(
                host=db_conf["HOST"],
                port=db_conf["PORT"],
                user=db_conf["USER"],
                password=db_conf["PASSWORD"],
                database=db_conf["DATABASE"]
            )
            self._cur = self._conn.cursor()

            # Print version
            self._cur.execute("SELECT version();")
            print("Connected to {}".format(self._cur.fetchone()))

            self._cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

        except (Exception, psycopg2.Error) as error:
            print("Error in the connection --- {}".format(error))
            exit()

    def close_db_connection(self):
        self._cur.close()
        self._conn.close()
        print("DB connection closed")

    def add_new_transaction(self, transaction_data):
        # TODO
        query = """INSER INTO product_transaction 
                   VALUES (uuid_generate_v4())"""

    def add_new_payment(self, payment_data):
        # TODO
        pass

    