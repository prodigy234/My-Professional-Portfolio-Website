import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Kajola Gbenga | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# HEADER SECTION
# -----------------------------
st.markdown(
    """
    <h1 style='text-align:center;'>Kajola Gbenga Adewale</h1>
    <h4 style='text-align:center; color:gray;'>
    Data Analyst | Financial Data Scientist | Business Intelligence Specialist
    </h4>
    <p style='text-align:center;'>
    One-stop access to my professional profiles, dashboards, and analytical projects.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# PROFESSIONAL LINKS
# -----------------------------
st.subheader("🔗 Professional Profiles")

profile_links = {
    "LinkedIn": "www.linkedin.com/in/kajolagbenga/",
    # "Portfolio Website": "https://your-portfolio-link.com",
    "Email": "mailto:k.gbenga234@gmail.com"
}

cols = st.columns(len(profile_links))

for col, (name, link) in zip(cols, profile_links.items()):
    with col:
        st.markdown(
            f"""
            <a href="{link}" target="_blank">
                <button style="
                    width:100%;
                    padding:12px;
                    font-size:16px;
                    border-radius:8px;
                    border:1px solid #ddd;
                    cursor:pointer;">
                    {name}
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

st.divider()

# -----------------------------
# DASHBOARDS & SYSTEMS
# -----------------------------
st.subheader("📈 Dashboards & Business Intelligence Systems")

dashboards = {
    "MTN H1 2025 Analytical Project": "https://mtnanalytics.streamlit.app",
    "Nigerian Breweries Executive Strategy System": "https://nigerianbreweries.streamlit.app/",
    "UMÉRA Investors Portfolio": "https://umerainvestors.streamlit.app/",
    "Sales Performance Dashboard": "https://salesperformance.streamlit.app/",
    "UMeRA Royal Palm Investor Analytics": "https://umerainvestors.streamlit.app/",
    "UMeRA Royal Palm Customer Age Segmentation Analytics": "https://umerainvestments.streamlit.app/",
    "Brent Superstore Interactive Dashboard": "https://brentsuperstore.streamlit.app/",
    "HR Employee Attrition Dashboard": "https://ibmhrdashboard.streamlit.app/",
    "Amazon Sales Analytics Dashboard": "https://amazonanalytics.streamlit.app/"
}

for name, link in dashboards.items():
    st.markdown(f"👉 **[{name}]({link})**", unsafe_allow_html=True)

st.divider()

# -----------------------------
# DATA SCIENCE & AI PROJECTS
# -----------------------------
st.subheader("🤖 Data Science & AI Projects")

projects = {
    "AI-powered ATS Resume Screener": "https://vibriss.streamlit.app/",
    "Fraud Detection System (XGBoost)": "https://checkfraud.streamlit.app/",
    "Advanced Heart Disease Risk Analysis": "https://heartanalytics.streamlit.app/",
    "Sales Modelling Project": "https://salesmodelling.streamlit.app/",
    "AI-enabled Resume Builder": "https://buildcv.streamlit.app/"
}

left_col, right_col = st.columns(2)

for i, (name, link) in enumerate(projects.items()):
    if i % 2 == 0:
        left_col.markdown(f"✅ **[{name}]({link})**", unsafe_allow_html=True)
    else:
        right_col.markdown(f"✅ **[{name}]({link})**", unsafe_allow_html=True)

st.divider()

# -----------------------------
# MARKETING & PRODUCT ANALYTICS
# -----------------------------
st.subheader("📊 Marketing & Product Analytics")

marketing_projects = {
    "iFOOD Campaign Marketing Optimization": "https://ifoodanalytics.streamlit.app/",
    "Product Intelligence Analytics": "https://amazonprescriptivedashboard.streamlit.app/",
    "UMÉRA Affiliates Dashboard": "https://umeraaffiliates.streamlit.app/",
    "iNICHOLAS Sales Analytics": "https://inicholas.streamlit.app/"
}

for name, link in marketing_projects.items():
    st.markdown(f"📌 **[{name}]({link})**", unsafe_allow_html=True)

st.divider()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    """
    <p style='text-align:center; color:gray; font-size:14px;'>
    © 2026 Kajola Gbenga Adewale | Built with Streamlit 🚀
    </p>
    """,
    unsafe_allow_html=True
)
