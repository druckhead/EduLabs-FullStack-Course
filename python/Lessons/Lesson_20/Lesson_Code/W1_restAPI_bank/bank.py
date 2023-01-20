import psycopg2 as pg
from flask import Flask, jsonify, request, abort

from .config import get_config

app = Flask(__name__)

# get config info for bank db
params = get_config()
# connect to bank db
conn = pg.connect(**params)


def serialize_customers(result):
    return {"passport_num": result[1], "name": result[2], "address": result[3]}


def serialize_accounts(result):
    return {"balance": result[1], "max_limit": result[2]}


def serialize_account_owners(results):
    return results[2]


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/")
def home():
    return "Welcome to Daniel's Bank!"


@app.route("/api/v1/customers", methods=["GET", "POST"])
def all_customers():
    if request.method == "GET":
        if request.args.get("page_num") is None:
            page_num = None
        else:
            page_num = int(request.args.get("page_num"))

        if request.args.get("results_per_page") is None:
            results_per_page = None
        else:
            results_per_page = int(request.args.get("results_per_page"))

        if request.args.get("city") is None:
            city = None
        else:
            city = request.args.get("city")

        if request.args.get("name_contains") is None:
            name_contains = None
        else:
            name_contains = request.args.get("name_contains")

        if (
            page_num is None
            and results_per_page is None
            and city is None
            and name_contains is None
        ):
            # get all customers
            with conn:
                with conn.cursor() as curs:
                    sql = f"""
                    SELECT *
                    FROM customers c
                    """
                    curs.execute(
                        sql,
                        (
                            city,
                            name_contains,
                        ),
                    )
                    result = curs.fetchall()
        else:
            # check query params if only one is given then give the other a default value
            if page_num is None:
                # default value
                page_num = 1
            if results_per_page is None:
                # default value
                results_per_page = 20
            if name_contains is None:
                name_contains = "%"

            with conn:
                with conn.cursor() as curs:
                    sql = f"""
                        SELECT *
                        FROM customers c
                        WHERE c.address ILIKE %s and c.name ILIKE %s
                        LIMIT %s
                        OFFSET %s
                        """
                    curs.execute(
                        sql,
                        (
                            f"%{city}%",
                            f"%{name_contains}%",
                            results_per_page,
                            page_num - 1,
                        ),
                    )
                    result = curs.fetchall()

        if result:
            response = {"data": {"customers": {}}}
            for r in result:
                response["data"]["customers"].update(
                    {f"{r[0]}": serialize_customers(r)}
                )
            return jsonify(response)
        else:
            abort(404, description="Resource Not Found")

    # TODO check returning status with the post
    if request.method == "POST":
        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":
            json = request.json
            with conn:
                with conn.cursor() as curs:
                    sql = f"""
                    INSERT INTO customers (passport_num, name, address)
                    VALUES (%s, %s, %s)
                    """
                    curs.execute(
                        sql, (json["passport_num"], json["name"], json["address"])
                    )
            return json
        else:
            return "Content-Type not supported!"


@app.route("/api/v1/customers/<int:customer_id>", methods=["GET", "PUT", "DELETE"])
def customer_data(customer_id: int):
    if request.method == "GET":
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
                    response = jsonify(data=serialize_customers(result))
                    return response
                else:
                    abort(404, description="Resource Not Found")
    if request.method == "PUT":
        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":
            content_set = []
            content_values = []
            json = request.json
            if json["passport_num"]:
                content_set.append("passport_num = %s")
                content_values.append(json["passport_num"])
            if json["name"]:
                content_set.append("name = %s")
                content_values.append(json["name"])
            if json["address"]:
                content_set.append("address = %s")
                content_values.append(json["address"])
            with conn:
                with conn.cursor() as curs:
                    sql = f"""
                    UPDATE customers
                    SET {', '.join(content_set)}
                    WHERE id = %s
                    """
                    curs.execute(
                        sql,
                        (
                            content_values[0],
                            content_values[1],
                            content_values[2],
                            customer_id,
                        ),
                    )
                    return json
    if request.method == "DELETE":
        content_type = request.headers.get("Content-Type")
        sql = """
        DELETE FROM customers
        WHERE id = %s
        """
        with conn:
            with conn.cursor() as curs:
                curs.execute(sql, (customer_id,))
        return jsonify()


@app.route("/api/v1/customers/<int:customer_id>/accounts", methods=["GET"])
def customer_accounts(customer_id: int):
    with conn:
        with conn.cursor() as curs:
            sql = f"""
            SELECT *
            FROM account_owners accown
            WHERE accown.customer_id = %s
            """
            curs.execute(sql, (customer_id,))
            result = curs.fetchall()
            if result:
                response = {"data": {"account_ids": []}}
                for r in result:
                    response["data"]["account_ids"].append(serialize_account_owners(r))
                return jsonify(response)
            else:
                abort(404, description="Resource Not Found")


"""
ACCOUNTS START HERE
"""


@app.route("/api/v1/accounts", methods=["GET", "POST"])
def all_accounts():
    if request.method == "GET":
        if request.args.get("page_num") is None:
            page_num = None
        else:
            page_num = int(request.args.get("page_num"))

        if request.args.get("results_per_page") is None:
            results_per_page = None
        else:
            results_per_page = int(request.args.get("results_per_page"))

        balance = request.args.get("balance")
        max_limit = request.args.get("max_limit")

        if page_num is None and results_per_page is None:
            # get all customers
            with conn:
                with conn.cursor() as curs:
                    if balance and not max_limit:
                        sql = f"""
                        SELECT *
                        FROM accounts a
                        WHERE a.balance = %s
                        """
                        curs.execute(sql, (balance,))
                    elif max_limit and not balance:
                        sql = f"""
                        SELECT *
                        FROM accounts a
                        WHERE a.max_limit = %s
                        """
                        curs.execute(sql, (max_limit,))
                    elif balance and max_limit:
                        sql = f"""
                        SELECT *
                        FROM accounts a
                        WHERE a.balance = %s AND a.max_limit = %s
                        """
                        curs.execute(sql, (balance, max_limit))
                    else:
                        sql = f"""
                        SELECT *
                        FROM accounts a
                        """
                        curs.execute(sql)
                    result = curs.fetchall()
        else:
            # check query params if only one is given then give the other a default value
            if page_num is None:
                # default value
                page_num = 1
            if results_per_page is None:
                # default value
                results_per_page = 20

            with conn:
                with conn.cursor() as curs:
                    sql = f"""
                        SELECT *
                        FROM accounts a
                        LIMIT %s
                        OFFSET %s
                        """
                    curs.execute(sql, (results_per_page, page_num - 1))
                    result = curs.fetchall()

        if result:
            response = {"data": {"accounts": {}}}
            for r in result:
                response["data"]["accounts"].update({f"{r[0]}": serialize_accounts(r)})
            return jsonify(response)
        else:
            abort(404, description="Resource Not Found")

    if request.method == "POST":
        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":
            json = request.json
            with conn:
                with conn.cursor() as curs:
                    sql = f"""
                    INSERT INTO accounts (balance, max_limit)
                    VALUES (%s, %s);
                    """
                    curs.execute(sql, (0, json["max_limit"]))
                    sql = """
                    INSERT INTO account_owners (customer_id, account_id)
                    VALUES (%s, %s);
                    """
                    curs.execute(sql, (json["customer_id"], json["account_id"]))
            return json
        else:
            return "Content-Type not supported!"


@app.route("/api/v1/accounts/<int:account_id>", methods=["GET", "DELETE"])
def accounts_id(account_id: int):
    if request.method == "GET":
        with conn:
            with conn.cursor() as curs:
                sql = f"""
                    SELECT *
                    FROM accounts a
                    WHERE a.id = %s
                    """
                curs.execute(sql, (account_id,))
                result = curs.fetchone()
                if result:
                    response = jsonify(data=serialize_accounts(result))
                    return response
                else:
                    abort(404, description="Resource Not Found")

    if request.method == "DELETE":
        sql = """
        DELETE FROM accounts
        WHERE id = %s
        """
        sql2 = """
        DELETE FROM account_owners ao
        WHERE ao.account_id = %s
        """
        with conn:
            with conn.cursor() as curs:
                curs.execute(sql2, (account_id,))
                curs.execute(sql, (account_id,))
        return jsonify()


@app.route("/api/v1/accounts/<int:account_id>/deposit", methods=["POST"])
def deposit(account_id: int):
    body = request.json
    amount = body["amount"]
    with conn:
        with conn.cursor() as curs:
            sql = """
            UPDATE accounts a
            SET balance = balance + %s
            WHERE a.id = %s
            """
            curs.execute(sql, (amount, account_id))

            # TODO update transactions

            return jsonify()


@app.route("/api/v1/accounts/<int:account_id>/withdraw", methods=["POST"])
def withdraw(account_id: int):
    body = request.json
    amount = body["amount"]
    with conn:
        with conn.cursor() as curs:
            sql = """
            SELECT a.balance, a.max_limit
            FROM accounts a
            WHERE a.id = %s
            """
            curs.execute(sql, (account_id,))
            balance, max_limit = curs.fetchone()
            if balance - amount < (-max_limit):
                return jsonify(
                    "This withdrawl will put you under your max limit, can't "
                )
            sql = """
            UPDATE accounts a
            SET balance = balance - %s
            WHERE a.id = %s
            """
            curs.execute(sql, (amount, account_id))

            # TODO update transactions

            return jsonify()


@app.route("/api/v1/accounts/<int:account_id>/transfer", methods=["POST"])
def transfer(account_id: int):
    body = request.json
    to_account_id = body["to_account_id"]
    amount = body["amount"]
    initiated_by = body["initiated_by"]
    
    with conn:
        with conn.cursor() as curs:
            sql = """
            INSERT INTO transactions (
                transaction_type,
                ts,
                initiated_by
            ) VALUES (
                'transfer',
                date_trunc('second', now()::timestamp),
                %s
            )
            """
            curs.execute(sql, (initiated_by,))
            sql = """
            INSERT INTO transaction_accounts (
                account_role,
                transaction_id,
                account_id
            ) VALUES (
                'sender',
                currval(pg_get_serial_sequence('transactions', 'id')),
                %s
            )
            """
            curs.execute(sql, (account_id,))
            sql = """
            INSERT INTO transaction_accounts (
                account_role,
                transaction_id,
                account_id
            ) VALUES (
                'receiver',
                currval(pg_get_serial_sequence('transactions', 'id')),
                %s
            )
            """
            curs.execute(sql, (to_account_id,))
            sql = """
            UPDATE accounts
            SET balance = balance - %s
            WHERE id=%s;
            """
            curs.execute(sql, (amount, account_id))
            sql = """
            UPDATE accounts
            SET balance = balance + %s
            WHERE id=%s;
            """
            curs.execute(sql, (amount, to_account_id))
        
        return jsonify()
            
if __name__ == "__main__":
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        conn.close()
        print("Connection closed!")
