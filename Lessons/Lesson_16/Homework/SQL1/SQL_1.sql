-- Queries:

-- Get all the data from superstore_data table (all the rows and all the columns)
SELECT
    *
FROM
    superstore_data;

-- Get the amount of rows (records) in the superstore_data table
SELECT
	count(*)
FROM
	superstore_data;
	
-- Get first 10 rows from the superstore_data table
SELECT
	*
FROM
	superstore_data
LIMIT 10;

-- Get rows from 20 to 45 from the table
SELECT
	*
FROM
	superstore_data
LIMIT 25
OFFSET 19;

-- Get only id, year_birth, and marital_status columns for the 20 first rows of the table.
SELECT
	id,
	year_birth,
	marital_status
FROM
	superstore_data
LIMIT 20;

-- Get ids of the customers who spent more than $1000 on wine in the past 2 years
SELECT
	id
FROM
	superstore_data
WHERE
	mntwines > 1000;

-- Get the age and the marital status of the customers who spent less than $500 on fish products, and more than $500 on meat products in the past 2 years.
SELECT
	date_part('year', (SELECT current_timestamp)) - year_birth AS customer_age,
	marital_status
FROM
	superstore_data sd
WHERE
	mntfishproducts < 500
	AND mntmeatproducts > 500;
	
-- Get the amount of customers who accepted the offer
SELECT
	count(response) AS num_accepted_offer
FROM
	superstore_data sd
WHERE
	response = 1;

-- Get all the possible Education values that exist in the table. Sort them alphabetically
SELECT
	DISTINCT education
FROM
	superstore_data sd
ORDER BY
	education;
	
-- Get the data for the youngest customer(s)
SELECT
    *
FROM
    superstore_data sd
WHERE
    year_birth = (
        SELECT
            max(year_birth)
        FROM
            superstore_data sd2
    );
	
-- Get id, age, and marital status of the oldest customers
SELECT
    id,
    date_part('year', (SELECT current_timestamp)) - year_birth AS customer_age,
    marital_status
FROM
    superstore_data sd
WHERE
    year_birth = (
        SELECT
            min(year_birth)
        FROM
            superstore_data sd2
    );

-- Get the average income of the customers who complained in the past 2 years
SELECT
	round(avg(income), 2) AS avg_income_of_complains
FROM
	superstore_data sd
WHERE
	complain = 1;

-- Get the total number of kids of all the customers
SELECT
    count(kidhome + teenhome) AS num_kids
FROM
    superstore_data sd;

-- Get the id, income, and age, and marital status of the customers that made more purchases in web rather than in store
SELECT
    id,
    income,
    date_part('year', (SELECT current_timestamp)) - year_birth AS customer_age,
    marital_status
FROM
    superstore_data sd
WHERE
    numwebpurchases > numstorepurchases;

-- Get the ids and total number of children (kids and teens) of the customers who made a purchase in the past 30 days
SELECT
    id,
    (kidhome + teenhome) AS num_kids_home
FROM
    superstore_data sd
WHERE
    recency <= 30;

-- Get the amount of customers who did not make any purchases of meat or fish in the past 2 years
SELECT
    count(*) AS num_no_meat_or_fish
FROM
    superstore_data sd
WHERE
    mntmeatproducts = 0
    OR mntfishproducts = 0;

-- Get all the details about the customer(s) who spent the maximum amount on gold products in the past 2 years
SELECT
	*
FROM
	superstore_data sd
WHERE
	mntgoldprods = (
		SELECT
			max(mntgoldprods)
		FROM
			superstore_data sd2
	);

-- Get ids and age of the customers who are between 20 and 40 years old, sort them from the oldest to the youngest
SELECT
	id,
	date_part('year', (SELECT current_timestamp)) - year_birth AS customer_age
FROM
	superstore_data sd
WHERE
	date_part('year', (SELECT current_timestamp)) - year_birth BETWEEN 20 AND 40
ORDER BY
	date_part('year', (SELECT current_timestamp)) - year_birth DESC;

-- Get all the unique birth years of the customers
SELECT
	year_birth
FROM
	superstore_data sd;

-- Get top 10 customers who spent the biggest amount of money to buy sweets in the past 2 years
SELECT
	*
FROM
	superstore_data sd
ORDER BY
	mntsweetproducts DESC
LIMIT 10;

-- With group by:

-- Get total amount of customers for each marital status
SELECT
	marital_status,
	count(marital_status) AS amt_status
FROM
	superstore_data sd
GROUP BY
	marital_status;

-- Get total purchases of sweets and wine per each education status
SELECT
	education, 
	sum(mntsweetproducts) AS num_sweets,
	sum(mntwines) AS num_wines,
	sum(mntsweetproducts + mntwines) AS num_sweets_and_wine
FROM
	superstore_data sd
GROUP BY
	education;

-- Get the maximum and the minimum age of customers with the same marital status and education ordered by education, and then minimum age
SELECT
	education,
	marital_status,
	min(date_part('year', (SELECT current_timestamp)) - year_birth) AS min_customer_age,
	max(date_part('year', (SELECT current_timestamp)) - year_birth) AS max_customer_age
FROM
	superstore_data sd
GROUP BY
	education,
	marital_status
ORDER BY
	education,
	min(date_part('year', (SELECT current_timestamp)) - year_birth);

-- Get amount of customers of each age that have accepted the offer and have not complained in the past 2 years
SELECT
	 date_part('year', (SELECT current_timestamp)) - year_birth AS min_customer_age,
	 response,
	 complain
FROM superstore_data sd
WHERE response = 1 AND complain = 0;

-- Get the youngest customer for each education level (id,  education, age)
SELECT
	DISTINCT ON
	(education) education,
	id,
	min(date_part('year', (SELECT current_timestamp)) - year_birth) AS min_customer_age
FROM
	superstore_data sd
GROUP BY
	education,
	id
ORDER BY
	education,
	min(date_part('year', (SELECT current_timestamp)) - year_birth);

-- Get average amount of purchases for each product type (fish, meat, sweets, wine, gold) for groups of customers with the same amounts of children at home (kids and teens)
SELECT
	kidhome + teenhome AS kids_home,
	avg(mntfishproducts) AS avg_amnt_fish,
	avg(mntmeatproducts) AS avg_amnt_meat,
	avg(mntsweetproducts) AS avg_amnt_sweets,
	avg(mntwines) AS avg_amnt_wines,
	avg(mntgoldprods) AS avg_amnt_gold
FROM
	superstore_data sd
GROUP BY
	kidhome + teenhome;

-- Get the youngest customer id, and birth year for every possible number of teens at home that exist in the table
SELECT
	DISTINCT ON (teenhome) teenhome,
	id,
	year_birth
FROM
	superstore_data sd
GROUP BY
	teenhome,
	id,
	year_birth
ORDER BY teenhome, min(date_part('year', (SELECT current_timestamp)) - year_birth);

-- Get total number of customers who accepted and did not accept the offer
SELECT
	count(sd.response) FILTER (WHERE response = 1) AS num_accepted,
	count(sd.response) FILTER (WHERE response = 0) AS num_not_accepted
FROM
	superstore_data sd;

-- Get average number of kids and average number of teens for customers with the same marital status (per status)
SELECT
	marital_status,
	round(avg(kidhome), 2) AS avg_kidhome,
	round(avg(teenhome), 2) AS avg_teenhome
FROM
	superstore_data sd
GROUP BY
	marital_status;

-- Get the minimum, maximum, and average income for every education level of customers
SELECT
	sd.education,
	min(sd.income) AS min_income,
	max(sd.income) AS max_income,
	round(avg(sd.income), 2) AS avg_income
FROM
	superstore_data sd
GROUP BY
	education;
