-- displays the max temperature of each state
SELSECT state, MAX(value) AS max_temp
FROM temperature
GROUP BY state
ORDER BY state;
