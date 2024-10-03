import streamlit as st

# Sidebar layout with persistent navigation
st.sidebar.title("HCI Project")

# Create buttons for Home and Team Members
home_button = st.sidebar.button("Introduction")
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
    st.markdown("<h1 style='text-align: center;'>AI-Based Skill Assessment System </h1>", unsafe_allow_html=True)
    

    # Centered Purpose and Objective Section with Smaller Font
    st.markdown("<h3 style='font-size: 26px;'>📌 Purpose and Objective</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul style="font-size: 16px;">
        <li>The AI-Based Skill Assessment System is designed to streamline the placement process for IT engineering students and the Training and Placement Office (TPO).</li>
        <li>By providing an integrated platform, the system helps students evaluate their skills, receive career guidance, and improve their placement prospects through domain-specific quizzes and personalized recommendations.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Centered Project Scope Section with Smaller Font
    st.markdown("<h3 style=' font-size: 26px;'>🔍 Project Scope</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul style="font-size: 16px;">
        <li>The system supports students in uploading their resumes, receiving ATS-based skill extraction, and accessing personalized career recommendations.</li>
        <li>It also assists TPOs in managing and sorting students based on skills, department, and resume scores.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Centered Target Audience Section with Smaller Font
    st.markdown("<h3 style=' font-size: 26px;'>🎓 Target Audience</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul style="font-size: 16px;">
        <li>This system is designed for IT engineering students, the Training and Placement Office, and academic administrators to facilitate career guidance and placement management.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Centered HCI Techniques Section with Smaller Font
    st.markdown("<h3 style='font-size: 26px;'>🛠️ Human-Computer Interaction (HCI) Techniques Used</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul style="font-size: 16px;">
        <li><strong>User Journey Map</strong>: Visual representation of a student’s experience with the system.</li>
        <li><strong>Scenario Design</strong>: Scenarios showcasing common interactions and system usage.</li>
        <li><strong>Card Sorting</strong>: Organizing content based on user feedback to improve information structure.</li>
        <li><strong>Low-Fidelity and High-Fidelity Prototypes</strong>: Iterative design approach to create and refine user interface designs.</li>
    </ul>
    """, unsafe_allow_html=True)

    

# Assignment 1
elif page == "Assignment 1: User personna":
    st.title("Assignment 1: User personna")
    st.write("In this assignment, we created detailed user personas for the AI-Based Skill Assessment System. The purpose of developing these personas was to gain a deeper understanding of the target users—IT engineering students, Training and Placement Officers (TPOs), and academic administrators. Each persona includes demographic information, goals, needs, and pain points related to the skill assessment and placement process. By identifying these user characteristics, we aimed to ensure that the system's design aligns with users' expectations and enhances their overall experience. This user-centered approach will guide the development of features and functionalities tailored to the diverse needs of our users.")
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
        st.write("Name: Vivek Pahilwan")
        st.write("Roll No: 331071")
        st.write("PRN: 22320030")
    
    with col2:
        st.image("./images/mansi.jpeg", width=150)
        st.write("Name: Manasi Hire")
        st.write("Roll No: 331070")
        st.write("PRN: 22320015")
    
    with col3:
        st.image("./images/mansi.jpeg", width=150)
        st.write("Name: Janhavi Hire")
        st.write("Roll No: 332069")
        st.write("PRN: 22320016")
    
    with col4:
        st.image("./images/mansi.jpeg", width=150)
        st.write("Name: Dhiraj Wagh")
        st.write("Roll No: 331072")
        st.write("PRN: 22320044")
