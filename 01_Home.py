from pathlib import Path
import streamlit as st
from PIL import Image

# Paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Juan Gonçalves Martins.pdf"
profile_pic_path = current_dir.parent / "assets" / "Profile.jpg"


# General settings
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
    "🏆 Medical Cost - Linear Regression": "https://www.linkedin.com/posts/juangmartins_medical-cost-activity-7198140280246558720-hOrb?utm_source=share&utm_medium=member_desktop",
    "🏆 Read Multi Files": "https://www.linkedin.com/posts/juangmartins_readmultifiles-activity-7185405507786993664-Oae_?utm_source=share&utm_medium=member_desktop",
    "🏆 In progress...": ""
}

# Setting page configuration
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Sidebar - perfil
myprofile = """
I'm a passionate data scientist with years of experience turning complex data into valuable insights. Skilled in Python, SQL, and data visualization, I have a strong background in statistics, mathematics, and computer science.
Always eager to improve and stay updated with trends, I enjoy collaborating and sharing knowledge. Open to new opportunities and challenges, feel free to reach out!
"""
st.sidebar.markdown(myprofile)

# Load CSS, PDF & profile picture
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_path)

# Hero section
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

# Social links
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Projects & Accomplishments
st.write('\n')
st.subheader("Blog")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
