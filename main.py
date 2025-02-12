import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import preprocessor
import seaborn as sns
import plotly.express as px

df = pd.read_csv('cleaned_dataset2.csv')

# Title for the Dashboard
st.markdown(
    """
    <style>
    .centered-title {
    text-align: center;
    font-size: 30px;
    
    }
    </style>
    <h1 class="centered-title">🍽️Food Ordering and Delivery Dashboard</h1>
    """,
    unsafe_allow_html=True
    
)


# Sidebar for filters
st.sidebar.title("Filters")

# Filters
selected_restaurant = preprocessor.multiselect('Select Restaurant', df['restaurant_name'].unique())
selected_cuisine = preprocessor.multiselect('Select Cuisine', df['cuisine_type'].unique())
select_day = preprocessor.multiselect('Select Day of the week', df['day_of_the_week'].unique())
select_rating = preprocessor.multiselect('Select Rating', df['rating'].unique())



# Key Performance Indicators
col1, col2, col3 = st.columns(3)


# Total no. of unique Resatraunts
with col1:
    st.metric(label = 'No. of Restaraunts', value = df['restaurant_name'].nunique())

# Popular Restaurant
with col2:
    st.metric(label = 'Popular Restaraunt', value = df['restaurant_name'].value_counts().idxmax())

# Popular cuisine
with col3:
    st.metric(label = 'Popular Cuisine', value = df['cuisine_type'].value_counts().idxmax())

#with col4:
 #   st.metric(label = 'Customer Satisfaction', value = df['rating'].mean().round(1))



col4, col5 = st.columns(2)


# Bar chart for Total sales per cuisine 
sales_per_cuisine = preprocessor.total_sales(df)
with col4:
    st.markdown("<h4 style='font-size: 20px; font-weight: bold; color: #333; text-align: center;'>Total Sales per Cuisine Type</h4>", unsafe_allow_html=True)
    st.bar_chart(
    sales_per_cuisine.set_index('cuisine_type'), 
    use_container_width=True
     )
       # Add summary
    st.markdown("<h3 style='color: #4CAF50; font-weight: bold;'>Summary</h3>", unsafe_allow_html=True)
    st.write(
        "This chart shows the total revenue generated by each cuisine type. "
        "It helps identify the most profitable cuisines to focus on."
    )


most_popular_cuisine = preprocessor.popular_cuisine(df)
with col5:
    st.markdown("<h4 style='font-size: 20px; font-weight: bold; color: #333; text-align: center;'>Total Sales per Cuisine Type</h4>", unsafe_allow_html=True)
    st.bar_chart(most_popular_cuisine.set_index('cuisine_type'), use_container_width = True)
       # Add summary
    st.markdown("<h3 style='color: #4CAF50; font-weight: bold;'>Summary</h3>", unsafe_allow_html=True)
    st.write(
        "This chart highlights the number of orders received for each cuisine type. "
        "It provides insights into customer preferences and helps with demand forecasting."
    )


# Line chart for Average delivery time as per the day of the week
delivery_performance = preprocessor.delivery_time(df)

fig = px.line(delivery_performance, x='day_of_the_week', y='delivery_time', markers=True, title='Average Delivery Time by Day of the Week')
st.plotly_chart(fig, use_container_width=True)


st.markdown("<h3 style='color: #4CAF50; font-weight: bold;'>Summary</h3>", unsafe_allow_html=True)
st.write(
    "This chart illustrates the average delivery time for each day of the week. "
    "It provides actionable insights to improve delivery operations, address inefficiencies, and ensure consistent customer satisfaction."
)





# Correlation Heatmap between any two columns (numeric)
st.title("Correlation Heatmap Between Two Columns")

# Dropdowns for selecting columns
col1 = st.selectbox("Select the first column:", df.columns)
col2 = st.selectbox("Select the second column:", df.columns)

# Check if the selected columns are valid and numeric
if col1 and col2:
    if pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
        # Create a small DataFrame with the selected columns
        selected_data = df[[col1, col2]]

        # Compute the correlation matrix
        correlation_matrix = selected_data.corr()

        # Generate a heatmap using Plotly
        fig = px.imshow(
            correlation_matrix,
            text_auto=True,
            color_continuous_scale="Viridis",   # Replace with a valid Plotly color scale
            title=f"Correlation Heatmap: {col1} and {col2}",
        )
        fig.update_layout(
            title_font_size=18,
            title_x=0.5,
            margin=dict(l=10, r=10, t=40, b=10),
        )

        # Display the Plotly heatmap in Streamlit
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Please select numeric columns to calculate correlation and display a heatmap.")

st.markdown("<h3 style='color: #4CAF50; font-weight: bold;'>Summary</h3>", unsafe_allow_html=True)
st.write(
    "This heatmap showcases the correlation between two selected numeric columns. "
    "It helps in identifying relationships between variables, which can be critical for predictive analysis and decision-making. "
    "Strong positive or negative correlations indicate potential dependencies worth exploring further."
)



# Histogram of cost of the order
st.title('Histogram of Cost of the Order')

fig = px.histogram(df, x='cost_of_the_order', nbins=20, labels={'cost_of_the_order':'Cost of the Order'}, template='plotly_white')
fig.update_layout(xaxis_title_text='Cost of the Order', yaxis_title_text='Frequency', bargap=0.1, height=600, width=800)
st.plotly_chart(fig, use_container_width=True)                  


st.markdown("<h3 style='color: #4CAF50; font-weight: bold;'>Summary</h3>", unsafe_allow_html=True)
st.write(
    "This histogram visualizes the distribution of the cost of orders. "
    "It provides insights into the frequency of different cost ranges, helping identify common price points and outliers. "
    "This information can be valuable for pricing strategies and understanding customer spending behavior."
)



# Pie chart to show no. of orders by cuisine type
st.title('Number of Orders by Cuisine Type') # Create the pie chart using Plotly 
fig = px.pie(df, values='order_id', names='cuisine_type', color_discrete_sequence=px.colors.sequential.RdBu) 

# Display the pie chart in Streamlit 
st.plotly_chart(fig, use_container_width=True)


st.markdown("<h3 style='color: #4CAF50; font-weight: bold;'>Summary</h3>", unsafe_allow_html=True)
st.write(
    "This pie chart illustrates the proportion of orders received for each cuisine type. "
    "It provides a clear overview of customer preferences across different cuisines, "
    "helping identify the most popular cuisine types and areas for potential growth."
)



# Define the project code and credits
st.markdown("""
<style>
    .project-details {
        font-size: 18px;
        margin-bottom: 15px;
    }
    .credits-heading {
        font-weight: bold;
        font-size: 20px;
        margin-top: 20px;
    }
    .team-member {
        font-size: 18px;
        margin-left: 20px;
    }
    .footer {
        margin-top: 30px;
        font-size: 16px;
        color: #6c757d;
    }
</style>
""", unsafe_allow_html=True)

# Add the project details
st.markdown("<div class='project-details'><strong>Project Code:</strong> [The_Statisticians_006]</div>", unsafe_allow_html=True)

# Add the credits section
st.markdown("<div class='credits-heading'>Credits:</div>", unsafe_allow_html=True)
st.markdown("""
<div>
    <ul style="list-style-type: disc; margin-left: 40px;">
        <li class="team-member"><strong>Waswi</strong>:  Visualization of Data, Compilation of Report and Final Presentation</li>
        <li class="team-member"><strong>Ujwal Reddy</strong>:  Data Cleaning, Analysis and Insights Extraction</li>
        
    
</div>
""", unsafe_allow_html=True)




