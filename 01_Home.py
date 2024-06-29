from pathlib import Path

import streamlit as st
from PIL import Image
#git remote add origin https://github.com/JuanGonccalves/MyPortifolio.git
#git remote set-url origin https://github.com/JuanGonccalves/MyPortifolio.git


primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Juan Gonçalves Martins.pdf"
profile_pic_path = current_dir / "assets" / "Profile.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Juan G. Martins"
PAGE_ICON = ":wave:"
NAME = "Juan Gonçalves Martins"
DESCRIPTION = """
🎲 Data Scientist | Machine Learning | Python | SQL
"""
EMAIL = "juangoncalves482@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/juangmartins/",
    "GitHub": "https://github.com/JuanGonccalves",
    "Twitter": "https://x.com/Juan10941907",
}
PROJECTS = {
    "🏆 House Sales in King County, USA": "https://github.com/JuanGonccalves/House",
    "🏆 Medical Cost - Linear Regression": "https://github.com/JuanGonccalves/Medical_Cost",
    "🏆 Read Multi Files": "https://github.com/JuanGonccalves/ReadMultiFiles"
    }

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
myprofile = """
I'm a passionate data scientist with years of experience turning complex data into valuable insights. Skilled in Python, SQL, and data visualization, I have a strong background in statistics, mathematics, and computer science.

Always eager to improve and stay updated with trends, I enjoy collaborating and sharing knowledge. Open to new opportunities and challenges, feel free to reach out!
"""
st.sidebar.markdown(myprofile)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 Years expereince extracting actionable insights from data
- ✔️ Using Python, Power BI and Excel for Data science and Data analysis.
- ✔️ Good understanding of statistical principles and their respective applications
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 🧑🏽‍💻 Programming: Python (Scikit-learn, Statsmodels, Numpy, Pandas and others), SQL.
- 📊 Data Visulization: PowerBi, Looker (Google Data Studio), Excel.
- 📚 Modeling: Logistic regression, linear regression, decition trees.
- 🗄️ Databases: SQL server, Sqlite and others.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🧑🏽‍💻", "**Pleno Data Analyst | Education**")
st.write("09/2022 - Present")
st.write(
    """
- ► Used Python for extracting financial data from SAP.
- ► Data modeling with Python to present financial controls.
- ► Public data webscraping and database storage for market research.
"""
)

# --- JOB 2
st.write('\n')
st.write("🧑🏽‍💻", "**Business Intelligence Consultant**")
st.write("01/2021 - 12/2021")
st.write(
    """
- ► Development of management reports in power BI - KPI's and OKR's.
- ► Data modeling using sql for data analysis.
"""
)

# --- JOB 3
#st.write('\n')
#st.write("🚧", "**Data Analyst | Chegg**")
#st.write("04/2015 - 01/2018")
#st.write(
#    """
#- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
#- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
#- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
#"""
#)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
