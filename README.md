# Data Analyst Task

A **data analyst** project demonstrating data validation, modeling, and reporting on customer, order, and shipping datasets.  

---

## Overview
This project showcases the end-to-end process a data analyst would follow:
1. Validate data for completeness, accuracy, and reliability.  
2. Transform raw datasets into a structured star schema.  
3. Generate actionable business insights.  

---

## Data Sources
- **Customer.xls** – Customer information  
- **Order.csv** – Order details  
- **Shipping.json** – Shipping information  

---

## Project Objectives
- **Data Validation**: Ensure datasets are clean, consistent, and reliable.  
- **Data Modeling**: Implement a star schema for analytics.  
- **Technical Implementation**: Provide instructions for Data & QA engineers.  
- **Business Reporting**: Enable actionable insights into customer behavior and sales trends.  

---

## Data Model
The project uses a **star schema**:

![01EE6F7E-7B6C-4D7D-A96A-A377A39F5A99](https://github.com/user-attachments/assets/2eda9163-b371-4436-981a-25641f8f3d5b)


- **Dim_Customer** – Stores customer details
- **Dim_Shipping** – Tracks shipment information
- **Dim_Product** – Tracks product information
- **Dim_Date** – Contains date series information for last 2 years
- **Fact_Order** – Tracks orders placed by customers  

---

## User Stories

### Data Engineer
- Ingest raw data into target tables.  
- Apply transformations and add housekeeping columns.  
- Ensure data consistency and integrity.

### QA Engineer
- Validate completeness, accuracy, and reliability of data.  
- Check for missing values and duplicate rows.  
- Verify transformation rules have been applied correctly.  

---

## Business Insights
This project supports the following analytics:

- Total amount spent per country for pending orders  
- Total transactions, quantity sold, and amount spent per customer along with product details
- Maximum products purchased per country  
- Most purchased products based on age category (<30 / ≥30)  
- Country with minimum transactions and sales amount  

---

## Author
**Akshaya Dhanraj**
