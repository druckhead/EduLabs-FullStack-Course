CREATE TABLE public.drivers (
    id serial PRIMARY KEY,
    passport_num varchar(9) UNIQUE NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    driver_address varchar(50) NOT NULL
);

-- create the table for route stops
CREATE TABLE public.stops (
    id serial PRIMARY KEY,
    city varchar(50) NOT NULL,
    name varchar(50) NOT NULL
);

-- create the table for bus routes
CREATE TABLE public.routes (
    id serial PRIMARY KEY,
    route_num int NOT NULL,
    origin_stop_id int NOT NULL,
    destination_stop_id int NOT NULL CONSTRAINT origin_is_diff_dest CHECK (origin_stop_id <> destination_stop_id),
    CONSTRAINT fk_origin_stop_id FOREIGN KEY (origin_stop_id) REFERENCES stops (id),
    CONSTRAINT fk_destination_id FOREIGN KEY (destination_stop_id) REFERENCES stops (id)
);

-- create the table for rides
CREATE TABLE public.rides (
    id serial PRIMARY KEY,
    driver_id int NOT NULL,
    route_id int NOT NULL,
    weekday varchar(3) NOT NULL CHECK (
        weekday IN ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
    ),
    CONSTRAINT fk_driver_id FOREIGN KEY (driver_id) REFERENCES drivers (id) ON DELETE
    SET NULL ON UPDATE CASCADE,
    CONSTRAINT fk_route_id FOREIGN KEY (route_id) REFERENCES routes (id) ON DELETE CASCADE
);

-- create the table for ride stops
CREATE TABLE public.ride_stops (
    id serial PRIMARY KEY,
    arrival_time time NOT NULL,
    departure_time time NOT NULL CONSTRAINT arrival_is_after_departure CHECK (arrival_time > departure_time),
    ride_id int NOT NULL,
    stop_id int NOT NULL,
    stop_ordinal smallint NOT NULL,
    CONSTRAINT fk_ride_id FOREIGN KEY (ride_id) REFERENCES rides (id),
    CONSTRAINT fk_stop_id FOREIGN KEY (stop_id) REFERENCES stops (id)
);

-- create table for service inturruptions
CREATE TABLE public.service_interruptions (
    id serial PRIMARY KEY,
    interruption_type varchar(11) NOT NULL CONSTRAINT is_valid_interruption CHECK (interruption_type IN ('cancelation', 'delay')),
    ride_delay timestamp,
    ride_id int NOT NULL,
    CONSTRAINT fk_ride_id FOREIGN KEY (ride_id) REFERENCES rides (id)
);

-- populate drives table
INSERT INTO drivers (
        passport_num,
        first_name,
        last_name,
        driver_address
    )
VALUES (
        406812631,
        'Kylie',
        'Friese',
        '1485 Homewood Drive'
    );

INSERT INTO drivers (
        passport_num,
        first_name,
        last_name,
        driver_address
    )
VALUES (
        968670164,
        'Berk',
        'Edgeon',
        '84068 Red Cloud Circle'
    );

INSERT INTO drivers (
        passport_num,
        first_name,
        last_name,
        driver_address
    )
VALUES (
        569442114,
        'Seka',
        'Flaverty',
        '5698 Graedel Street'
    );

INSERT INTO drivers (
        passport_num,
        first_name,
        last_name,
        driver_address
    )
VALUES (
        969426134,
        'Melanie',
        'Romushkin',
        '27 Cottonwood Road'
    );

INSERT INTO drivers (
        passport_num,
        first_name,
        last_name,
        driver_address
    )
VALUES (
        156345386,
        'Martainn',
        'Reder',
        '20370 Warrior Street'
    );

-- populate stops table
INSERT INTO stops (city, name)
VALUES ('Bulualto', 'Vidon');

INSERT INTO stops (city, name)
VALUES ('Sibayo', 'Hollow Ridge');

INSERT INTO stops (city, name)
VALUES ('Kebon', 'La Follette');

INSERT INTO stops (city, name)
VALUES ('Caicun', 'Morning');

INSERT INTO stops (city, name)
VALUES ('Chum Phae', 'Springview');

-- populate routes table
INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES (1, 5, 1);

INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES (2, 3, 2);

INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES (3, 4, 3);

INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES (4, 2, 4);

INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES (5, 1, 5);

-- pupulate rides table
INSERT INTO rides (driver_id, route_id, weekday)
VALUES (1, 1, 'sun');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES (2, 2, 'tue');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES (3, 1, 'tue');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES (4, 4, 'wed');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES (5, 1, 'sun');

-- pupulate ride_stops table
INSERT INTO ride_stops (
        arrival_time,
        departure_time,
        ride_id,
        stop_id,
        stop_ordinal
    )
VALUES ('18:43:24', '15:51:30', 1, 1, 1);

INSERT INTO ride_stops (
        arrival_time,
        departure_time,
        ride_id,
        stop_id,
        stop_ordinal
    )
VALUES ('6:37:10', '3:53:15', 2, 2, 2);

INSERT INTO ride_stops (
        arrival_time,
        departure_time,
        ride_id,
        stop_id,
        stop_ordinal
    )
VALUES ('19:34:59', '15:17:23', 3, 3, 3);

INSERT INTO ride_stops (
        arrival_time,
        departure_time,
        ride_id,
        stop_id,
        stop_ordinal
    )
VALUES ('19:25:58', '16:21:50', 4, 4, 4);

INSERT INTO ride_stops (
        arrival_time,
        departure_time,
        ride_id,
        stop_id,
        stop_ordinal
    )
VALUES ('12:46:13', '4:15:07', 5, 5, 5);

-- populate service_interruptions table
INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES ('delay', '2022-12-16 21:06:02', 1);

INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES ('delay', '2022-08-24 20:38:47', 2);

INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES ('cancelation', NULL, 3);

INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES ('delay', '2022-08-26 17:44:33', 4);

INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES ('cancelation', NULL, 5);



-- sdssss
INSERT INTO drivers (passport_num, first_name, last_name, driver_address)
VALUES ('111111111', 'Israel', 'Israeli', 'Tel Aviv');

INSERT INTO drivers (passport_num, first_name, last_name, driver_address)
VALUES ('222222222', 'Moshe', 'Cohen', 'Hod Hasharon');

INSERT INTO drivers (passport_num, first_name, last_name, driver_address)
VALUES ('333333333', 'David', 'Shwimmer', 'Tveriya');

INSERT INTO drivers (passport_num, first_name, last_name, driver_address)
VALUES ('444444444', 'Tali', 'Shani', 'Tel Aviv');

INSERT INTO drivers (passport_num, first_name, last_name, driver_address)
VALUES ('555555555', 'Sagi', 'Shem Tov', 'Tel Aviv');

INSERT INTO stops (city, "name")
VALUES('Tel Aviv', 'Central bus station');

INSERT INTO stops (city, "name")
VALUES('Tel Aviv', 'Alenby');

INSERT INTO stops (city, "name")
VALUES('Tel Aviv', 'University');

INSERT INTO stops (city, "name")
VALUES('Haifa', 'Matam');

INSERT INTO stops (city, "name")
VALUES('Haifa', 'Technion');

INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES(4, 1, 100);

INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES(10, 1, 200);

INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES(5, 4, 300);

INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES(5, 3, 400);

INSERT INTO routes (destination_stop_id, origin_stop_id, route_num)
VALUES(2, 3, 500);

INSERT INTO rides (driver_id, route_id, weekday)
VALUES(6, 1, 'sun');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES(2, 4, 'tue');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES(1, 5, 'tue');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES(4, 3, 'thu');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES(1, 6, 'sun');

-- T
INSERT INTO ride_stops (
        arrival_time,
        departure_time,
        ride_id,
        stop_id,
        stop_ordinal
    )
VALUES('10:31', '10:30', 1, 9, 1);

INSERT INTO ride_stops (
        arrival_time,
        departure_time,
        ride_id,
        stop_id,
        stop_ordinal
    )
VALUES('10:55', '10:50', 1, 3, 2);

INSERT INTO ride_stops (
        arrival_time,
        departure_time,
        ride_id,
        stop_id,
        stop_ordinal
    )
VALUES('11:32', '11:30', 1, 5, 3);

INSERT INTO ride_stops (
        arrival_time,
        departure_time,
        ride_id,
        stop_id,
        stop_ordinal
    )
VALUES('12:50', '11:50', 1, 9, 4);

INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES('cancelation', '2023-01-08 04:05:06', 1);

INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES('delay', '2023-01-09 17:05:00', 2);

INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES('delay', '2023-01-06 14:00:00', 1);

INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES('cancelation', '2023-01-05 09:05:10', 3);

INSERT INTO service_interruptions (interruption_type, ride_delay, ride_id)
VALUES('cancelation', '2023-01-08 12:00:00', 1);

-- gfuyfiytt
INSERT INTO rides (driver_id, route_id, weekday)
VALUES (4, 7, 'wed');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES (1, 7, 'sun');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES (3, 7, 'thu');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES (10, 7, 'sun');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES (9, 7, 'sun');

INSERT INTO rides (driver_id, route_id, weekday)
VALUES (4, 7, 'wed');