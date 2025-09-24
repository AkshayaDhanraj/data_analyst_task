import pandas as pd
from dim_date import df_date
from datetime import datetime

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
print('Customers with non-positive age: ', df_customer[df_customer['Age'] <= 0].count())

# Age field should not be more than 100
print('Customer age greater than 100: ', df_customer[df_customer['Age'] > 100].count())

# Records containing special characters in First & Last name
print('Customer first name with special characters: \n', df_customer[df_customer['First'].str.contains(r'[^a-zA-Z0-9\s]', regex=True)])
print('Customer last name with special characters: \n', df_customer[df_customer['Last'].str.contains(r'[^a-zA-Z0-9\s]', regex=True)])

# Check foreign key consistency
print('Orders with missing customer info: ', df_order[~df_order['Customer_ID'].isin(df_customer['Customer_ID'])].count())
print('Shipping with missing customer info: ', df_shipping[~df_shipping['Customer_ID'].isin(df_customer['Customer_ID'])].count())
print('Orders with missing shipping info: ', df_order[~df_order['Customer_ID'].isin(df_shipping['Customer_ID'])].count())

print('\n--- Step 3: Reliability ---\n')
# Check for duplicate records
print('Orders with duplicate values: ',df_order.duplicated().sum())
print('Customer with duplicate values: ',df_customer.duplicated().sum())
print('Shipping with duplicate values: ',df_shipping.duplicated().sum())

# Re-create df_customer
df_customer['date_of_birth'] = pd.to_datetime((datetime.today().year - df_customer['Age']).astype(str) + '-01-01')
df_customer[['created_date','modified_date']] = pd.Timestamp.now()
df_customer = df_customer.rename(columns={'Customer_ID':'customer_id','First': 'first_name','Last':'last_name','Country':'country'})
df_customer['age_category'] = df_customer['Age'].apply(lambda x: '<30' if x < 30 else '>=30')
df_customer = df_customer[['customer_id','first_name','last_name','date_of_birth','age_category','country','created_date','modified_date']]
df_customer.to_csv('/Users/akshayadhanraj/Python/DataAnalystTask/dim_customer.csv', index=False)

# Re-create df_order
df_order = df_order.merge(df_shipping[['Customer_ID','Shipping_ID']], on='Customer_ID' , how = 'left')
df_order[['order_date']] = pd.Timestamp.now().date()
df_order[['created_date','modified_date']] = pd.Timestamp.now()
df_order = df_order.merge(df_date[['full_date', 'date_id']],left_on='order_date',right_on='full_date',how='left')
df_order = df_order.rename(columns={'Order_ID':'order_id','Amount': 'amount','Customer_ID':'customer_id','Shipping_ID':'shipping_id'})
df_order = df_order[['order_id','customer_id','shipping_id','date_id','Item','amount','order_date','created_date','modified_date']]

# Re-create df_shipping
df_shipping[['shipping_date']] = pd.Timestamp.now().date()
df_shipping[['created_date','modified_date']] = pd.Timestamp.now()
df_shipping = df_shipping.rename(columns={'Shipping_ID':'shipping_id','Status': 'status'})
df_shipping = df_shipping[['shipping_id','status','shipping_date','created_date','modified_date']]
df_shipping.to_csv('/Users/akshayadhanraj/Python/DataAnalystTask/dim_shipping.csv', index=False)

# Create df_product
df_product = df_order[['Item']].drop_duplicates().reset_index(drop=True)
df_product = df_product.rename(columns={'Item': 'product_name'})
df_product['product_id'] = range(1, len(df_product) + 1)
df_product[['created_date','modified_date']] = pd.Timestamp.now()
df_product = df_product[['product_id','product_name','created_date','modified_date']]
df_product.to_csv('/Users/akshayadhanraj/Python/DataAnalystTask/dim_product.csv', index=False)

# Re-create df_order
df_order = df_order.merge(df_product[['product_name', 'product_id']],left_on='Item',right_on='product_name',how='left')
df_order = df_order[['order_id','customer_id','shipping_id','date_id','product_id','amount','order_date','created_date','modified_date']]
df_order.to_csv('/Users/akshayadhanraj/Python/DataAnalystTask/fact_order.csv', index=False)



