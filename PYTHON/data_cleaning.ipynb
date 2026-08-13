{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "467fb9a1-db3d-49f2-8312-2f41d47db47c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "engine = create_engine(\"mysql+pymysql://root:1234@localhost/inventory_capstone\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "3c24b479-89ce-48aa-b74a-485e84c348bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "categories = pd.read_csv(\"C:\\\\Users\\\\ASUS\\\\Downloads\\\\inventory_management\\\\categories.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ef3c3101-5153-46c0-b8b3-d69d537e5865",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "category_id      object\n",
      "category_name    object\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(categories.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "98dd4767-a437-44a0-8b89-7e7bf1a3952a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "category_id      0\n",
       "category_name    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "categories.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2f264a0a-d526-437e-aaf5-dd1dde0327e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "categories.to_sql(\"categories\", engine, if_exists=\"replace\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "485d9fc5-2038-4351-86fd-c33b005f38af",
   "metadata": {},
   "outputs": [],
   "source": [
    "suppliers = pd.read_csv(\"C:\\\\Users\\\\ASUS\\\\Downloads\\\\inventory_management\\\\suppliers.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "bd52e4b1-5b51-4a8e-9f9f-3a35089fec3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "supplier_id        object\n",
      "supplier_name      object\n",
      "city               object\n",
      "lead_time_days      int64\n",
      "rating            float64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(suppliers.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "065d2c35-b58e-45d0-9a95-9c6c56e33e37",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "supplier_id        0\n",
       "supplier_name      0\n",
       "city               0\n",
       "lead_time_days     0\n",
       "rating            16\n",
       "dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "suppliers.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "dd3fe609-38ca-4edb-b586-8533a60d4921",
   "metadata": {},
   "outputs": [],
   "source": [
    "suppliers[\"rating\"] = suppliers[\"rating\"].fillna(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0d55988f-c984-471d-908a-77689c08e691",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "suppliers.to_sql(\"suppliers\", engine, if_exists=\"replace\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f3799393-8477-4707-be7d-372e1cb12f5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "products = pd.read_csv(\"C:\\\\Users\\\\ASUS\\\\Downloads\\\\inventory_management\\\\products.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3cd80ae8-47b7-4f91-9f9a-4e3e797fb238",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "product_id          object\n",
      "product_name        object\n",
      "category_id         object\n",
      "supplier_id         object\n",
      "unit_price         float64\n",
      "reorder_level        int64\n",
      "shelf_life_days    float64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(products.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "341b6c83-f3d4-45d5-b4d7-d607e2a86169",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "product_id           0\n",
       "product_name         0\n",
       "category_id          0\n",
       "supplier_id          0\n",
       "unit_price           0\n",
       "reorder_level        0\n",
       "shelf_life_days    400\n",
       "dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "products.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "2f36e999-3b11-4347-bd27-48acf3826457",
   "metadata": {},
   "outputs": [],
   "source": [
    "shelf_life_clean = {\n",
    "    \"CAT_002\": 151,\n",
    "    \"CAT_003\": 183,\n",
    "    \"CAT_004\": 272,\n",
    "    \"CAT_006\": 640,\n",
    "    \"CAT_007\": 461,\n",
    "    \"CAT_008\": 657,\n",
    "    \"CAT_012\": 108,\n",
    "    \"CAT_013\": 355,\n",
    "    \"CAT_014\": 456,\n",
    "    \"CAT_015\": 225,\n",
    "    \"CAT_016\": 363,\n",
    "    \"CAT_017\": 235,\n",
    "    \"CAT_018\": 466,\n",
    "    \"CAT_019\": 1194,\n",
    "    \"CAT_020\": 928\n",
    "}\n",
    "\n",
    "products[\"shelf_life_days\"] = products.apply(\n",
    "    lambda row: shelf_life_clean.get(row[\"category_id\"], row[\"shelf_life_days\"])\n",
    "    if pd.isnull(row[\"shelf_life_days\"])\n",
    "    else row[\"shelf_life_days\"],\n",
    "    axis=1\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "dea6eacf-fa27-41a5-a008-02825da64898",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "product_id          object\n",
      "product_name        object\n",
      "category_id         object\n",
      "supplier_id         object\n",
      "unit_price         float64\n",
      "reorder_level        int64\n",
      "shelf_life_days      int64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(products.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "e3631b61-9c82-466d-87de-aec8d3776428",
   "metadata": {},
   "outputs": [],
   "source": [
    "products[\"shelf_life_days\"] = products[\"shelf_life_days\"].round().astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "d36d8d86-a3cf-401f-b077-899c99f12308",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5000"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "products.to_sql(\"products\", engine, if_exists=\"replace\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "22a2b1ac-f565-45a0-b717-2dbc9b680ad5",
   "metadata": {},
   "outputs": [],
   "source": [
    "inventory = pd.read_csv(\"C:\\\\Users\\\\ASUS\\\\Downloads\\\\inventory_management\\\\inventory.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "95d83a95-a9e3-4203-9188-73457603c416",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "inventory_id       0\n",
       "product_id         0\n",
       "warehouse_id       0\n",
       "stock_in_hand      0\n",
       "damaged_units    800\n",
       "last_updated     800\n",
       "dtype: int64"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventory.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "e0e76b66-9835-4dd9-aa3e-7f8b11a895dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inventory_id             object\n",
      "product_id               object\n",
      "warehouse_id             object\n",
      "stock_in_hand             int64\n",
      "damaged_units           float64\n",
      "last_updated     datetime64[ns]\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(inventory.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "93644ede-ed4f-4534-8b27-773a82a44f6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "inventory['last_updated'] = pd.to_datetime(inventory['last_updated'],errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "c6d20af5-ca66-4a31-a5d3-60d7c2dfb7f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "inventory['damaged_units'] = inventory['damaged_units'].fillna(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "b14d92f5-4199-470a-bb69-0f6dfa9c6a6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "inventory['last_updated'] = inventory['last_updated'].fillna(purchase_orders['received_date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "d9bc299b-7c42-4f6b-ab99-46e14991c150",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "inventory_id     0\n",
       "product_id       0\n",
       "warehouse_id     0\n",
       "stock_in_hand    0\n",
       "damaged_units    0\n",
       "last_updated     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventory.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "2d2b9b67-6dcc-44be-9407-e3a7f0e84ee1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8000"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventory.to_sql(\"inventory\", engine, if_exists=\"replace\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "0b3e9c00-1838-49cd-8896-d48978333941",
   "metadata": {},
   "outputs": [],
   "source": [
    "purchase_orders = pd.read_csv(\"C:\\\\Users\\\\ASUS\\\\Downloads\\\\inventory_management\\\\purchase_orders.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "3373a4d6-dd10-442a-9e36-9aa4d0133bb6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "po_id               0\n",
       "product_id          0\n",
       "supplier_id         0\n",
       "warehouse_id        0\n",
       "order_date          0\n",
       "expected_date       0\n",
       "received_date    1440\n",
       "order_qty           0\n",
       "received_qty     1440\n",
       "dtype: int64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "purchase_orders.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "d0a65d14-452e-4c36-8d6d-169fafcf1c9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "po_id                    object\n",
      "product_id               object\n",
      "supplier_id              object\n",
      "warehouse_id             object\n",
      "order_date       datetime64[ns]\n",
      "expected_date    datetime64[ns]\n",
      "received_date    datetime64[ns]\n",
      "order_qty                 int64\n",
      "received_qty            float64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(purchase_orders.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "5bc95042-40a8-40a3-afbb-d93af2c8e195",
   "metadata": {},
   "outputs": [],
   "source": [
    "purchase_orders[\"received_date\"] = pd.to_datetime( purchase_orders[\"received_date\"],errors=\"coerce\")\n",
    "purchase_orders[\"order_date\"] = pd.to_datetime( purchase_orders[\"order_date\"],errors=\"coerce\")\n",
    "purchase_orders[\"expected_date\"] = pd.to_datetime( purchase_orders[\"expected_date\"],errors=\"coerce\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "45f72a40-0d17-4e6f-9a01-74ba63edee8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "purchase_orders[\"received_date\"] = purchase_orders[\"received_date\"].fillna(purchase_orders[\"expected_date\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "6ce6b5b8-16b4-44f3-8525-579925cdd918",
   "metadata": {},
   "outputs": [],
   "source": [
    "purchase_orders[\"received_qty\"] = purchase_orders[\"received_qty\"].fillna(purchase_orders[\"order_qty\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "58eb085b-50b5-4f1e-a6f2-5d0081e87476",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "po_id            0\n",
       "product_id       0\n",
       "supplier_id      0\n",
       "warehouse_id     0\n",
       "order_date       0\n",
       "expected_date    0\n",
       "received_date    0\n",
       "order_qty        0\n",
       "received_qty     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "purchase_orders.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "8007453d-7a87-48d8-abf0-485f36ce1f03",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12000"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "purchase_orders.to_sql(\"purchase_orders\", engine, if_exists=\"replace\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "2c82e538-dbfd-4673-872a-d0fe16c5dbe7",
   "metadata": {},
   "outputs": [],
   "source": [
    "sales_transactions = pd.read_csv(\"C:\\\\Users\\\\ASUS\\\\Downloads\\\\inventory_management\\\\sales_transactions.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "1c3427fe-c6a8-4e96-9b2c-e05280733439",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "sale_id             0\n",
       "product_id          0\n",
       "warehouse_id        0\n",
       "sale_date           0\n",
       "quantity_sold       0\n",
       "sales_amount     1976\n",
       "dtype: int64"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sales_transactions.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "29ee975c-5d56-4f71-8383-2b9815f53f29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sale_id           object\n",
      "product_id        object\n",
      "warehouse_id      object\n",
      "sale_date         object\n",
      "quantity_sold      int64\n",
      "sales_amount     float64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(sales_transactions.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "1823909f-06c3-4b4b-8e18-f609dfa48f6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "price_map = products.set_index(\"product_id\")[\"unit_price\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "f7c3903a-7ee4-47e6-bba1-3dd8b0b501a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "sales_transactions[\"unit_price\"] = sales_transactions[\"product_id\"].map(price_map)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "beaab6cb-e383-4a98-98b4-1a5822ca6f41",
   "metadata": {},
   "outputs": [],
   "source": [
    "sales_transactions[\"sales_amount\"] = sales_transactions[\"sales_amount\"].fillna(\n",
    "    sales_transactions[\"quantity_sold\"] * sales_transactions[\"unit_price\"]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "62bb41ec-be76-4fb7-99be-76113035c055",
   "metadata": {},
   "outputs": [],
   "source": [
    "sales_transactions.drop(columns=[\"unit_price\"], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "761d6fb6-e5f3-4249-8d68-e40571301176",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sales_transactions[\"sales_amount\"].isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "0c62cc7b-4b17-4974-918f-bc87f40e1c76",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24700"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sales_transactions.to_sql(\"sales_transactions\", engine, if_exists=\"replace\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "4a89d45e-9c74-4174-b1bc-397eb1db7749",
   "metadata": {},
   "outputs": [],
   "source": [
    "warehouses = pd.read_csv(\"C:\\\\Users\\\\ASUS\\\\Downloads\\\\inventory_management\\\\warehouses.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "4ab8b061-7d13-4cc8-93f8-da5dfa0053e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "warehouse_id      0\n",
       "warehouse_name    0\n",
       "city              0\n",
       "capacity          0\n",
       "opening_date      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "warehouses.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "59fc6ceb-5902-4632-b8b4-7d20914897b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "80"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "warehouses.to_sql(\"warehouses\", engine, if_exists=\"replace\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f7769b8-0c7e-4c9a-9559-bfd0ad70fa70",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8487102f-c270-4afb-99e8-d0d86ee12204",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbb0bbb0-bef5-4478-af76-f1da45c63279",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
