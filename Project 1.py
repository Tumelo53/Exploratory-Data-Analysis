from numpy import mean
import pandas as pd
import matplotlib.pyplot as plt

#Load the data and inspect the data set
sales_info = pd.read_csv(r'C:\Users\Tumelo.Mothuli\Desktop\Internship\retail_sales_dataset.csv')


#Checking for missing data
missing_values = sales_info.isnull().sum()

#Dropping rows with missing data
sales_info = sales_info.dropna()

#Remove duplicate rows
sales_info = sales_info.drop_duplicates()


#Descriptive statistics
#Calculating basic Statistics

mean_salesteam = sales_info['Total Amount'].mean()
median_salesteam = sales_info['Total Amount'].median()
mode_salesteam = sales_info['Total Amount'].mode()[0]
std_salesteam = sales_info['Total Amount'].std()



#Time Series Analysis
#Convert the date column to the datetime format
#Converting to datetime format allows for time-based operations and analyses, 
#like resampling or plotting over time
sales_info['Date'] = pd.to_datetime(sales_info['Date'])

#Analysing sales trends over time
daily_sales = sales_info.groupby('Date')['Total Amount'].sum()
print(daily_sales)


#Customer and Product Analysis
# The goal is to understand customer demographics and thier purscharing beahviour and analyse product performance

#Segment customer by demographics
customer_demographics = sales_info.groupby(['Age', 'Gender']).size().reset_index(name='Counts')
print(customer_demographics)

#Analyze product Sales:Evaluating the sales performances of different products

product_sales = sales_info.groupby('Product Category')['Total Amount'].sum().reset_index()
print(product_sales)

#Visualisation
product_sales.plot(kind='bar', x='Product Category', y='Total Amount', figsize=(8, 6), title='Product Sales')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()
#Show which demographic buys a lot
demographic_sales = sales_info.groupby(['Age', 'Gender'])['Sales'].sum().reset_index()
# Sort the results to see the highest spending demographics at the top
demographic_sales = demographic_sales.sort_values(by='Sales', ascending=False)
#Visualise
demographic_sales.plot(kind= 'bar', x='Age', y='Sales', color='Gender'figsize=(10,6), title="Sales by demographic")
plt.xlabel("Age and Gender")
plt.ylabel("Total Sales")
plt.show()

#Show the sales trend over time using a line plot
daily_sales.plot(figsize=(10, 6), title='Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.show()

