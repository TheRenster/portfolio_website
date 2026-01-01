import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import base64
import os

# ==================== HEARTBEAT / UPTIME PING ====================
if st.query_params.get("ping") == ["true"]:
    st.write("OK")
    st.stop()
# ================================================================

# Page configuration
st.set_page_config(
    page_title="Lauren's Portfolio",
    page_icon="🪩",
    layout="wide"
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'About me'
if 'qa_expanded' not in st.session_state:
    st.session_state.qa_expanded = False
if 'verification_num1' not in st.session_state:
    st.session_state.verification_num1 = random.randint(1, 10)
    st.session_state.verification_num2 = random.randint(1, 10)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Main background */
    .main {
        background-color: #000000 !important;
    }
    
    .stApp {
        background-color: #000000;
    }
    
    /* Remove default Streamlit padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 100%;
    }
    
    /* Navigation buttons - fixed height to prevent jumping */
    .stButton button {
        background-color: #1a1a1a !important;
        color: white !important;
        border: 1px solid #333 !important;
        border-radius: 0px !important;
        padding: 10px 15px !important;
        font-size: 13px !important;
        transition: all 0.3s !important;
        width: 100% !important;
        height: 45px !important;
        box-sizing: border-box !important;
    }
    
    .stButton button:hover {
        background-color: #2a2a2a !important;
        border-color: #555 !important;
    }
    
    /* Text input and textarea styling */
    .stTextInput input, .stTextArea textarea {
        background-color: #1a1a1a !important;
        color: white !important;
        border: 1px solid #333 !important;
        border-radius: 0px !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Reduce column gap */
    [data-testid="column"] {
        padding: 0 3px;
    }
            
    /* Disable Streamlit header anchor/link icons */
    h1 a, h2 a, h3 a {
        display: none !important;
    }

    /* ===== PORTFOLIO STYLES ===== */

    .portfolio-section {
        max-width: 1100px;
        margin: auto;
        padding: 2rem 0;
    }

    .project {
        display: flex;
        align-items: center;
        gap: 3rem;
        margin-bottom: 4rem;
    }

    .project.reverse {
        flex-direction: row-reverse;
    }

    .project img {
        width: 100%;
        border-radius: 14px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.18);
    }

    .project-text h3 {
        margin-bottom: 0.25rem;
    }

    .project-text .dates {
        font-size: 0.9rem;
        opacity: 0.7;
        margin-bottom: 0.75rem;
    }

    .project-text p {
        line-height: 1.6;
        margin-bottom: 0.75rem;
    }

    .tech {
        font-size: 0.9rem;
        opacity: 0.85;
    }

    .project-links a {
        margin-right: 1rem;
        font-weight: 600;
        text-decoration: none;
    }

    @media (max-width: 900px) {
        .project,
        .project.reverse {
            flex-direction: column;
        }
    }

    </style>
    """, unsafe_allow_html=True)

# Function to create navigation
def create_navigation():
    tab_col1, tab_col2, tab_col3, tab_col4 = st.columns(4, gap="small")
    
    with tab_col1:
        if st.button("About me", key="about", use_container_width=True):
            st.session_state.page = 'About me'
            st.rerun()
    
    with tab_col2:
        if st.button("Resume", key="resume", use_container_width=True):
            st.session_state.page = 'Resume'
            st.rerun()
    
    with tab_col3:
        if st.button("Portfolio", key="portfolio", use_container_width=True):
            st.session_state.page = 'Portfolio'
            st.rerun()
    
    with tab_col4:
        if st.button("Contact Me", key="contact", use_container_width=True):
            st.session_state.page = 'Contact Me'
            st.rerun()

# Function to send email (protected)
def send_email(name, sender_email, subject, message):
    recipient = base64.b64decode("bGF1cmVuY2tub3hAZ21haWwuY29t").decode()

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "laurencknox@gmail.com"
    smtp_password = "xghq uarx wtul gasj"
    
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = recipient
    msg['Subject'] = f"Portfolio Contact: {subject}"
    body = f"From: {name}\nEmail: {sender_email}\n\n{message}"
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        return False

# ==================== ABOUT ME PAGE ====================
if st.session_state.page == 'About me':
    col_left, col_right = st.columns([1, 1], gap="large")
    
    with col_left:
        st.markdown("""
        <div style='background-color: #1a4d7a; padding: 30px 40px; margin-bottom: 30px; border-radius: 0px;'>
            <h2 style='color: white; font-style: italic; margin: 0; font-size: 24px; font-weight: 400; line-height: 1.6;'>"You're never given a dream without also being given the power to make it true."</h2>
            <p style='color: #e0e0e0; margin-top: 15px; margin-bottom: 0; font-size: 16px;'><strong>Richard Bach, Illusions: The Adventures of a Reluctant Messiah</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 40px; border-radius: 0px;'>
            <p style='color: #e0e0e0; font-size: 16px; line-height: 1.8; margin-bottom: 20px;'>
                Hi, my name is Lauren, and my dream is simple: I want to make the world a better place. I love people, I love problem solving, and I'm at my best where the two intersect.
            </p>
            <p style='color: #e0e0e0; font-size: 16px; line-height: 1.8; margin-bottom: 20px;'>
                I have a Master's in Data Analytics with dual emphases in FinTech and Machine Learning and Operations and a triple bachelor's degree in Economics, Data Analytics, and Finance. I chose each of these degrees carefully. Economics is the lens through which I see the world—how problems form and how solutions interact through tradeoffs. Finance gives me the language to quantify those solutions and test real possibilities. Data Analytics gives me the tools to tackle wicked problems and, just as importantly, to ask better questions.
            </p>
            <p style='color: #e0e0e0; font-size: 16px; line-height: 1.8; margin-bottom: 20px;'>
                My FinTech emphasis allowed me to explore more statistical simulations such as Monte Carlo, real options pricing, and binomial trees, while also developing an understanding of the fundamental economic concepts needed for a successful entrepreneur. Because of this training, I now identify as a Bayesian and am comfortable reasoning under uncertainty in a complex, evolving catallax.
            </p>
            <p style='color: #e0e0e0; font-size: 16px; line-height: 1.8; margin-bottom: 20px;'>
                Through my Machine Learning and Operations coursework, I learned forecasting methods and different statistical tools such as text mining, DNNs, RNNs, LSTMs, ARIMA, and more. Beyond implementation, I focused on understanding when and why these methods work, their limitations, and how to choose the right approach given data constraints and real-world uncertainty. This perspective allows me to build models that are not only accurate, but practical and decision-relevant.
            </p>
            <p style='color: #e0e0e0; font-size: 16px; line-height: 1.8; margin-bottom: 0;'>
                Together, these methods allow me to reason under uncertainty, forecast outcomes, and build solutions that are both technically rigorous and deeply human-centered.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        create_navigation()
        
        # Load and display photo
        photo_path = "250502_LO_Commencement_HSBUndergrad_P52A8882.jpg"
        if os.path.exists(photo_path):
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            st.image(photo_path, use_container_width=True)
        else:
            st.markdown("""
            <div style='background-color: #1a1a1a; padding: 40px; border-radius: 0px; text-align: center; margin-top: 20px; height: 755px; display: flex; align-items: center; justify-content: center;'>
                <div style='background-color: #2a2a2a; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; border-radius: 0px; color: #888; font-size: 18px;'>
                    Your Photo Here<br/>(Add 250502_LO_Commencement_HSBUndergrad_P52A8882.jpg to folder)
                </div>
            </div>
            """, unsafe_allow_html=True)

# ==================== RESUME PAGE ====================
elif st.session_state.page == 'Resume':
    col_left, col_right = st.columns([1, 1], gap="large")
    
    with col_left:
        st.write("")  # Empty placeholder
    
    with col_right:
        create_navigation()
    
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    
    # Centered resume content
    col_spacer1, col_resume, col_spacer2 = st.columns([1, 2, 1])
    
    with col_resume:
        # Header with download button
        header_col1, header_col2 = st.columns([3, 1])
        with header_col1:
            st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
            
            # Check if resume.pdf exists
        # Check if resume.pdf exists
        try:
            with open("resume.pdf", "rb") as pdf_file:
                pdf_data = pdf_file.read()
            st.download_button(
                label="Download Resume",
                data=pdf_data,
                file_name="Lauren_Knox_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        except FileNotFoundError:
            st.markdown("""
                <div style='background-color: #333; padding: 10px; text-align: center; border-radius: 0px;'>
                    <p style='color: #888; font-size: 12px; margin: 0;'>resume.pdf not found</p>
                </div>
            """, unsafe_allow_html=True)
        
        # Technical Skills
        st.markdown("<h2 style='color: #4a90e2; font-size: 20px; margin-top: 20px; margin-bottom: 15px; border-bottom: 2px solid #4a90e2; padding-bottom: 5px;'>Technical Skills</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #e0e0e0; line-height: 1.8;'><strong>Programming & Data:</strong> Python, SQL, Pandas, NumPy</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #e0e0e0; line-height: 1.8;'><strong>Modeling & Forecasting:</strong> Time Series Forecasting, Machine Learning, Econometrics, Monte Carlo Simulation</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #e0e0e0; line-height: 1.8;'><strong>Text Mining:</strong> NLP Pipelines, TF-IDF, Sentiment Analysis, Document Clustering, Word Embeddings, Transformers</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #e0e0e0; line-height: 1.8;'><strong>Data Engineering & Automation:</strong> Multi-Source Data Integration, Automated Reporting & Workflow Pipelines</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #e0e0e0; line-height: 1.8; margin-bottom: 25px;'><strong>Applications & Tools:</strong> Streamlit, Power BI, Tableau (Certified), Snowflake, Excel (Certified), AWS, WordPress</p>", unsafe_allow_html=True)
        
        # Projects
        st.markdown("<h2 style='color: #4a90e2; font-size: 20px; margin-bottom: 15px; border-bottom: 2px solid #4a90e2; padding-bottom: 5px;'>Projects</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: white; font-size: 17px; margin-bottom: 5px;'>Droplet: Tokenized Water Rights System</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #888; font-size: 14px; font-style: italic; margin-bottom: 10px;'>HackUSU - Awarded 3rd Place | March 2025</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #e0e0e0; line-height: 1.8; margin-bottom: 20px;'>Designed a blockchain-based water rights allocation model by deploying 1M ERC-20 tokens on Ethereum (Sepolia), proposing a market-driven governance framework that addresses regulatory, legal, and sustainability constraints in resource management.</p>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: white; font-size: 17px; margin-bottom: 5px;'>Clarity Context (NLP News Intelligence System)</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #888; font-size: 14px; font-style: italic; margin-bottom: 10px;'>December 2025</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #e0e0e0; line-height: 1.8; margin-bottom: 25px;'>Built an end-to-end NLP pipeline that ingests news from multiple APIs, preprocesses text, and applies TF-IDF, sentiment analysis, and document clustering to quantify sentiment intensity, sensationalism, and thematic structure across news sources.</p>", unsafe_allow_html=True)
        
        # Work Experience
        st.markdown("<h2 style='color: #4a90e2; font-size: 20px; margin-bottom: 15px; border-bottom: 2px solid #4a90e2; padding-bottom: 5px;'>Work Experience</h2>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: white; font-size: 17px; margin-bottom: 5px;'>Data Consultant</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #888; font-size: 14px; font-style: italic; margin-bottom: 10px;'>Analytics Solutions Center - Logan, Utah | August 2025 - Present</p>", unsafe_allow_html=True)
        st.markdown("""
        <ul style='color: #e0e0e0; line-height: 1.8; margin-left: 20px; margin-bottom: 20px;'>
            <li>Querying and extracting survey data from Metabase to evaluate dataset structure, completeness, and consistency across multiple data sources for the Data Quality Co-op (DQC).</li>
            <li>Engineering and evaluating data quality features capturing missingness, response patterns, outliers, and internal inconsistencies to construct a quantitative data quality scoring model.</li>
            <li>Validating data quality metrics using statistical diagnostics to assess how variations in data quality affect downstream analysis and research usability.</li>
            <li>Developing a text mining-based question answering system for USU Agriculture Extension offices, preprocessing unstructured text and organizing domain knowledge to support community-facing information access.</li>
        </ul>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: white; font-size: 17px; margin-bottom: 5px;'>Operations and Technology Specialist</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #888; font-size: 14px; font-style: italic; margin-bottom: 10px;'>Vibrant IP - Logan, Utah | June 2025 - December 2025</p>", unsafe_allow_html=True)
        st.markdown("""
        <ul style='color: #e0e0e0; line-height: 1.8; margin-left: 20px; margin-bottom: 20px;'>
            <li>Designed and implemented automated reporting and analytics workflows, replacing manual monthly processes with standardized dashboards and executive-ready reports for portfolio and marketing decisions.</li>
            <li>Built the company's first unified lead-intelligence system by consolidating and cleaning 400,000+ contacts across HubSpot, Apollo, and legacy trackers, significantly improving data quality and targeting.</li>
            <li>Developed internal operational dashboards with sortable fields, timestamps, and integrated analytics to track campaign performance, lead flow, and content effectiveness.</li>
            <li>Automated report generation and distribution pipelines, eliminating recurring errors, accelerating turnaround time, and removing 10+ hours of manual work per month.</li>
        </ul>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: white; font-size: 17px; margin-bottom: 5px;'>Data Analytics Intern</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #888; font-size: 14px; font-style: italic; margin-bottom: 10px;'>Lamb Weston - Kennewick, Washington | May 2024 - August 2024</p>", unsafe_allow_html=True)
        st.markdown("""
        <ul style='color: #e0e0e0; line-height: 1.8; margin-left: 20px; margin-bottom: 25px;'>
            <li>Analyzed financial and operational datasets (10M+ rows), documenting data models and improving data integrity while identifying key performance patterns.</li>
            <li>Rebuilt and transitioned enterprise reporting from DOMO to Power BI and Excel, modeling data relationships and delivering executive-ready dashboards to support business decision-making.</li>
            <li>Collaborated with cross-functional teams in a remote environment to validate reporting requirements, ensure data consistency, and support ongoing analytics initiatives.</li>
        </ul>
        """, unsafe_allow_html=True)
        
        # Education
        st.markdown("<h2 style='color: #4a90e2; font-size: 20px; margin-bottom: 15px; border-bottom: 2px solid #4a90e2; padding-bottom: 5px;'>Education</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: white; font-size: 17px; margin-bottom: 10px;'>Utah State University, Jon M. Huntsman School of Business</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #e0e0e0; line-height: 1.8; margin-bottom: 5px;'><strong>Masters of Data:</strong> Fintech and Machine Learning Operations emphases | May 2026</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #e0e0e0; line-height: 1.8; margin-bottom: 5px;'><strong>Triple Bachelor's of Science:</strong> Data Analytics, Economics, and Finance | May 2025</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #888; font-size: 14px;'>Dean's list (Spring 2022, Fall 2022, Spring 2023, Fall 2023, Spring 2024, Fall 2024, Spring 2025)</p>", unsafe_allow_html=True)
    
    # Empty spacers for other columns
    with col_spacer1:
        st.write("")
    with col_spacer2:
        st.write("")

# ==================== PORTFOLIO PAGE ====================
elif st.session_state.page == 'Portfolio':
    # 1. Navigation Header
    col_left, col_right = st.columns([1, 1], gap="large")
    with col_right:
        create_navigation()
    
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    # 2. Project Data List - Sorted by Date (Most Recent First)
# 2. Project Data List - Sorted by Date (Most Recent First)
    projects = [
        {
            "title": "Clarity Context (NLP Intelligence)",
            "date": "December 2025",
            "desc": "Built an end-to-end NLP pipeline that ingests news from multiple APIs, preprocesses text, and applies TF-IDF, sentiment analysis, and document clustering to quantify sentiment intensity, sensationalism, and thematic structure across news sources.",
            "skills": "NLP · Python · Data Engineering",
            "link": "https://clarity-context-app.streamlit.app/",  # Placeholder - you'll update once published
            "image": "clarity_context_logo.png"  # Placeholder - you'll update once published
        },
        {
            "title": "Forecasting Friend",
            "date": "December 2025",
            "desc": "Built a Streamlit app for time-series forecasting. Users upload data and compare Econometric, ML, and Deep Learning models using RMSE, MAE, and MAPE metrics.",
            "skills": "Streamlit · Time-Series · Machine Learning · Econometrics",
            "link": "https://deep-forecasting-renster.streamlit.app",
            "image": "ff_image.png"
        },
        {
            "title": "Droplet: Tokenized Water Rights",
            "date": "March 2025",
            "desc": "Designed and deployed 1 million DRP tokens using ERC-20 Solidity on Sepolia Ethereum. Awarded 3rd Place at HackUSU for modernizing Utah water rights management through blockchain governance.",
            "skills": "Blockchain · Solidity · Ethereum · Water Rights",
            "link": "droplet_portfolio.pdf",  # PDF file
            "image": "drp_image.png"
        },
        {
            "title": "Job–Candidate Fit Analysis Tool",
            "date": "December 2024",
            "desc": "Built an NLP-based system that analyzes resumes and ranks job postings based on candidate–job fit with interpretable scoring explaining matching criteria.",
            "skills": "NLP · Scikit-Learn · Text Matching",
            "link": "https://github.com/TheRenster/Projects_Demos/blob/main/Job_Alignment_Analysis.ipynb",
            "image": "job candidate fit analysis tool.png"
        },
        {
            "title": "Crypto Currency Arbitrage",
            "date": "November 2024",
            "desc": "Coded a Python arbitrage program on AWS tracking 6 currencies over 100 days. Implemented SMA and Mean Reversion strategies with simulations yielding up to $7,000 profit/day.",
            "skills": "Python · AWS · Trading Systems",
            "link": "https://github.com/TheRenster/Projects_Demos/blob/main/Crypto-Arbitrage",
            "image": "crypto arbitrage image.png"
        },
        {
            "title": "Dash n' Crash Inc.",
            "date": "December 2022",
            "desc": "Led a four-person team to create a comprehensive business plan and financial model for a student startup, including HR policies and risk management strategies.",
            "skills": "Business Strategy · Financial Forecasting · Leadership",
            "link": "Business Plan.docx",  # Word doc file
            "image": "dnc_image.png"
        }
    ]

    # 3. Render Projects with Alternating Layout
    for i, project in enumerate(projects):
        col1, col2 = st.columns([1, 1], gap="large")
        
    # Replace the existing image_html block with this:
        image_path = project['image'] # Example naming convention

        # Check if the file exists, otherwise use your placeholder
        if os.path.exists(image_path):
            image_html = f"""
                <div style="width: 100%; height: 300px; overflow: hidden; border-radius: 10px; border: 1px solid #333;">
                    <img src="data:image/png;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" 
                        style="width: 100%; height: 100%; object-fit: contain;">
                </div>
            """
        else:
            # This is your existing placeholder fallback
            image_html = f"""
                <div style="width: 100%; height: 300px; background-color: #1e1e1e; 
                    border-radius: 10px; display: flex; align-items: center; 
                    justify-content: center; border: 1px dashed #4a90e2;">
                    <p style="color: #4a90e2; font-family: sans-serif; font-size: 14px;">{project['title']} Image Not Found</p>
                </div>
            """
            
        # Text Content HTML
        text_html = f"""
            <h2 style='color: #4a90e2; font-size: 24px; margin-bottom: 5px; font-family: sans-serif;'>{project['title']}</h2>
            <p style='color: #888; font-style: italic; font-size: 14px; margin-bottom: 15px; font-family: sans-serif;'>{project['date']}</p>
            <p style='color: #e0e0e0; line-height: 1.6; font-size: 15px; font-family: sans-serif;'>{project['desc']}</p>
            <p style='color: #4a90e2; font-weight: bold; font-size: 14px; font-family: sans-serif; margin-top: 10px;'>{project['skills']}</p>
        """

        if i % 2 == 0:
                    with col1:
                        st.markdown(image_html, unsafe_allow_html=True)
                    with col2:
                        st.markdown(text_html, unsafe_allow_html=True)
                        if project['link'] != "#":
                            # Handle PDF and DOCX files differently
                            if project['link'].endswith('.pdf') or project['link'].endswith('.docx'):
                                if os.path.exists(project['link']):
                                    with open(project['link'], "rb") as file:
                                        st.download_button(
                                            "View Project", 
                                            data=file, 
                                            file_name=project['link'],
                                            mime="application/pdf" if project['link'].endswith('.pdf') else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                                        )
                            else:
                                st.link_button("View Project", project['link'])
        else:
            with col1:
                st.markdown(text_html, unsafe_allow_html=True)
                if project['link'] != "#":
                    # Handle PDF and DOCX files differently
                    if project['link'].endswith('.pdf') or project['link'].endswith('.docx'):
                        if os.path.exists(project['link']):
                            with open(project['link'], "rb") as file:
                                st.download_button(
                                    "View Project", 
                                    data=file, 
                                    file_name=project['link'],
                                    mime="application/pdf" if project['link'].endswith('.pdf') else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                                )
                    else:
                        st.link_button("View Project", project['link'])
            with col2:
                st.markdown(image_html, unsafe_allow_html=True)
        
        # Space between projects
        st.markdown("<div style='margin-bottom: 80px;'></div>", unsafe_allow_html=True)

# ==================== CONTACT PAGE ====================
elif st.session_state.page == 'Contact Me':
    col_left, col_right = st.columns([1, 1], gap="large")
    
    with col_left:
        st.write("")  # Empty placeholder
    
    with col_right:
        create_navigation()
    
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    
    # Centered content
    col_spacer1, col_center, col_spacer2 = st.columns([1, 2, 1])
    
    with col_center:
        # Contact Form
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 0px; border-radius: 0px;'>
            <h2 style='color: white; margin-bottom: 10px; font-size: 22px;'>Send Me a Message</h2>
        """, unsafe_allow_html=True)
        
        name = st.text_input("Your Name", key="contact_name", placeholder="John Doe")
        email = st.text_input("Your Email", key="contact_email", placeholder="john@example.com")
        subject = st.text_input("Subject", key="contact_subject", placeholder="Let's connect!")
        message = st.text_area("Message", key="contact_message", placeholder="Your message here...", height=150)
        
        # Human verification
        st.markdown(f"<p style='color: #e0e0e0; margin-top: 20px; margin-bottom: 10px;'><strong>Human Verification:</strong> What is {st.session_state.verification_num1} + {st.session_state.verification_num2}?</p>", unsafe_allow_html=True)
        verification = st.text_input("Your answer:", key="verification", placeholder="Enter the sum")
        
        if st.button("Submit", key="submit_contact", use_container_width=True):
            if not name or not email or not subject or not message:
                st.error("Please fill in all fields")
            elif not verification or int(verification) != (st.session_state.verification_num1 + st.session_state.verification_num2):
                st.error("Incorrect verification answer. Please try again.")
            else:
                success = send_email(name, email, subject, message)
                if success:
                    st.success("Message sent successfully! I'll get back to you soon.")
                    st.session_state.verification_num1 = random.randint(1, 10)
                    st.session_state.verification_num2 = random.randint(1, 10)
                else:
                    st.warning("Email sending failed. Please try again or contact me directly.")
        
        # LinkedIn and GitHub links
        st.markdown("<div style='margin-top: 30px; text-align: center;'>", unsafe_allow_html=True)
        link_col1, link_col2 = st.columns(2)
        with link_col1:
            st.markdown("<a href='https://www.linkedin.com/in/lauren-knox303/' target='_blank' style='text-decoration: none; color: #4a90e2; font-size: 16px;'>LinkedIn</a>", unsafe_allow_html=True)
        with link_col2:
            st.markdown("<a href='https://github.com/TheRenster' target='_blank' style='text-decoration: none; color: #4a90e2; font-size: 16px;'>GitHub</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Empty spacers for other columns
    with col_spacer1:
        st.write("")
    with col_spacer2:
        st.write("")
