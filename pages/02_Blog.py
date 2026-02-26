import streamlit as st
from pathlib import Path
from PIL import Image

# --- CONFIGURAÇÕES GLOBAIS ---
PAGE_TITLE = "Digital CV | Juan G. Martins"
PAGE_ICON = "🎲" # Atualizado para um ícone de dados
NAME = "Juan Gonçalves Martins"
# Descrição atualizada conforme fonte [1]
DESCRIPTION = "Senior Data Scientist | Practical Machine Learning for real-world decisions"
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
}

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
base_dir = current_dir.parent  # Diretório base, acima de 'pages'

css_file = base_dir / "styles" / "main.css"
resume_file = base_dir / "assets" / "Juan Gonçalves Martins.docx"
profile_pic_path = base_dir / "assets" / "Profile.jpg"

# Configuração da página Streamlit
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Carregar CSS com verificação
if css_file.exists():
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Carregar PDF do currículo
PDFbyte = b""
if resume_file.exists():
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

# Carregar imagem de perfil
profile_pic = None
if profile_pic_path.exists():
    profile_pic = Image.open(profile_pic_path)

# --- SIDEBAR - BIO ATUALIZADA ---
# Texto baseado nas suas fontes [1, 2] enfatizando senioridade e filosofia
st.sidebar.markdown(f"### About Me")
st.sidebar.info("""
I work with Data Science focusing on clarity, structure, and real-world decision-making — not just models and metrics [1]. 

With **6 years of experience**, I’ve been involved in end-to-end data projects, from messy data and unclear questions to analyses that support business decisions [1]. 

**My Principles:**
- Understand the problem before the model.
- Data quality before performance metrics.
- Context before technique [2].
""")

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3], gap="small")
with col1:
    if profile_pic:
        st.image(profile_pic, width=230)
    else:
        st.write("📸 [Foto de Perfil]")

with col2:
    st.title(NAME)
    st.write(f"**{DESCRIPTION}**")
    st.write("📍 Rio de Janeiro, Brasil [1]")
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Juan_Martins_CV.docx",
        mime="application/octet-stream",
    )
    st.write(f"📫 {EMAIL}")

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(f"**[{platform}]({link})**")

# --- COMPETÊNCIAS PRINCIPAIS (Extraído das fontes [2-4]) ---
st.write('\n')
st.subheader("Key Expertise")
st.write("---")
st.markdown("""
- **Languages & Frameworks:** Python (Scikit-Learn, Pandas), SQL, PySpark, APIs [3, 4].
- **Data Science:** Machine Learning (Feature Engineering, Model Selection), Statistical Modeling, Clustering [2, 5].
- **Business Intelligence:** Power BI, Financial Data Modeling, NPS Analytics [2, 6].
""")

# --- PROJETOS E REALIZAÇÕES ---
st.write('\n')
st.subheader("Selected Projects & Publications")
st.write("---")
for project, link in PROJECTS.items():
    if link:
        st.write(f"[{project}]({link})")
    else:
        st.write(f"{project}")