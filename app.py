import streamlit as st

# Sidebar navigation
st.sidebar.title("Assignments")
pages = ["Home", "Assignment 1", "Assignment 2", "Team Members"]
page = st.sidebar.selectbox("Select a page", pages)

# Homepage
if page == "Home":
    st.title("Human-Computer Interaction Course Assignments")
    st.write("Welcome to our HCI assignment portal. Explore all the assignments and team members here.")

# Assignment 1
if page == "Assignment 1":
    st.title("Assignment 1: User Research")
    st.write("Description of Assignment 1")
    st.markdown("[Assignment 1 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)
    st.markdown("""
    <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" 
    src="https://www.figma.com/embed?embed_host=share&url=https://www.figma.com/file/your-figma-link" 
    allowfullscreen></iframe>
    """, unsafe_allow_html=True)

# Team members section
if page == "Team Members":
    st.title("Team Members")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("path_to_image1.jpg", width=150)
        st.write("Name: John Doe")
        st.write("Roll No: 123")
        st.write("PRN: ABC123")
    
    with col2:
        st.image("path_to_image2.jpg", width=150)
        st.write("Name: Jane Doe")
        st.write("Roll No: 124")
        st.write("PRN: XYZ456")
    
    with col3:
        st.image("path_to_image3.jpg", width=150)
        st.write("Name: Michael Smith")
        st.write("Roll No: 125")
        st.write("PRN: LMN789")
