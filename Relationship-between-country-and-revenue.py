import pyodbc
import pandas as pd
from matplotlib import pyplot as plt
# Establish connection to the AdventureWorks2022 database
connection = pyodbc.connect(
	r'DRIVER={ODBC Driver 17 for SQL Server};'
	r'SERVER=DESKTOP-G1HPGDT\SQLEXPRESS;'
	r'DATABASE=AdventureWorks2022;'
	r'Trusted_Connection=yes;'
	r'TrustServerCertificate=yes;'
)
# SQL Query to retrieve and aggregate revenue data
query = """
SELECT SD.CountryRegionName as Country, SUM(SW.AnnualRevenue) AS Revenue
FROM Sales.vStoreWithAddresses as SD
JOIN Sales.vStoreWithDemographics as SW
ON SD.BusinessEntityID=SW.BusinessEntityID
GROUP BY CountryRegionName
ORDER BY Revenue DESC;
"""
 
# Execute the query and load the results into a DataFrame
df = pd.read_sql(query, connection)
# Print the data to verify
print(df) 
# Create a bar chart
plt.barh(df['Country'], df['Revenue'], color='orange')
plt.title(" Country by Revenue", fontweight='bold', fontsize=22)
plt.ylabel("Country")
plt.xlabel("Revenue(in millions)")
plt.show()
# Close the database connection
connection.close()
