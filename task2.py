import pandas as pd

# Load the datasets
customers_path = "/mnt/data/Customers.csv"
products_path = "/mnt/data/Products.csv"
transactions_path = "/mnt/data/Transactions.csv"

# Read data into pandas DataFrames
customers_df = pd.read_csv(customers_path)
products_df = pd.read_csv(products_path)
transactions_df = pd.read_csv(transactions_path)

# Display the first few rows of each dataset to understand their structure
customers_head = customers_df.head()
products_head = products_df.head()
transactions_head = transactions_df.head()

# Basic info to understand the structure
customers_info = customers_df.info()
products_info = products_df.info()
transactions_info = transactions_df.info()

(customers_head, products_head, transactions_head)
