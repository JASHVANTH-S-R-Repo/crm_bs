import streamlit as st
from PIL import Image

# Define the function to display an image
def show_image(image_path):
    img = Image.open(image_path)
    st.image(img, caption='', use_column_width=True)

# Define the function to display the information about a CRM software
def show_crm(name, image_path, reasons):
    st.subheader(name)
    show_image(image_path)
    st.write('Reasons why it is one of the best CRMs:')
    for reason in reasons:
        st.write('- ' + reason)

# Define the list of top 5 CRMs with their information
top_5_crms = [
    {
        'name': 'Salesforce',
        'image_path': 'salesforce.png',
        'reasons': ['Highly customizable', 'Large community and support']
    },
    {
        'name': 'HubSpot',
        'image_path': 'hubspot.png',
        'reasons': ['Easy to use', 'All-in-one solution for sales, marketing, and service']
    },
    {
        'name': 'Zoho CRM',
        'image_path': 'zoho.jpg',
        'reasons': ['Affordable pricing', 'Integration with other Zoho apps']
    },
    {
        'name': 'Pipedrive',
        'image_path': 'pipedrive.png',
        'reasons': ['Visual pipeline management', 'Automation features']
    },
    {
        'name': 'Freshsales',
        'image_path': 'Freshsales.jpg',
        'reasons': ['AI-based lead scoring', 'Integration with Freshworks suite']
    }
]

# Display the header of the blog
st.title('Top 5 Best CRM Softwares')
st.write('In this blog post, we will introduce you to the top 5 best CRM softwares based on their features, user-friendliness, and pricing.')

# Display the information about each CRM software
for crm in top_5_crms:
    show_crm(crm['name'], crm['image_path'], crm['reasons'])
