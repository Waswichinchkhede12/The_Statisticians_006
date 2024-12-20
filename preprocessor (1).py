import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def multiselect(title, options):
    selected = st.sidebar.multiselect(title, options)
    select_all = st.sidebar.checkbox('Select all', value = True, key = title)
    if select_all:
        select_options = options
    else:
        select_options = selected
    return select_options


# Total sales per cuisine type
def total_sales(df):
    return df.groupby('cuisine_type')['cost_of_the_order'].sum().reset_index()


def popular_cuisine(df):
    return df['cuisine_type'].value_counts().reset_index()


def delivery_time(df):
    return df.groupby('day_of_the_week')['delivery_time'].mean().reset_index()
    



