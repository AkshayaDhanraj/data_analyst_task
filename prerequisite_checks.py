import pandas as pd

df_shipping = pd.read_json('/Users/akshayadhanraj/Python/DataAnalystTask/Shipping.json')
df_order = pd.read_csv('/Users/akshayadhanraj/Python/DataAnalystTask/Order.csv')
df_customer = pd.read_excel('/Users/akshayadhanraj/Python/DataAnalystTask/Customer.xls', sheet_name='atkoe-u250m')

#print(df_shipping.info(),df_order.info(),df_customer.info())

print('\n--- Step 1: Completeness ---\n')
# Check NULL values in any of the fields
print('Order missing values:\n', df_order.isnull().sum())
print('Customer missing values:\n', df_customer.isnull().sum())
print('Shipping missing values:\n', df_shipping.isnull().sum())

print('\n--- Step 2: Accuracy ---\n')
# Amounts should be positive
print('Orders with non-positive amount: ', df_order[df_order['Amount'] <= 0].count())

# Check foreign key consistency
print('Orders with missing customer info: ', df_order[~df_order['Customer_ID'].isin(df_customer['Customer_ID'])].count())
print('Shipping with missing customer info: ', df_shipping[~df_shipping['Customer_ID'].isin(df_customer['Customer_ID'])].count())

print('\n--- Step 3: Reliability ---\n')
# Check for duplicate records
print('Orders with duplicate values: ',df_order.duplicated().sum())
print('Customer with duplicate values: ',df_customer.duplicated().sum())
print('Shipping with duplicate values: ',df_shipping.duplicated().sum())



