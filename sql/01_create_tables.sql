PRAGMA foreign_keys=ON;
DROP TABLE IF EXISTS sales; DROP TABLE IF EXISTS products; DROP TABLE IF EXISTS customers; DROP TABLE IF EXISTS regions; DROP TABLE IF EXISTS categories;
CREATE TABLE regions(region_id TEXT PRIMARY KEY, region TEXT NOT NULL, city TEXT NOT NULL);
CREATE TABLE categories(category_id TEXT PRIMARY KEY, category TEXT NOT NULL UNIQUE);
CREATE TABLE products(product_id TEXT PRIMARY KEY, product_name TEXT NOT NULL, category TEXT NOT NULL, category_id TEXT NOT NULL REFERENCES categories(category_id), unit_price REAL NOT NULL CHECK(unit_price>=0), unit_cost REAL NOT NULL CHECK(unit_cost>=0));
CREATE TABLE customers(customer_id TEXT PRIMARY KEY, customer_name TEXT NOT NULL, region_id TEXT NOT NULL REFERENCES regions(region_id));
CREATE TABLE sales(order_id TEXT PRIMARY KEY, order_date TEXT NOT NULL, customer_id TEXT NOT NULL REFERENCES customers(customer_id), product_id TEXT NOT NULL REFERENCES products(product_id), region_id TEXT NOT NULL REFERENCES regions(region_id), quantity INTEGER NOT NULL CHECK(quantity>0), unit_price REAL NOT NULL, unit_cost REAL NOT NULL, discount_rate REAL NOT NULL CHECK(discount_rate BETWEEN 0 AND 0.5), payment_method TEXT NOT NULL, sales_channel TEXT NOT NULL);
CREATE INDEX idx_sales_date ON sales(order_date); CREATE INDEX idx_sales_product ON sales(product_id); CREATE INDEX idx_sales_region ON sales(region_id);
