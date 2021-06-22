/*если правильно понял тз*/
SELECT *, RANK() OVER (ORDER BY seat_no) FROM bookings.seats WHERE aircraft_code = '319' AND fare_conditions = 'Economy'
