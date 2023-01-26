# SELECT name, city, SUM(o.amount) AS totalSum
# FROM orders o JOIN customers c
# ON o.customer_id = c.id
# WHERE amount>=100 AND amount<=3500
# GROUP BY c.name, c.city
# ORDER BY c.city;