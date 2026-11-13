-- 1 Revenue and profit by product
SELECT p.product_name, SUM(s.quantity*s.unit_price*(1-s.discount_rate)) revenue, SUM(s.quantity*(s.unit_price*(1-s.discount_rate)-s.unit_cost)) profit FROM sales s JOIN products p USING(product_id) GROUP BY p.product_name ORDER BY revenue DESC;
-- 2 Monthly sales
SELECT substr(order_date,1,7) month, SUM(quantity*unit_price*(1-discount_rate)) revenue FROM sales GROUP BY month ORDER BY month;
-- 3 Performance by region
SELECT r.region, COUNT(*) orders, SUM(s.quantity*s.unit_price*(1-s.discount_rate)) revenue FROM sales s JOIN regions r USING(region_id) GROUP BY r.region ORDER BY revenue DESC;
-- 4 Category summary
SELECT p.category, SUM(s.quantity) units, SUM(s.quantity*s.unit_price*(1-s.discount_rate)) revenue FROM sales s JOIN products p USING(product_id) GROUP BY p.category ORDER BY revenue DESC;
-- 5 Payment methods
SELECT payment_method, COUNT(*) orders FROM sales GROUP BY payment_method ORDER BY orders DESC;
-- 6 Channel revenue
SELECT sales_channel, SUM(quantity*unit_price*(1-discount_rate)) revenue FROM sales GROUP BY sales_channel ORDER BY revenue DESC;
-- 7 Product margin with HAVING
SELECT p.product_name, ROUND(100.0*SUM(s.quantity*(s.unit_price*(1-s.discount_rate)-s.unit_cost))/NULLIF(SUM(s.quantity*s.unit_price*(1-s.discount_rate)),0),2) margin_pct FROM sales s JOIN products p USING(product_id) GROUP BY p.product_id HAVING SUM(s.quantity)>20 ORDER BY margin_pct DESC;
-- 8 CASE WHEN discount bands
SELECT CASE WHEN discount_rate=0 THEN 'No discount' WHEN discount_rate<=0.1 THEN 'Up to 10%' ELSE 'Over 10%' END band, COUNT(*) orders FROM sales GROUP BY band;
-- 9 Average order size
SELECT AVG(quantity) average_units, AVG(unit_price) average_unit_price FROM sales;
-- 10 Annual performance
SELECT substr(order_date,1,4) year, SUM(quantity*unit_price*(1-discount_rate)) revenue FROM sales GROUP BY year ORDER BY year;
