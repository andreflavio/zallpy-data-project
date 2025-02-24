import sqlite3
import pandas as pd

conn = sqlite3.connect('sales_database.db')
result = pd.read_sql_query("SELECT Region, SUM(Sales) AS Total_Sales FROM sales GROUP BY Region ORDER BY Total_Sales DESC;", conn)
print(result)
conn.close()