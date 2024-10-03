import streamlit as st

# Sidebar layout with persistent navigation
st.sidebar.title("Navigation")

# Create buttons for Home and Team Members
home_button = st.sidebar.button("Home")
team_button = st.sidebar.button("Team Members")

# Create dropdown menu for assignments
assignment_page = st.sidebar.selectbox("Select an Assignment", 
                                       ["Assignment 1: User Research", 
                                        "Assignment 2: User Interface Design", 
                                        "Assignment 3: Interaction Design",
                                        "Assignment 4: Prototyping",
                                        "Assignment 5: Usability Testing",
                                        "Assignment 6: Final Evaluation"])

# Determine the page to display
if home_button:
    page = "Home"
elif team_button:
    page = "Team Members"
else:
    page = assignment_page

# Main content changes based on selection
# Home page content
if page == "Home":
    st.title("Human-Computer Interaction Course Assignments")
    st.write("Welcome to our HCI assignment portal. Explore all the assignments and team members here.")

# Assignment 1
elif page == "Assignment 1: User Research":
    st.title("Assignment 1: User Research")
    st.write("Description of Assignment 1")
    st.markdown("[Assignment 1 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)
    st.markdown("""
    <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" 
    src="https://embed.figma.com/design/1Hj98OAQlYOB4EBUPBpJ2Y/WEBISTE-DESIGNS?node-id=0-1&embed-host=share" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

# Assignment 2
elif page == "Assignment 2: User Interface Design":
    st.title("Assignment 2: User Interface Design")
    st.write("Description of Assignment 2")
    st.markdown("[Assignment 2 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)
    st.markdown("""
    <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" 
    src="https://embed.figma.com/design/2Lk98RBQlYOB4EBUPBpJ3Y/WEBISTE-DESIGNS?node-id=0-2&embed-host=share" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

# Add more assignments similarly...
elif page == "Assignment 3: Interaction Design":
    st.title("Assignment 3: Interaction Design")
    st.write("Description of Assignment 3")
    st.markdown("[Assignment 3 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)
    st.markdown("""
    <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" 
    src="https://embed.figma.com/design/3Hj98OAQlYOB4EBUPBpJ4Y/WEBISTE-DESIGNS?node-id=0-3&embed-host=share" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

elif page == "Assignment 4: Prototyping":
    st.title("Assignment 4: Prototyping")
    st.write("Description of Assignment 4")
    st.markdown("[Assignment 4 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)

elif page == "Assignment 5: Usability Testing":
    st.title("Assignment 5: Usability Testing")
    st.write("Description of Assignment 5")
    st.markdown("[Assignment 5 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)

elif page == "Assignment 6: Final Evaluation":
    st.title("Assignment 6: Final Evaluation")
    st.write("Description of Assignment 6")
    st.markdown("[Assignment 6 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)

# Team Members Section
elif page == "Team Members":
    st.title("Team Members")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("./images/mansi.jpeg", width=150)
        st.write("Name: John Doe")
        st.write("Roll No: 123")
        st.write("PRN: ABC123")
    
    with col2:
        st.image("./images/mansi.jpeg", width=150)
        st.write("Name: Jane Doe")
        st.write("Roll No: 124")
        st.write("PRN: XYZ456")
    
    with col3:
        st.image("./images/mansi.jpeg", width=150)
        st.write("Name: Michael Smith")
        st.write("Roll No: 125")
        st.write("PRN: LMN789")
    
    with col4:
        st.image("./images/mansi.jpeg", width=150)
        st.write("Name: Sarah Johnson")
        st.write("Roll No: 126")
        st.write("PRN: QWE890")
