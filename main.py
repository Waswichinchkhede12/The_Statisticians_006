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
    st.title('Total Sales per Cuisine Type')
    st.bar_chart(
    sales_per_cuisine.set_index('cuisine_type'), 
    use_container_width=True
     )


most_popular_cuisine = preprocessor.popular_cuisine(df)
with col5:
    st.title('Number of orders by cuisine type')
    st.bar_chart(most_popular_cuisine.set_index('cuisine_type'), use_container_width = True)


# Line chart for Average delivery time as per the day of the week
delivery_performance = preprocessor.delivery_time(df)

fig = px.line(delivery_performance, x='day_of_the_week', y='delivery_time', markers=True, title='Average Delivery Time by Day of the Week')
st.plotly_chart(fig, use_container_width=True)






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
            color_continuous_scale="RdBu",  # Replace with a valid Plotly color scale
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





# Histogram of cost of the order
st.title('Histogram of Cost of the Order')

fig = px.histogram(df, x='cost_of_the_order', nbins=20, labels={'cost_of_the_order':'Cost of the Order'}, template='plotly_white')
fig.update_layout(xaxis_title_text='Cost of the Order', yaxis_title_text='Frequency', bargap=0.1, height=600, width=800)
st.plotly_chart(fig, use_container_width=True)                  
         




# Pie chart to show no. of orders by cuisine type
st.title('Number of Orders by Cuisine Type') # Create the pie chart using Plotly 
fig = px.pie(df, values='order_id', names='cuisine_type', color_discrete_sequence=px.colors.sequential.RdBu) 

# Display the pie chart in Streamlit 
st.plotly_chart(fig, use_container_width=True)




