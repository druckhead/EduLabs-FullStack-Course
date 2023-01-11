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
GROUP BY r1.route_num, r2.weekday;

-- display route with most rides
SELECT r1.route_num,
    COUNT(r2.id) AS amnt_ride_id
FROM routes r1
    LEFT JOIN rides r2 ON r1.id = r2.route_id
GROUP BY r1.route_num
ORDER BY COUNT(r2.id) DESC
LIMIT 1;

-- get the weekday that has most rides for route 200
-- Get all the routes that have stops in Haifa Matam
-- Get driver names and amount of routes they drove in the last year
-- Display driver names and total time they drove. Note, you should not take into account canceled rides. 
-- Get all the driver names who drive on route 100
-- Get all the routes which rides last more than 1 hour
-- Display driver names, and amount of delays for each in the rides they drove