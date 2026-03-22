import streamlit as st
import pandas as pd

#Title and subheader

st.title("Sales summary dashboard")
st.subheader("A simple streamlit app to view and filter product sales by category")

#Hardcoded dataset

data={
    "Product":["Laptop","Mouse","Shirt","Shoes","Phone","Jeans"],
    "Category":["Electronics","Electronics","Clothing","Footwear","Electronics","Clothing"],
    "Sales":[50000,1500,2000,3500,30000,2500]
}

df=pd.DataFrame(data)

#Sidebar filter

categories=["All"]+list(df["Category"].unique())
selected_category=st.sidebar.selectbox("Select Category",categories)

#Filtered DataFrame
if selected_category=="All":
    filtered_df=df
else:
    filtered_df=df[df["Category"]==selected_category]

#Display Filtered table

st.write("Filtered Sales Data")
st.dataframe(filtered_df)

#Line chart
st.write("Sales Line chart")
st.line_chart(filtered_df["Sales"])