import streamlit as st


# Sidebar layout with persistent navigation
st.sidebar.title("HCI Project")

# Create buttons for Home and Team Members
home_button = st.sidebar.button("Introduction")
team_button = st.sidebar.button("Team Members")

# Create dropdown menu for assignments
assignment_page = st.sidebar.selectbox("Select an Assignment", 
                                       ["Assignment 1: User Personna", 
                                        "Assignment 2: Scenerio and user jouney map", 
                                        "Assignment 3: Card sorting",
                                        "Assignment 4: Low fidelity design",
                                        "Assignment 5: High fidelity design",
                                        "Assignment 6: prototype design"])

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
elif page == "Assignment 1: User Personna":
    st.title("Assignment 1: User Personna")
    st.markdown("In this assignment, we created detailed user personas for the AI-Based Skill Assessment System. The purpose of developing these personas was to gain a deeper understanding of the target users—IT engineering students, Training and Placement Officers (TPOs), and academic administrators. Each persona includes demographic information, goals, needs, and pain points related to the skill assessment and placement process. By identifying these user characteristics, we aimed to ensure that the system's design aligns with users' expectations and enhances their overall experience. This user-centered approach will guide the development of features and functionalities tailored to the diverse needs of our users.")
    st.markdown("[Assignment 1 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)
    st.markdown("""
    <iframe src="./assignments/ass1.png" width="800" height="600" 
    style="border: none;"></iframe>
    """, unsafe_allow_html=True)

# Assignment 2
elif page == "Assignment 2: Scenerio and user jouney map":
    st.title("Assignment 2: Scenerio and user jouney map")
    st.write("In this assignment, we developed detailed scenarios and a user journey map for the AI-Based Skill Assessment System. The primary goal was to visualize and analyze the interactions of our target users—IT engineering students and Training and Placement Officers (TPOs)—with the system.")
    st.write("Scenarios: We crafted specific use cases that represent typical interactions users might have with the platform. These scenarios illustrate how students can upload resumes, take domain-specific quizzes, and receive personalized career recommendations. Simultaneously, we depicted how TPOs can manage and sort students based on their skills and resume scores. This method helps us identify user needs and pain points, guiding the design and functionality of our system.")
    st.write("User Journey Map: We created a user journey map to capture the entire experience of students as they navigate through the placement process. This map highlights key touchpoints, emotions, and potential barriers faced by users, allowing us to enhance the user experience. By understanding the user journey, we aim to streamline interactions and ensure that the platform meets the needs of its diverse audience.")
    st.write("This assignment has laid the groundwork for a user-centered design approach, ensuring that our system effectively addresses the challenges faced by IT engineering students and TPOs in the placement process")

    st.markdown("[Assignment 2 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)
    st.markdown("""
    <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" 
    src="https://embed.figma.com/design/2Lk98RBQlYOB4EBUPBpJ3Y/WEBISTE-DESIGNS?node-id=0-2&embed-host=share" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

# Add more assignments similarly...
elif page == "Assignment 3: Card sorting":
    st.title("Assignment 3: Card sorting")
    st.write("To enhance the information architecture of the AI-Based Skill Assessment System through open and closed card sorting techniques, ensuring intuitive navigation for users.Card sorting is a user-centered design method used to categorize information based on user input. It helps reveal how users expect content to be organized.")
    st.markdown("<h3 style='font-size: 26px;'>Types of Card Sorting </h3>",unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 22px;'>1.  Open Card Sorting</h2>", unsafe_allow_html=True)
    st.write(
        "Participants sort a set of cards representing content/features into groups they create. "
        "This method helps us understand how users naturally categorize information and their expectations for the system's structure."
    )
    st.markdown("<h2 style='font-size: 22px;'>2.  Closed Card Sorting</h2>", unsafe_allow_html=True)
    st.write(
        "Participants sort cards into predefined categories. "
        "This method evaluates the effectiveness of the proposed information architecture and helps refine the categorization."
    )
    st.markdown("<h2 style='font-size: 26px;'>Outcomes</h2>", unsafe_allow_html=True)
    st.write(
        "The card sorting assignment significantly improved the usability of the AI-Based Skill Assessment System by aligning its structure with user preferences, ensuring an effective user experience."
    )

    st.markdown("[Assignment 3 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)
    st.markdown("""
    <iframe src="./assignments/card_sort.pdf" width="800" height="450" 
    style="border: none;"></iframe>
    """, unsafe_allow_html=True)


elif page == "Assignment 4: Low fidelity design":
    st.title("Assignment 4: Low fidelity design")
    st.write(
        "In this assignment, we created low-fidelity prototypes for the AI-Based Skill Assessment System. The primary objective of low-fidelity design is to visualize and iterate on the basic layout and functionality of the system without getting bogged down by intricate details."
    )
    st.markdown("<h2 style='font-size: 26px;'>Process</h2>", unsafe_allow_html=True)
    st.write(
        "1. **Sketching**: We began by sketching the main interfaces on paper, including the home screen, user registration, resume upload, quiz interface, and TPO dashboard. These sketches helped us conceptualize the layout and navigation.\n"
        "2. **Wireframing**: After sketching, we moved to digital wireframing using tools like Figma or Balsamiq. This step allowed us to create a more structured layout with defined elements while maintaining a focus on functionality over aesthetics.\n"
        "3. **Feedback and Iteration**: We conducted user testing sessions with peers to gather feedback on the wireframes. Participants provided insights into usability, layout preferences, and potential navigation issues. Based on this feedback, we iteratively improved our designs."
    )
    st.markdown("<h2 style='font-size: 26px;'>Outcomes</h2>", unsafe_allow_html=True)
    st.write(
        "The low-fidelity prototypes enabled us to effectively communicate our design ideas and gather early feedback. This iterative process not only enhanced our understanding of user needs but also served as a foundation for developing high-fidelity prototypes in subsequent assignments."
    )
    st.markdown("[Assignment 4 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)

elif page == "Assignment 5: High fidelity design":
    st.title("Assignment 5: High fidelity design")
    st.write(
        "In this assignment, we developed high-fidelity prototypes for the AI-Based Skill Assessment System. High-fidelity designs incorporate detailed visual elements and interactions, closely resembling the final product."
    )
    st.markdown("<h2 style='font-size: 26px;'>Process</h2>", unsafe_allow_html=True)
    st.write(
        "1. **Visual Design**: Building on our low-fidelity prototypes, we focused on creating visually appealing interfaces. This included selecting color schemes, typography, and icons that align with our target audience and branding.\n"
        "2. **Interactive Prototyping**: Using tools like Figma or Adobe XD, we transformed static screens into interactive prototypes. This enabled users to navigate through the application and experience its functionality as they would in a live environment.\n"
        "3. **User Testing**: We conducted usability testing sessions with potential users to gather feedback on the high-fidelity prototypes. Observing how users interacted with the design allowed us to identify any usability issues or areas for improvement."
    )
    st.markdown("<h2 style='font-size: 26px;'>Outcomes</h2>", unsafe_allow_html=True)
    st.write(
        "The high-fidelity prototypes provided a realistic representation of the system, enabling us to validate design choices and gather comprehensive user feedback. This phase was crucial for ensuring that the final product aligns with user expectations and requirements."
    )
    st.markdown("[Assignment 5 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)

elif page == "Assignment 6: prototype design":
    st.title("Assignment 6: prototype design")
    st.write(
        "In this assignment, we developed a high-fidelity prototype of the AI-Based Skill Assessment System. The goal was to translate our low-fidelity designs into a more polished and interactive representation of the system, ensuring that all user requirements and feedback from previous assignments were incorporated."
    )
    st.write(
        "The prototype was created using design tools that allowed us to simulate user interactions, providing a realistic experience of how the system will function. This phase involved:"
    )
    st.markdown("""
    <ul style="font-size: 16px;">
        <li>Integrating visual elements such as color schemes, typography, and icons that align with the branding and usability principles.</li>
        <li>Defining user flows and navigation paths to ensure intuitive access to all features of the system.</li>
        <li>Conducting usability testing sessions to gather feedback on the prototype and make necessary refinements.</li>
        <li>Iterating on the design based on user feedback to enhance the overall user experience.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.write(
        "By the end of this assignment, we aimed to have a functional prototype that not only looks appealing but also meets the usability standards necessary for effective interaction. This prototype serves as a crucial step before the final implementation of the system."
    )
    st.markdown("[Assignment 6 Report](https://drive.google.com/your-link)", unsafe_allow_html=True)

# Team Members Section
elif page == "Team Members":
    st.title("Team Members")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("./images/vivek.jpeg", width=150)
        st.write("Name: Vivek Pahilwan")
        st.write("Roll No: 331071")
        st.write("PRN: 22320030")
    
    with col2:
        st.image("./images/mansi.jpeg", width=150)
        st.write("Name: Manasi Hire")
        st.write("Roll No: 331070")
        st.write("PRN: 22320015")
    
    with col3:
        st.image("./images/janhavi.jpeg", width=150)
        st.write("Name: Janhavi Hire")
        st.write("Roll No: 332069")
        st.write("PRN: 22320016")
    
    with col4:
        st.image("./images/dhiraj.jpeg", width=150)
        st.write("Name: Dhiraj Wagh")
        st.write("Roll No: 331072")
        st.write("PRN: 22320044")
