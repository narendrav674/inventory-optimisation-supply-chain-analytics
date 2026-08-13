CREATE DATABASE inventory_capstone;

SHOW DATABASES;

USE inventory_capstone;

### 1. 1. Data Validation after Loading ------
## 1. Check Tables--
SHOW TABLES;

## 2. Count rows in each table--
SELECT COUNT(*) AS total_rows FROM categories;
SELECT COUNT(*) AS total_rows FROM suppliers;
SELECT COUNT(*) AS total_rows FROM warehouses;
SELECT COUNT(*) AS total_rows FROM products;
SELECT COUNT(*) AS total_rows FROM inventory;
SELECT COUNT(*) AS total_rows FROM purchase_orders;
SELECT COUNT(*) AS total_rows FROM sales_transactions;

## 3. Preview data--
SELECT * FROM products LIMIT 10;
SELECT * FROM inventory LIMIT 10;
SELECT * FROM purchase_orders LIMIT 10;
SELECT * FROM sales_transactions LIMIT 10;

### 2. Data Transformation Queries -----
## 1. Create stock status--
SELECT
    i.inventory_id,
    i.product_id,
    p.product_name,
    i.warehouse_id,
    i.stock_in_hand,
    p.reorder_level,
    CASE
        WHEN i.stock_in_hand = 0 THEN 'Out of Stock'
        WHEN i.stock_in_hand < p.reorder_level THEN 'Low Stock'
        ELSE 'Healthy'
    END AS stock_status
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id;
    
## 2. Create order delivery status--
SELECT
    po_id,
    product_id,
    supplier_id,
    warehouse_id,
    order_date,
    expected_date,
    received_date,
    CASE
        WHEN received_date > expected_date THEN 'Delayed'
        ELSE 'On Time'
    END AS delivery_status
FROM purchase_orders;

## 3. Calculate inventory value--
SELECT
    i.inventory_id,
    i.product_id,
    p.product_name,
    i.warehouse_id,
    i.stock_in_hand,
    p.unit_price,
    (i.stock_in_hand * p.unit_price) AS inventory_value
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id;
    
## 4. Calculate order fulfillment percentage--
SELECT
    po_id,
    product_id,
    supplier_id,
    order_qty,
    received_qty,
    ROUND((received_qty / order_qty) * 100, 2) AS fulfillment_percent
FROM purchase_orders;

### 3. KPI / Business Analysis Queries--
## 1. Total inventory value--
SELECT
    ROUND(SUM(i.stock_in_hand * p.unit_price), 2) AS total_inventory_value
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id;
    
##2. Total Revenue--
SELECT
    ROUND(SUM(sales_amount), 2) AS total_revenue
FROM sales_transactions;

## 3. Total quantity sold--
SELECT
    SUM(quantity_sold) AS total_quantity_sold
FROM sales_transactions;

## 4. Total Products--
SELECT
    COUNT(DISTINCT product_id) AS total_products
FROM products;

## 5. Low stock products count--
SELECT
    COUNT(*) AS low_stock_count
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id
WHERE i.stock_in_hand < p.reorder_level;

## 6. Out-of-stock products count--
SELECT
    COUNT(*) AS out_of_stock_count
FROM inventory
WHERE stock_in_hand = 0;

## 7. Damaged units Total--
SELECT
    SUM(damaged_units) AS total_damaged_units
FROM inventory;

## 8. Supplier delay percentage--
SELECT
    ROUND(
        SUM(CASE WHEN received_date > expected_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS supplier_delay_percent
FROM purchase_orders;


### 4. Advanced Insight Queries----
## 1. Products below reorder level--
SELECT
    p.product_id,
    p.product_name,
    i.stock_in_hand,
    p.reorder_level
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id
WHERE i.stock_in_hand < p.reorder_level
ORDER BY i.stock_in_hand ASC;

## 2. Products needing urgent reorder--
SELECT
    p.product_id,
    p.product_name,
    i.stock_in_hand,
    p.reorder_level,
    (p.reorder_level - i.stock_in_hand) AS shortage_qty
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id
WHERE i.stock_in_hand < p.reorder_level
ORDER BY shortage_qty DESC;

## 3. Overstocked Products--
SELECT
    p.product_id,
    p.product_name,
    i.stock_in_hand,
    p.reorder_level
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id
WHERE i.stock_in_hand > p.reorder_level * 3
ORDER BY i.stock_in_hand DESC;

## 4. Category-wise inventory value--
SELECT
    c.category_name,
    ROUND(SUM(i.stock_in_hand * p.unit_price), 2) AS inventory_value
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id
JOIN categories c
    ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY inventory_value DESC;

## 5. Category-wise revenue--
SELECT
    c.category_name,
    ROUND(SUM(s.sales_amount), 2) AS total_revenue
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
JOIN categories c
    ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_revenue DESC;

## 6. Top 10 selling products by revenue--
SELECT
    p.product_name,
    SUM(s.quantity_sold) AS total_qty_sold,
    ROUND(SUM(s.sales_amount), 2) AS total_revenue
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC
LIMIT 10;

## 7. Top 10 products by quantity sold--
SELECT
    p.product_name,
    SUM(s.quantity_sold) AS total_qty_sold
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_qty_sold DESC
LIMIT 10;

## 8. Monthly revenue trend--
SELECT
    DATE_FORMAT(sale_date, '%Y-%m') AS month,
    ROUND(SUM(sales_amount), 2) AS monthly_revenue
FROM sales_transactions
GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
ORDER BY month;

## 9. Monthly quantity sold trend--
SELECT
    DATE_FORMAT(sale_date, '%Y-%m') AS month,
    SUM(quantity_sold) AS monthly_quantity_sold
FROM sales_transactions
GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
ORDER BY month;

## 10. Supplier-wise delayed orders--
SELECT
    s.supplier_name,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN p.received_date > p.expected_date THEN 1 ELSE 0 END) AS delayed_orders
FROM purchase_orders p
JOIN suppliers s
    ON p.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY delayed_orders DESC;

## 11. Supplier-wise delay percentage--
SELECT
    s.supplier_name,
    COUNT(*) AS total_orders,
    ROUND(
        SUM(CASE WHEN p.received_date > p.expected_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS delay_percent
FROM purchase_orders p
JOIN suppliers s
    ON p.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY delay_percent DESC;

## 12. Supplier fulfillment percentage--
SELECT
    s.supplier_name,
    SUM(p.order_qty) AS total_order_qty,
    SUM(p.received_qty) AS total_received_qty,
    ROUND(SUM(p.received_qty) * 100.0 / SUM(p.order_qty), 2) AS fulfillment_percent
FROM purchase_orders p
JOIN suppliers s
    ON p.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY fulfillment_percent DESC;

## 13. Warehouse-wise stock units--
SELECT
    w.warehouse_name,
    w.city,
    SUM(i.stock_in_hand) AS total_stock_units
FROM inventory i
JOIN warehouses w
    ON i.warehouse_id = w.warehouse_id
GROUP BY w.warehouse_name, w.city
ORDER BY total_stock_units DESC;

## 14. Warehouse-wise inventory value--
SELECT
    w.warehouse_name,
    w.city,
    ROUND(SUM(i.stock_in_hand * p.unit_price), 2) AS inventory_value
FROM inventory i
JOIN warehouses w
    ON i.warehouse_id = w.warehouse_id
JOIN products p
    ON i.product_id = p.product_id
GROUP BY w.warehouse_name, w.city
ORDER BY inventory_value DESC;

## 15. Warehouse-wise damaged stock--
SELECT
    w.warehouse_name,
    SUM(i.damaged_units) AS total_damaged_units
FROM inventory i
JOIN warehouses w
    ON i.warehouse_id = w.warehouse_id
GROUP BY w.warehouse_name
ORDER BY total_damaged_units DESC;

## 16. City-wise revenue--
SELECT
    w.city,
    ROUND(SUM(s.sales_amount), 2) AS total_revenue
FROM sales_transactions s
JOIN warehouses w
    ON s.warehouse_id = w.warehouse_id
GROUP BY w.city
ORDER BY total_revenue DESC;

## 17. Average supplier rating by city--
SELECT
    city,
    ROUND(AVG(rating), 2) AS avg_supplier_rating
FROM suppliers
GROUP BY city
ORDER BY avg_supplier_rating DESC;



## 18. Dead stock products (no sales)---
SELECT
    p.product_id,
    p.product_name
FROM products p
LEFT JOIN sales_transactions s
    ON p.product_id = s.product_id
WHERE s.product_id IS NULL;

## 19. Products not sold in last 90 days--
SELECT
    p.product_id,
    p.product_name
FROM products p
WHERE p.product_id NOT IN (
    SELECT DISTINCT product_id
    FROM sales_transactions
    WHERE sale_date >= CURDATE() - INTERVAL 90 DAY
);

## 20. Fast-moving products--
SELECT
    p.product_name,
    SUM(s.quantity_sold) AS total_qty_sold
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_qty_sold DESC
LIMIT 20;




