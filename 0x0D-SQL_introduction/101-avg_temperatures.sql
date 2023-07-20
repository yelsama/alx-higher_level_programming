-- displays the average temperature (Fahrenheit) by city ordered by temperature
SELECT city, ROUND(AVG(value * 9/5 + 32), 2) AS average_temperature_fahrenheit FROM temperatures GROUP BY city ORDER BY average_temperature_fahrenheit DESC;
