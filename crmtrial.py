import streamlit as st
import pandas as pd

# Set page title and favicon
st.set_page_config(page_title='CRM Software', page_icon=':guardsman:')

# Load CSV data
df = pd.read_csv('customer_data.csv')

# Define sidebar options
options = ['View Customers', 'Add Customer', 'Edit Customer', 'Delete Customer']
choice = st.sidebar.selectbox('Select an option', options)

# Add customer
if choice == 'Add Customer':
    st.header('Add Customer')
    name = st.text_input('Name')
    email = st.text_input('Email')
    phone = st.text_input('Phone Number')
    address = st.text_input('Address')
    if st.button('Submit'):
        new_customer = {'Name': name, 'Email': email, 'Phone Number': phone, 'Address': address}
        df = df.append(new_customer, ignore_index=True)
        df.to_csv('customer_data.csv', index=False)
        st.success('Customer added successfully!')

# Edit customer
if choice == 'Edit Customer':
    st.header('Edit Customer')
    customer = st.selectbox('Select a customer', df['Name'])
    index = df[df['Name'] == customer].index[0]
    name = st.text_input('Name', value=df['Name'][index])
    email = st.text_input('Email', value=df['Email'][index])
    phone = st.text_input('Phone Number', value=df['Phone Number'][index])
    address = st.text_input('Address', value=df['Address'][index])
    if st.button('Submit'):
        df.loc[index] = [name, email, phone, address]
        df.to_csv('customer_data.csv', index=False)
        st.success('Customer information updated successfully!')

# Delete customer
if choice == 'Delete Customer':
    st.header('Delete Customer')
    customer = st.selectbox('Select a customer', df['Name'])
    if st.button('Delete'):
        index = df[df['Name'] == customer].index[0]
        df = df.drop(index)
        df.to_csv('customer_data.csv', index=False)
        st.success('Customer deleted successfully!')

# View customers
if choice == 'View Customers':
    st.header('View Customers')
    st.dataframe(df)

# Set footer
st.markdown("""<div style='text-align: center'>
                Built with Streamlit by <a href='https://www.linkedin.com/in/jashvanth-s-r-476646213/'>Jashvanth S R</a>
                </div>""", unsafe_allow_html=True)
