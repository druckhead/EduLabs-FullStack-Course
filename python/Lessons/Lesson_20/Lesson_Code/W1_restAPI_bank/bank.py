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
    if request.method == 'GET':
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

        if page_num is None and results_per_page is None and city is None and name_contains is None:
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
                    curs.execute(sql, (f"%{city}%", f'%{name_contains}%', results_per_page, page_num - 1))
                    result = curs.fetchall()

        if result:
            response = {"data": {"customers": {}}}
            for r in result:
                response["data"]["customers"].update({f"{r[0]}": serialize_customers(r)})
            return jsonify(response)
        else:
            abort(404, description="Resource Not Found")
    
    if request.method == "POST":
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
            return json
        else:
            return "Content-Type not supported!"
        
        new_passport_num = request.form['passport_num']
        new_name = request.form['name']
        return jsonify(new_passport_num, new_name)


@app.route("/api/v1/customers/<int:customer_id>", methods=["GET"])
def customer_data(customer_id: int):
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


@app.route("/api/v1/accounts", methods=["GET"])
def all_accounts():
    if request.args.get("page_num") is None:
        page_num = None
    else:
        page_num = int(request.args.get("page_num"))

    if request.args.get("results_per_page") is None:
        results_per_page = None
    else:
        results_per_page = int(request.args.get("results_per_page"))

    if page_num is None and results_per_page is None:
        # get all customers
        with conn:
            with conn.cursor() as curs:
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


@app.route("/api/v1/accounts/<int:account_id>", methods=["GET"])
def accounts_id(account_id: int):
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


if __name__ == "__main__":
    app.run(debug=True)
