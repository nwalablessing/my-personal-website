import streamlit as st
from PIL import Image

# Custom Orange Header
st.markdown(
    """
    <style>
    .orange-header {
        background-color: #FFA500;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    .orange-header h1 {
        color: white;
        margin: 0;
        font-size: 28px;
    }
    </style>
    <div class="orange-header">
        <h1>Welcome to My Personal Website!</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Subheader
st.subheader("Hi, I’m Nwala Blessing Uchechi 👩‍💻")

# Introduction Section with Picture on the Left
st.header("About Me")
col1, col2 = st.columns([1, 2])  # Adjust column widths
with col1:
    # Use the relative file path for the image
    image = Image.open("GREAT_9069.jpg")
    st.image(image, caption="Blessing Uchechi Nwala", use_container_width=True)
with col2:
    st.write(
        """
        Hello! My name is **Nwala Blessing Uchechi**, a passionate **Computer Engineer**.  
        I am driven by my love for **technology**, **coding**, **cooking**, and **travelling**. 
        I come from a family of six with three amazing brothers and loving parents, **Mr. and Mrs. Nwala**.  

        In 2020, my team and i won the HUAWEI 2020 global ICT competition.
        """
    )

# Mission and Vision Statements
st.header("Mission Statement")
st.write("To leverage technology to solve real-world problems and create innovative solutions that empower communities globally.")

st.header("Vision Statement")
st.write("To be a global leader in technological innovation, making a positive impact across various industries while inspiring the next generation of engineers.")

# Professional Summary
st.header("Professional Summary")
st.write(
    """
    I am a graduate student in **Computer Science** specializing in **Cybersecurity and Digital Forensics**.  
    I have a deep expertise in **data analysis**, **machine learning**, and **data visualization**, complemented by strong proficiency in **cybersecurity practices**.  
    I excel at predictive modeling, data preprocessing, and applying advanced algorithms like **random forest**, XGBoost and **linear regression** 
    to derive actionable insights from complex datasets.  

    My cybersecurity skills include **threat detection**, **vulnerability assessments**, and **incident response planning**.  
    I am experienced in **network security** design, **firewall implementation**, and performing **digital forensic investigations** using tools like **Autopsy** and **Magnet Axiom**.  
    With hands-on experience in **cyber defense strategies** and **risk analysis**, I aim to create secure, innovative solutions that protect and optimize real-world systems and processes.  
    """
)

# Educational Background Section
st.header("Educational Background")
st.write(
    """
    - **Clitter House Infant and Junior School** (2001–2007)  
    - **Brainfield Secondary School** (2008–2012)  
    - **All Nations University**  
      - **Bachelor of Engineering in Computer Engineering** (2013–2017)  
    - **University of Port Harcourt**  
      - **Master of Science in Computer Science** (2018–2023)  
    - **Bowling Green State University, USA**  
      - Currently pursuing a **Master of Science in Cybersecurity and Digital Forensics** (2023–2025)  
    """
)

# Hobbies Section
st.header("Hobbies")
st.write(
    """
    - Cooking and experimenting with new meals  
    - Traveling and exploring different cultures  
    - Coding and working on innovative projects  
    - Staying updated with advancements in technology  
    """
)

# Travel Section
st.header("Countries I've Traveled To")
st.write("Ghana, Togo, Benin Republic, Germany, Qatar (Doha), USA")
st.subheader("Countries I Wish to Explore")
st.write("All countries in **Europe**, **Asia**, **Africa**, **North America**, **Australia** and **South America**.")

# Certificates Section
st.header("Certificates")
st.write(
    """
    - **IBM Cybersecurity Analyst** (02/2024)  
    - **CPR/First Aid Certification** (01/2024)  
    - **Project Management Certification** (01/2019)  
    - **HSE Level 1, 2, 3** (01/2019)  
    - **Environmental Impact Assessment** (11/2018)  
    - **Quality Management Certification** (01/2019)  
    - **Data Science Tools Certification** (12/2020)  
    - **Diploma in Data Service** (12/2020)  
    - **Diploma in Robotic Process Automation** (12/2020)  
    - **IBM Python for Data Science Certification** (09/2020)  
    - **IEEE Robotics and Raspberry Pi Certification** (03/2014)  
    - **Computer Networking – Digital Network Security** (04/2020)  
    - **The COSHH365 Software Certification** (05/2020)  
    """
)

# Career Aspiration Section
st.header("Career Aspiration")
st.write(
    """
    I aim to **invest in technology** to impact sectors such as:  
    - Agriculture and Farming  
    - Health  
    - Aviation  
    - Construction and Real Estate  
    - Fashion and Clothing  
    - Entertainment  
    - Food and Nutrition  
    - Economics  
    - Geography  
    - Information Technology  

    My vision is to use technology to drive transformation and innovation across the globe.  
    """
)

# Work Experience Section (Expanded Cybersecurity Roles)
st.header("Work Experience")
st.write(
    """
    - **Computer Technician**, Bowling Green State University, USA (08/2024 – 04/2025)  
      - I managed computerized manikins in simulation labs and maintained their optimal functionality.  
      - I performed cybersecurity monitoring and resolved network vulnerabilities in the simulation labs.  
      - I conducted data analysis and visualizations to enhance system performance and security.

    - **IT Support Engineer**, Julius Berger (10/2021 – 08/2023)  
      - I managed and maintained the company’s IT infrastructure, ensuring seamless operations across systems and networks.
      - I provided technical support by troubleshooting and resolving hardware, software, and network issues hereby ensuring minimal downtime for employees.
      - I administered user access control, ensuring that sensitive data and systems were secure from unauthorized access by setting up accounts and managing permissions.
      - I proactively monitored network and system performance, identifying and resolving potential issues before they impacted operations, ensuring a smooth workflow across the organization.
      


    - **Data Engineer**, PJ Rapha Care Limited (09/2019 – 10/2021)  
      - I collected and analyzed patient data from antenatal visits, tracking vital signs, health progress, and trends from the first visit to delivery using charts and graphs.  
      - I monitored patient records across ICU, male, female, and children’s wards, analyzing visit frequency, reasons for admission, and health outcomes over time.
      - I developed visual reports using data visualization tools to assess patient improvement, risk factors, and overall hospital admission trends.
      - I performed statistical analysis on maternal health data to identify patterns in pregnancy outcomes and antenatal care effectiveness.
      - I streamlined hospital data management by organizing large patient datasets, ensuring accuracy, consistency, and easy retrieval for decision-making.

    - **Computer Engineer**, OCDA (11/2017 – 11/2018)  
      - Provided support for IT infrastructure and implemented **cyber defense protocols**.  
      - Conducted **vulnerability testing** and protected sensitive urban development data.  
    """
)

# Projects Section
st.header("Projects")
st.write(
    """
    - **Advanced Machine Learning Framework for Real-Time Sepsis Prediction** (2025)  
    - **Adaptive Color Quantization for Efficient Image Compression Using Convolutional Autoencoders** (2024)  
    - **Comprehensive Analysis of Chemical Components in Wetland Pools** (2023)  
    - **Fuzzy-Logic Based Model for Remote Livestock Farming Monitoring** (2021)  
    - **Smart Walking Stick for Visually Impaired Patients** (2017)  
    """
)

# Skills and Expertise Section
st.header("Skills and Expertise")
st.write(
    """
    - **Cybersecurity Expertise:** Threat detection, Incident Response, Digital Forensics, Network Security  
    - Data Analysis, Machine Learning, and Predictive Modeling  
    - Programming: Python, TensorFlow, PyTorch, Java, C++  
    - Cybersecurity Tools: Firewalls, Encryption, Autopsy, Magnet Axiom  
    - Data Visualization and Spatial Analysis (ArcGIS, QGIS, ENVI, Google Earth Engine)  
    - Embedded Systems, Remote Sensing, and Image Processing  
    - Network Administration and IT Infrastructure Management  
    """
)

# Contact Section
st.header("Get in Touch")
st.write(
    """
    - 📧 Email: nwalablessing0@gmail.com  
    - 🌐 GitHub: [github.com/nwalablessing](https://github.com/nwalablessing)  
    - 🔗 LinkedIn: [linkedin.com/in/blessing-nwala-319012118](https://linkedin.com/in/blessing-nwala-319012118)  
    """
)

# Footer
st.write("---")
st.write("© 2025 Nwala Blessing Uchechi | All Rights Reserved.")
