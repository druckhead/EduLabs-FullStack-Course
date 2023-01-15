from pprint import pprint

import psycopg2
from config import get_config


class Bank:
    def __init__(self) -> None:
        pass

    def _passport_exists(self, curs, passport_num) -> bool:
        res = None

        # check passport validity
        query = """
        SELECT c.passport_num
        FROM customers c
        WHERE c.passport_num = %s;
        """
        curs.execute(query, (passport_num,))
        res = curs.fetchone()

        return res[0] == passport_num

    def _accounts_exist(self, curs, from_account, to_account) -> bool:
        res = None

        # check balance validity
        query = """
        SELECT a.id = 1 or a.id = 2
        FROM accounts a
        WHERE a.id = %s or a.id = %s;
        """
        curs.execute(query, (from_account, to_account))
        res = curs.fetchmany(2)

        for a in res:
            if not a[0]:
                return False

        return True

    def _check_balance(self, curs, from_account, amount) -> bool:
        res = None
        
        # check balance validity
        query = """
        SELECT a.balance - %s > -a.max_limit
        FROM customers c
        LEFT JOIN accounts a ON c.id = a.id
        WHERE a.id = %s;
        """
        curs.execute(query, (amount, from_account))
        res = curs.fetchone()

        return res[0]

    def transfer(self, from_account, to_account, amount, initiated_by):
        params = get_config()

        conn = psycopg2.connect(**params)
        try:
            with conn:
                with conn.cursor() as curs:
                    is_valid = self._check_balance(curs, from_account, amount)
                    if not is_valid:
                        raise ValueError(
                            f"Transfering {amount} would put you over your max limit.\n"
                            f"Can NOT continue with transfer..."
                        )

                    accounts_exist = self._accounts_exist(
                        curs, from_account, to_account
                    )
                    if not accounts_exist:
                        raise ValueError(f"One of the accounts does not exist")

                    passport_exists = self._passport_exists(curs, initiated_by)
                    if not passport_exists:
                        raise ValueError(
                            f"Passport: {initiated_by} does not belong to any customer."
                        )

                    query = """
                    INSERT INTO transactions (
                        transaction_type,
                        ts,
                        initiated_by
                    )
                    VALUES (
                        'transfer',
                        date_trunc('second', now()::timestamp),
                        %s
                    );
                    """
                    curs.execute(query, (initiated_by,))

                    query2 = """
                    INSERT INTO transaction_accounts (
                        account_role,
                        transaction_id,
                        account_id
                    )
                    VALUES (
                        'sender',
                        currval(pg_get_serial_sequence('transactions', 'id')),
                        %s
                    );
                    """
                    curs.execute(query2, (from_account,))

                    query3 = """
                    INSERT INTO transaction_accounts (
                        account_role,
                        transaction_id,
                        account_id
                    )
                    VALUES (
                        'receiver',
                        currval(pg_get_serial_sequence('transactions', 'id')),
                        %s
                    );
                    """
                    curs.execute(query3, (to_account,))

                    query4 = """
                    UPDATE accounts
                    SET balance = balance - %s
                    WHERE id=%s;
                    """
                    curs.execute(query4, (amount, from_account))

                    query5 = """
                    UPDATE accounts
                    SET balance = balance + %s
                    WHERE id=%s;
                    """
                    curs.execute(query5, (amount, to_account))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")


if __name__ == "__main__":
    b = Bank()
    # print(b.accounts_exist(1, 2))
    # print(b.check_balance(2, 1000000))
    # print(b.passport_exists(123456789))
    # print(b.passport_exists(101010101))
    print(b.transfer(1, 2, 1, 123456789))
