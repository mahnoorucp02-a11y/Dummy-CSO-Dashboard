# app.py
import streamlit as st
import pandas as pd
from groq import Groq
from data import FACULTIES, JOB_LISTINGS, COUNSELORS

# Page Configuration
st.set_page_config(
    page_title="UCP Student Career & Placement Portal",
    page_icon="🎓",
    layout="wide"
)

# UCP Custom Branding CSS
st.markdown("""
    
""", unsafe_allow_html=True)

# Header / Hero Section
st.markdown("""
    
        University of Central Punjab
        Student Career & Placement Portal
        Empowering UCP Graduates for Professional Success
    
""", unsafe_allow_html=True)

# Key Statistics Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Active Job Listings", value="120+")
col2.metric(label="Hiring Partners", value="85")
col3.metric(label="Placement Rate", value="92%")
col4.metric(label="1-on-1 Sessions Done", value="450+")

st.markdown("---")

# Sidebar: Groq API Key Setup
st.sidebar.image("https://raw.githubusercontent.com/streamlit/streamlit/main/docs/static/logo.png", width=120)
st.sidebar.title("Configuration")

# Retrieve key from st.secrets if available, else require manual entry
api_key_input = st.sidebar.text_input(
    "Groq API Key",
    type="password",
    value=st.secrets.get("GROQ_API_KEY", ""),
    help="Enter your Groq API key for the AI Career Assistant."
)

# Main Tabs Navigation
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Job & Internship Board",
    "📅 1-on-1 Advisory Sessions",
    "🤖 AI Career Assistant",
    "📚 Career Services & Resources"
])

# TAB 1: Job & Internship Board
with tab1:
    st.subheader("Faculty-Wise Opportunities")
    selected_faculty = st.selectbox("Select Faculty:", FACULTIES)
    
    listings = JOB_LISTINGS.get(selected_faculty, [])
    st.write(f"Showing **{len(listings)}** listings for **{selected_faculty}**:")
    
    for job in listings:
        with st.expander(f"📌 {job['title']} — {job['company']} ({job['type']})"):
            st.write(f"**Location:** {job['location']}")
            st.write(f"**Application Deadline:** {job['deadline']}")
            st.write(f"**Requirements:** {job['reqs']}")
            
            # Apply Modal Form
            with st.form(key=f"apply_form_{job['id']}"):
                st.subheader("Apply for this Position")
                student_name = st.text_input("Full Name")
                student_email = st.text_input("UCP Student Email")
                student_roll = st.text_input("Roll Number (e.g., L1F20BSCS0000)")
                resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
                
                submitted = st.form_submit_button("Submit Application")
                if submitted:
                    if student_name and student_email and resume:
                        st.success(f"Application submitted successfully for {job['title']}! Confirmation sent to {student_email}.")
                    else:
                        st.error("Please fill in all details and upload your resume.")

# TAB 2: 1-on-1 Advisory Sessions
with tab2:
    st.subheader("Book a Career Consultation")
    c1, c2 = st.columns(2)
    
    with c1:
        selected_counselor = st.selectbox("Select Advisor:", [c["name"] + f" ({c['specialty']})" for c in COUNSELORS])
        session_topic = st.selectbox("Session Topic:", [
            "Resume & CV Review",
            "Mock Technical/HR Interview",
            "Career Path Counseling",
            "LinkedIn Profile Optimization"
        ])
        booking_date = st.date_input("Preferred Date")
        booking_time = st.time_input("Preferred Time")
        
    with c2:
        st.info("💡 **Advisor Info**\nSessions are held virtually via MS Teams or in-person at the UCP Career Services Office (Building A, 2nd Floor).")
        notes = st.text_area("Specific Notes or Questions for Counselor:")
        if st.button("Confirm Booking"):
            st.balloons()
            st.success(f"Booking Confirmed with {selected_counselor} on {booking_date} at {booking_time}!")

# TAB 3: AI Career Assistant (Groq API)
with tab3:
    st.subheader("UCP AI Career Assistant")
    st.caption("Powered by Groq API — Ask questions about resume crafting, interview tips, or career guidance.")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am your UCP AI Career Assistant. How can I help prepare you for your job search today?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Ask a question..."):
        if not api_key_input:
            st.error("Please enter your Groq API Key in the sidebar to use the AI assistant.")
        else:
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            try:
                client = Groq(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are an expert career counselor at the University of Central Punjab (UCP). Provide concise, encouraging, and actionable advice tailored to university students."}
                    ] + st.session_state.messages
                )
                ai_reply = response.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                st.chat_message("assistant").write(ai_reply)
            except Exception as e:
                st.error(f"Error communicating with Groq API: {str(e)}")

# TAB 4: Student Career Services & Resources
with tab4:
    st.subheader("Downloads & Campus Placement Drives")
    r1, r2 = st.columns(2)
    
    with r1:
        st.markdown("### 📄 Resume & CV Templates")
        st.download_button("Download Standard UCP Resume Template (.docx)", data="Sample Template Content", file_name="UCP_Resume_Template.docx")
        st.download_button("Download Tech/CS Resume Template (.docx)", data="Sample Tech Template Content", file_name="UCP_Tech_Resume_Template.docx")
        
    with r2:
        st.markdown("### 🗓️ Upcoming Campus Drives")
        events_df = pd.DataFrame([
            {"Company": "Systems Ltd", "Date": "2026-09-05", "Venue": "Auditorium 1"},
            {"Company": "NetSol Technologies", "Date": "2026-09-12", "Venue": "Auditorium 2"},
            {"Company": "KPMG Pakistan", "Date": "2026-09-18", "Venue": "Executive Hall"}
        ])
        st.table(events_df)
