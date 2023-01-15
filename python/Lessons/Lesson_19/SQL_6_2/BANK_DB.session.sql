CREATE TABLE customers(
    id serial PRIMARY KEY,
    passport_num bigint UNIQUE NOT NULL,
    name varchar(128) NOT NULL,
    address varchar(256)
);

CREATE TABLE accounts(
    id serial PRIMARY KEY,
    balance float NOT NULL DEFAULT 0,
    max_limit float NOT NULL DEFAULT 0
);

CREATE TABLE account_owners(
    id serial PRIMARY KEY,
    customer_id int NOT NULL,
    account_id int NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

CREATE TABLE transactions(
    id serial PRIMARY KEY,
    transaction_type varchar(16) NOT NULL,
    ts timestamp NOT NULL,
    initiated_by int NOT NULL,
    FOREIGN KEY (initiated_by) REFERENCES customers(passport_num) ON DELETE CASCADE
);

CREATE TABLE transaction_accounts(
    id serial PRIMARY KEY,
    -- states the role of the account in transaction
    -- for example, when transfering (sender / receiver)
    -- for withdraw/deposit, can be null
    account_role varchar(16),
    transaction_id int NOT NULL,
    account_id int NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES transactions(id) ON DELETE CASCADE,
    FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

INSERT INTO customers (passport_num, "name", address)
VALUES (123456789, 'Brad Pitt', 'California');

INSERT INTO customers (passport_num, "name", address)
VALUES (101010101, 'Angelina Jolie', 'California');

INSERT INTO accounts (max_limit)
VALUES (10000000);

INSERT INTO accounts (balance, max_limit)
VALUES (5000000, 10000000);

INSERT INTO account_owners (customer_id, account_id)
VALUES(2, 2);