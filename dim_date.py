import pandas as pd
from datetime import datetime, timedelta

# Define start and end dates
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 12, 31)

# Generate list of all dates
date_list = pd.date_range(start=start_date, end=end_date)

# Create DataFrame
df_date = pd.DataFrame(date_list, columns=['full_date'])
df_date['full_date'] = df_date['full_date'].dt.date

# Add required fields
df_date['date_id'] = df_date['full_date'].apply(lambda x: int(x.strftime('%Y%m%d')))
df_date['day'] = pd.DatetimeIndex(df_date['full_date']).day
df_date['month'] = pd.DatetimeIndex(df_date['full_date']).month
df_date['year'] = pd.DatetimeIndex(df_date['full_date']).year
df_date['quarter'] = pd.DatetimeIndex(df_date['full_date']).quarter
df_date['created_date'] = pd.Timestamp.now()

# Optional: reorder columns
df_date = df_date[['date_id', 'full_date', 'day', 'month', 'year', 'quarter', 'created_date']]


