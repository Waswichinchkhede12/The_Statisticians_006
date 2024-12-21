# 🍽️ The food order & delivery dashboard 

This project is a **Streamlit-based dashboard** for analyzing food orders and delivery across different restaurants. 
---

## Features ✨

1. **Dataset Overview**:
   - Displays the dataset's head and missing values.
   - Handles missing values with mean imputation.

2. **Interactive Visualizations**:
   - Total Sales per Cuisine.
   - Average delivery time by day of the week.
   - Correlation heatmap.
   - Histogram visualizes the distribution of the cost of orders. 
   - Pie chart visualizes the number of orders by cuisine type. 

4. **User Inputs**:
   - Select restaurant, cuisine, day of the week, and rating for focused analysis.
   - Dynamic filtering and visual updates based on user selections.

5. **Correlation Heatmap**:
   - Visualizes correlations between two numeric columns. 

---

## Tech Stack 🛠️

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: 
  - Matplotlib
  - Seaborn
  - Plotly Express
- **Data**: Food order and delivery dashboard (`food_order.csv`)

---

## Installation 🔧

### Prerequisites

- Python 3.8 or higher
- Virtual Environment (optional but recommended)
- Required Python Libraries:
  - `streamlit`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `plotly`

### Steps

1. Install dependencies 
    pip install -r requirements.txt
2. Run app
    streamlit run main.py

File structure
 ├── app.py                 # Main Streamlit app
├── cleaned_dataset2.csv # Dataset
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
 
        
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
Categorical columns: restaurant_name, cuisine_type, day_of_the_week, 

# Known Issues
Ensure the dataset food_order.csv is uncleaned data and the clean data is cleaned_dataset2.csv is present in the root directory.
The app is optimized for desktops; smaller screens may impact the layout. 

