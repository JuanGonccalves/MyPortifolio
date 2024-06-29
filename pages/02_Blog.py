import streamlit as st
from pathlib import Path
from PIL import Image

# Configurações globais
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
    "🏆 House Sales in King County, USA": "https://www.linkedin.com/posts/juangmartins_previs%C3%A3o-de-pre%C3%A7os-de-casas-em-king-county-activity-7209906015184605184-33oh?utm_source=share&utm_medium=member_desktop",
    "🏆 Medical Cost - Linear Regression": "https://www.linkedin.com/posts/juangmartins_medical-cost-activity-7198140280246558720-hOrb?utm_source=share&utm_medium=member_desktop",
    "🏆 Read Multi Files": "https://www.linkedin.com/posts/juangmartins_readmultifiles-activity-7185405507786993664-Oae_?utm_source=share&utm_medium=member_desktop",
    "🏆 In progress...": ""
}

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
base_dir = current_dir.parent  # Diretório base, acima de 'pages'

css_file = base_dir / "styles" / "main.css"
resume_file = base_dir / "assets" / "Juan Gonçalves Martins.pdf"
profile_pic_path = base_dir / "assets" / "Profile.jpg"

# Configuração da página Streamlit
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Carregar CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Carregar PDF do currículo
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Carregar imagem de perfil
profile_pic = Image.open(profile_pic_path)

# Sidebar - perfil
st.sidebar.markdown("""
I'm a passionate data scientist with years of experience turning complex data into valuable insights. Skilled in Python, SQL, and data visualization, I have a strong background in statistics, mathematics, and computer science.
Always eager to improve and stay updated with trends, I enjoy collaborating and sharing knowledge. Open to new opportunities and challenges, feel free to reach out!
""")

# Seção principal - herói
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

# Links sociais
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Projetos e realizações
st.write('\n')
st.subheader("Blog")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
