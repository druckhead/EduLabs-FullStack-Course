import psycopg2 as pg
from flask import Flask, jsonify, request

from .config import get_config

app = Flask(__name__)

# get config info for bank db
params = get_config()
# connect to bank db
conn = pg.connect(**params)


@app.route("/")
def home():
    return "Welcome to Daniel's Bank!"


@app.route("/api/v1/customers", methods=["GET"])
def all_customers():
    args = request.args
    # name = args.get("name")
    return "customers"


@app.route("/api/v1/customers/<int:customer_id>", methods=["GET"])
def customers_id(customer_id: int):
    with conn:
        with conn.cursor() as curs:
            sql = f"""
                SELECT *
                FROM customers c
                WHERE c.id = %s
                """
            curs.execute(sql, (customer_id,))
            result = curs.fetchone()
            if result:
                response = jsonify(result)
                return response


@app.route("/api/v1/accounts", methods=["GET"])
def all_accounts():
    return "accounts"


@app.route("/api/v1/accounts/<int:account_id>", methods=["GET"])
def accounts_id(account_id: int):
    return f"Account id: {account_id}"


if __name__ == "__main__":
    app.run(debug=True)
