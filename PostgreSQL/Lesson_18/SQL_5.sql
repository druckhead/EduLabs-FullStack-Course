-- Display amount of rides for each route
SELECT routes.id,
    COUNT(*) AS num_rides
FROM routes
    LEFT JOIN rides ON rides.route_id = routes.id
GROUP BY routes.id;

-- display amount of rides for each route and each weekday
SELECT r1.route_num AS route_id,
    r2.weekday,
    COUNT(r2.id) AS amnt_ride_id
FROM routes r1
    LEFT JOIN rides r2 ON r1.id = r2.route_id
GROUP BY r1.route_num,
    r2.weekday;

-- display route with most rides
SELECT r1.route_num,
    COUNT(r2.id) AS amnt_ride_id
FROM routes r1
    LEFT JOIN rides r2 ON r1.id = r2.route_id
GROUP BY r1.route_num
ORDER BY COUNT(r2.id) DESC
LIMIT 1;

-- get the weekday that has most rides for route 200
SELECT r2.weekday,
    r1.route_num AS route_id,
    COUNT(r2.id) AS amnt_ride_id
FROM routes r1
    LEFT JOIN rides r2 ON r1.id = r2.route_id
WHERE r1.route_num = 200
GROUP BY r1.route_num,
    r2.weekday
ORDER BY COUNT(r2.id) DESC
LIMIT 1;

-- Get all the routes that have stops in Haifa Matam
SELECT *
FROM ride_stops rs
WHERE rs.stop_id = (
        SELECT s.id
        FROM stops s
        GROUP BY s.id
        HAVING s.city = 'Haifa'
            AND s.name = 'Matam'
    );

-- Get driver names and amount of routes they drove in the last year
SELECT d.name,
    COUNT(r2.id) AS num_rides
FROM drivers d
    LEFT JOIN rides r1 ON d.id = r1.driver_id
    LEFT JOIN routes r2 ON r1.route_id = r2.id
GROUP BY d.name;

-- Display driver names and total time they drove. Note, you should not take into account canceled rides. 
SELECT d.name,
    sum(r2.arrival_time - r2.departure_time) len_rides
FROM drivers d
    LEFT JOIN rides r1 ON d.id = r1.driver_id
    LEFT JOIN ride_stops r2 ON r1.route_id = r2.id
GROUP BY d.name,
    r2.arrival_time - r2.departure_time;

-- Get all the driver names who drive on route 100
SELECT d.name
FROM drivers d
    LEFT JOIN rides r1 ON r1.driver_id = d.id
    LEFT JOIN routes r2 ON r2.id = r1.route_id
WHERE r2.route_num = 100;

-- Get all the routes which rides last more than 1 hour
SELECT rs1.*
FROM rides r1
    LEFT JOIN routes r2 ON r2.id = r1.route_id
    LEFT JOIN ride_stops rs1 ON rs1.id = r1.id
WHERE (rs1.arrival_time - rs1.arrival_time) > INTERVAL '1' HOUR;

-- Display driver names, and amount of delays for each in the rides they drove
SELECT d.name AS driver_name,
    r1.id AS ride_id,
    COUNT(si1.id) AS amount_of_delays
FROM drivers d
    LEFT JOIN rides r1 ON d.id = r1.driver_id
    LEFT JOIN service_interruptions si1 ON r1.id = si1.ride_id
WHERE si1.interrupt_type = 'delay'
GROUP BY d.name,
    r1.id;