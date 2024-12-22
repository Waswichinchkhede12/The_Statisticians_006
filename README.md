# 🍽️Food Ordering & Delivery Dashboard 

## Dashboard Link: https://thestatisticians006-uwwsf8rbywqqhtigq98qhn.streamlit.app/

## Overview

This project presents an interactive dashboard designed for food ordering and delivery businesses. It provides key insights such as the number of restaurants, popular cuisines, customer preferences, and operational performance metrics. Visualizations include total sales by cuisine type, order distribution, average delivery times, and a correlation heatmap for predictive analysis. With tools for exploring demand forecasting, pricing strategies, and delivery efficiency, this dashboard helps businesses optimize operations and enhance customer satisfaction.

## Features ✨

### Data Cleaning & Preprocessing 🔧
- Checked for missing data, Duplicates and Handled them.
- Replaced 'Not given' values in the rating column with the mean of the column, then converted the column to a numeric data type for further analysis.
- Converted the day_of_the_week column into a categorical variable to facilitate more efficient data analysis and ensure proper handling of weekday information in 
visualizations and modeling.
- Generated summary statistics for the dataset by excluding the order_id and customer_id columns. This provides key metrics like mean, median, standard deviation, and range for the remaining numerical columns to better understand the data distribution.
- Cleaned the restaurant_name column by removing all special characters using regular expressions. This ensures the names contain only alphanumeric characters and spaces, improving consistency for analysis and visualization.
- Coverted into csv file and downloaded the cleaned dataset.
- Conducted Exploratory Data Analysis (EDA) to ensure data quality by identifying missing values, outliers, and inconsistencies in the dataset. This process helped improve data integrity and informed preprocessing decisions for accurate insights.

## Streamlit Dashboard 🚀📊
### 🌟 Key-Performance Indicators(KPI's):
   - No. of Restaraunts in the dataset.
   - Restaraunt with max no. orders (Popular Restaraunt).
   - Most popular Cuisine.
### Visualizations📊 
  1. Total Sales per cuisine analysis🍽️💰
     - Bar chart for total sales per cuisine
  2. Popular cuisine 🍴
     - Bar chart for count of cuisine type
  3. Average Delivery time analysis⏰
     - Line chart for average delivery time based on day of the week
  4. Correlation Heatmap 🔗
     - Correelation between two selected numeric columns
  5. Distribution of cost of the orders 📈
     - Histogram visualizing the distribution of cost of the orders
  6. Proportion of orders 🥧📊
     - Pie chart for customer preferences across different cuisines

## Tools and IDE used 🛠️
  - Jupyter Notebook 
  - Python - Data Manipulation and analysis
  - Pandas - Data Cleaning and EDA
  - Matplotlib and seaborn - Data Visualization on EDA
  - Plotly - Interactive Visualizations in Streamlit
  - Streamlit - Web-based Dashboard application

## Insights 💡
  - The dashboard provides a visual analysis of total sales by cuisine type, helping businesses identify the most profitable categories.
  - By examining the number of orders per cuisine, we gain insights into customer preferences, aiding in demand forecasting.
  - The average delivery time analysis by day of the week helps identify inefficiencies in the delivery process, offering opportunities for improvement.
  - The correlation heatmap and order cost histogram support predictive analysis and pricing strategies, enabling better business decisions.

---
      
# How to use
Launch the app using streamlit run app.py.
## Explore the Dashboard:
Use the sidebar to select a restaurant, cuisine, day of the week, and rating.
View missing values, duplicate entries, and their replacements.
Analyze heatmap, histogram, and pie chart for better understanding.
## Visualize Data:
Interactive charts for better insights.

## Sample Dataset
The dataset food_order.csv contains the following columns:
Numeric columns: order_id, customer_id, cost_of_the_order, rating, food_preparation_time, deliver_time. 
Categorical columns: restaurant_name, cuisine_type, day_of_the_week

## Acknowledgments
- Waswi: Responsible for the visualization of data, compilation of the report, and the final presentation.
- Ujwal Reddy: Focused on data cleaning, analysis, and extracting key insights.
- tools and libraries used in this project: Streamlit, Plotly, Pandas, and Plotly Express, making the development process seamless and efficient.



