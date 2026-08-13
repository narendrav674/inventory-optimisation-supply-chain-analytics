Inventory Management Capstone Dataset
Total rows across 7 tables: 50000

Row counts:
- categories: 20
- suppliers: 200
- warehouses: 80
- products: 5000
- inventory: 8000
- purchase_orders: 12000
- sales_transactions: 24700

Null rates:
- suppliers.rating: 8%
- products.shelf_life_days: 8%
- inventory.damaged_units: 10%
- inventory.last_updated: 10%
- purchase_orders.received_date: 12%
- purchase_orders.received_qty: 12%
- sales_transactions.sales_amount: 8%

Notes:
- IDs use formats like CAT_001, SUP_001, WH_001, PRD_0001, INV_00001, PO_00001, SAL_00001
- Purchase orders with blank received_date / received_qty represent pending deliveries
- Products with blank shelf_life_days are mostly non-perishable items
- Inventory includes low-stock, out-of-stock, normal, and overstock scenarios
