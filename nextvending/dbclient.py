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
        query = "INSERT INTO product_transactions VALUES (uuid_generate_v4(), {price}, {quantity_remaining}, TO_TIMESTAMP('{timestamp}'), '{product_id}', '{machine_id}');".format(
            price=transaction_data["price"],
            quantity_remaining=transaction_data["quantity_remaining"],
            timestamp=transaction_data["timestamp"],
            product_id=transaction_data["product_id"],
            machine_id=transaction_data["machine_id"]
        )
        self._cur.execute(query)
        self._conn.commit()


    def add_new_payment(self, payment_data):
        # TODO
        query = "INSERT INTO payment_transactions VALUES (uuid_generate_v4(), {amount}, '{user_id}', '{first_name}', '{last_name}', TO_TIMESTAMP('{timestamp}'), '{machine_id}');".format(
            amount=payment_data["amount"],
            user_id=payment_data["user_id"],
            first_name=payment_data["first_name"],
            last_name=payment_data["last_name"],
            timestamp=payment_data["timestamp"],
            machine_id=payment_data["machine_id"],
        )
        self._cur.execute(query)
        self._conn.commit()

    