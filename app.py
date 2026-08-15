import streamlit as st

# Custom CSS for UI Enhancement
st.markdown(
    """
    <style>
    /* Main container padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    /* Hero Banner Gradient Styling */
    .hero-banner {
        background: linear-gradient(135deg, #7A0000 0%, #4A0000 100%);
        color: white;
        padding: 2.5rem 1.5rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
        margin-bottom: 2rem;
    }
    .hero-banner h1 {
        color: #FFD700 !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    .hero-banner h3 {
        color: #FFFFFF !important;
        font-size: 1.3rem !important;
        font-weight: 500 !important;
        margin-bottom: 0.5rem !important;
    }
    .hero-banner p {
        color: #E0E0E0 !important;
        font-size: 0.95rem !important;
        margin: 0 !important;
    }

    /* Modern Styled Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    div[data-testid="stMetricLabel"] {
        color: #64748B !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetricValue"] {
        color: #1E293B !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }

    /* Tabs Styling */
    button[data-baseweb="tab"] {
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
    }

    /* Input Field & Select Box Focus Styling */
    div[data-baseweb="select"] > div {
        border-radius: 8px !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 1. Sidebar Cleanup
with st.sidebar:
    st.header("⚙️ Settings")
    with st.expander("🔑 API Configuration", expanded=True):
        groq_api_key = st.text_input(
            "Groq API Key", type="password", help="Enter your Groq API key here"
        )

# 2. Custom Hero Banner HTML
st.markdown(
    """
    <div class="hero-banner">
        <h1>University of Central Punjab</h1>
        <h3>Student Career & Placement Portal</h3>
        <p>Empowering UCP Graduates for Professional Success</p>
    </div>
""",
    unsafe_allow_html=True,
)

# 3. Metrics Layout with Cards
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Active Job Listings", "120+")
with m2:
    st.metric("Hiring Partners", "85")
with m3:
    st.metric("Placement Rate", "92%")
with m4:
    st.metric("1-on-1 Sessions Done", "450+")

st.markdown("---")

# 4. Tabs & Form Section
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📋 Job & Internship Board",
        "📅 1-on-1 Advisory Sessions",
        "🤖 AI Career Assistant",
        "📚 Career Services & Resources",
    ]
)

with tab2:
    st.subheader("Book a Career Consultation")

    col1, col2 = st.columns([1, 1], gap="medium")

    with col1:
        advisor = st.selectbox(
            "Select Advisor:", ["Dr. Sarah Ahmed (Tech & Engineering)", "Prof. Ali Khan (Business & Marketing)"]
        )
        date = st.date_input("Select Date:")
        st.button("Confirm Booking", type="primary", use_container_width=True)

    with col2:
        st.info(
            "💡 **Advisor Info**\n\n"
            "Sessions are held virtually via **MS Teams** or in-person at the "
            "**UCP Career Services Office** (Building A, 2nd Floor)."
        )
