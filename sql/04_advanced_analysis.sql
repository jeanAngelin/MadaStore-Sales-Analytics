-- 11 CTE: monthly revenue
WITH monthly AS (SELECT substr(order_date,1,7) month, SUM(quantity*unit_price*(1-discount_rate)) revenue FROM sales GROUP BY month) SELECT * FROM monthly ORDER BY month;
-- 12 Window function: monthly rank within year
WITH m AS (SELECT substr(order_date,1,4) year, substr(order_date,6,2) month, SUM(quantity*unit_price*(1-discount_rate)) revenue FROM sales GROUP BY year,month) SELECT *, RANK() OVER(PARTITION BY year ORDER BY revenue DESC) rank_in_year FROM m;
-- 13 Cumulative revenue
WITH m AS (SELECT substr(order_date,1,7) month, SUM(quantity*unit_price*(1-discount_rate)) revenue FROM sales GROUP BY month) SELECT month, revenue, SUM(revenue) OVER(ORDER BY month) cumulative_revenue FROM m;
-- 14 Low performers
SELECT p.product_name, SUM(s.quantity) units, SUM(s.quantity*s.unit_price*(1-s.discount_rate)) revenue FROM sales s JOIN products p USING(product_id) GROUP BY p.product_id ORDER BY revenue ASC LIMIT 10;
-- 15 Customer repeat-purchase distribution
WITH c AS (SELECT customer_id, COUNT(*) orders FROM sales GROUP BY customer_id) SELECT orders, COUNT(*) customers FROM c GROUP BY orders ORDER BY orders;
