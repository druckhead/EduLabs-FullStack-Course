CREATE TABLE customers (
    id serial PRIMARY KEY,
    passport_num varchar(9) NOT NULL,
    name varchar(32) NOT NULL,
    address varchar(50) NOT NULL
);

CREATE TABLE accounts (
    id serial PRIMARY KEY,
    acc_num int UNIQUE NOT NULL,
    max_limit bigint NOT NULL DEFAULT 0,
    balance bigint NOT NULL DEFAULT 0
);

CREATE TABLE customer_accounts (
    id serial PRIMARY KEY,
    customer_id int NOT NULL,
    account_id int NOT NULL,
    CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers (id),
    CONSTRAINT fk_account_id FOREIGN KEY (account_id) REFERENCES accounts (id)
);

CREATE TABLE transactions (
    id serial PRIMARY KEY,
    transaction_type varchar(8) NOT NULL,
    ts time NOT NULL,
    receiver int,
    sender int,
    amount int NOT NULL,
    initiated_by int NOT NULL,
    CONSTRAINT fk_receiver FOREIGN KEY (receiver) REFERENCES accounts (id),
    CONSTRAINT fk_sender FOREIGN KEY (sender) REFERENCES accounts (id),
    CONSTRAINT fk_initiated FOREIGN KEY (initiated_by) REFERENCES customers (id)
);