#!/usr/bin/env python
# coding: utf-8

# The "techsmart.db" database setup

import sqlite3
import pandas as pd

# The "techsmart.db" database setup function
def setup_database( db_name="techsmart.db" ):
    
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()

            # Creating Employee_Records table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Employee_Records (
                   employee_id INTEGER PRIMARY KEY,
                   role TEXT,
                   store_location TEXT,
                   sales_performance TEXT  -- adapted to the data
                )
            ''')

            # Creating Product_Details table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Product_Details (
                    product_id TEXT PRIMARY KEY,  -- adapted to the data
                    product_name TEXT,
                    category TEXT,
                    price TEXT,                   -- adapted to the data
                    stock INTEGER
                )
            ''')

            # Creating Customer_Demographics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Customer_Demographics (
                    customer_id INTEGER PRIMARY KEY,
                    age TEXT,                      -- adapted to the data
                    gender TEXT,
                    location TEXT,
                    loyalty_program TEXT
                )
            ''')
            
            # Creating Sales_Transactions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Sales_Transactions (
                    transaction_id INTEGER PRIMARY KEY,
                    customer_id INTEGER,
                    product_id TEXT,               -- adapted to the data
                    employee_id INTEGER,
                    quantity TEXT,                 -- adapted to the data
                    total_amount REAL,
                    sale_date TEXT,
                    FOREIGN KEY (customer_id) REFERENCES customer_demographics(customer_id),
                    FOREIGN KEY (employee_id) REFERENCES employee_records(employee_id)
                )
            ''')

            
            conn.commit()

                       
            # Loading data from CSVs
            employee_df = pd.read_csv("employee_records.csv")
            products_df = pd.read_csv("product_details.csv")
            customers_df = pd.read_csv("customer_demographics.csv")
            transactions_df = pd.read_csv("sales_transactions.csv")
                   
            # Inserting data into tables
            employee_df.to_sql("Employee_Records", conn, if_exists="append", index=False)
            customers_df.to_sql("Customer_Demographics", conn, if_exists="append", index=False)
            transactions_df.to_sql("Sales_Transactions", conn, if_exists="append", index=False)
            products_df.to_sql("Product_Details", conn, if_exists="append", index=False)
   
            conn.close()
            print("✅ Database setup complete: Tables created and populated with data!")

