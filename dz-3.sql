SELECT s1.airport_name, s2.airport_name FROM bookings.airports AS s1, (SELECT airport_name, POINT(longitude, latitude) as point FROM bookings.airports) AS s2 ORDER BY (POINT(longitude, latitude) <@> s2.point) DESC LIMIT 1
