import streamlit as st
from PIL import Image
from pathlib import Path

# --- CONFIGURAÇÕES DE PÁGINA ---
st.set_page_config(page_title="Digital CV | Juan G. Martins", page_icon="🎲", layout="wide")

# --- CARREGAMENTO DE ATIVOS (Simulado conforme seu código original) ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "Juan Gonçalves Martins.docx"
profile_pic_path = current_dir / "assets" / "Profile.jpg"

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="large")
with col1:
    st.image(profile_pic_path, width=230) # Descomente para usar sua foto
    # st.markdown("### 📸 [Sua Foto Aqui]")

with col2:
    st.title("Juan Gonçalves Martins")
    st.write("**Data Scientist | Practical Machine Learning for real-world decisions**")
    st.write("📍 Rio de Janeiro, Brasil")
    
    # Botões de ação
    col_btn1, col_btn2 = st.columns([1, 3])
    with col_btn1:
        st.download_button("📄 Download CV", b"PDF_CONTENT", file_name="Juan_Martins_CV.docx")
    with col_btn2:
        st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/juangmartins/")

st.divider()

# --- MÉTRICAS DE IMPACTO ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Experiência", "6+ Anos")
m2.metric("Especialidade", "Machine Learning")
m3.metric("Idiomas", "2 Fluentes")
m4.metric("Foco", "Decisões de Negócio")

st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["🎯 Sobre & Filosofia", "💼 Experiência", "🛠️ Skills & Educação"])

with tab1:
    st.markdown("### 💡 Minha Abordagem")
    st.write("""
    Trabalho com Ciência de Dados focando em **clareza, estrutura e tomada de decisão no mundo real** — não apenas modelos e métricas [2]. 
    Ao longo dos últimos 6 anos, envolvi-me em projetos de ponta a ponta, transformando dados brutos e perguntas incertas em análises que realmente apoiam o negócio [2].
    
    **Minhas Prioridades:**
    *   Entender o problema antes do modelo [4].
    *   Qualidade dos dados antes das métricas de performance [4].
    *   Contexto antes da técnica [4].
    """)

with tab2:
    # Scientia Dados
    st.subheader("Senior Data Scientist | Scientia")
    st.caption("12/2025 - Presente")
    st.markdown("""
    *   **Liderança Técnica:** Estruturação de trilhas de formação em Data Science e desenvolvimento de frameworks educacionais que conectam estatística e ML a aplicações práticas [3].
    *   **Projetos Aplicados:** Criação de soluções utilizando **Machine Learning, Python, SQL e APIs**, preparando profissionais para desafios reais de mercado [5].
    *   **Mentoria:** Foco na construção de maturidade analítica e tradução de dados em impacto de negócio [5].
    """)
    
    # Remessa Online
    st.subheader("Pleno Data Scientist | Remessa Online")
    st.caption("12/2025 - Presente")
    st.markdown("""
    *   **Projetos Aplicados:** Criação de soluções utilizando **Python, SQL e APIs**, preparando profissionais para desafios reais de mercado [5].
    """)

    # YDUQS
    st.subheader("Data Analyst Pl - Performance | YDUQS")
    st.caption("11/2024 - 12/2025")
    st.markdown("""
    *   **Modelagem Preditiva:** Desenvolvi modelos de **regressão linear** para projeção de metas (SKU nacional), aumentando a acurácia do planejamento de receitas [5].
    *   **Inteligência de Cliente:** Estruturação de **personas via clusterização**, otimizando estratégias de contato e reduzindo custos [6].
    *   **Inferência Estatística:** Identificação de drivers de performance para acelerar metas corporativas [6].
    """)

    # Estácio
    st.subheader("Data Analyst Pl | Estácio")
    st.caption("09/2022 - 12/2024")
    st.markdown("*   Foco em planejamento operacional, análise de inadimplência e liderança de indicadores de NPS [7].")

with tab3:
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown("### 🚀 Hard Skills")
        st.write("- **Linguagens:** Python (Pandas, Scikit-Learn), SQL, PySpark [1, 4]")
        st.write("- **Técnicas:** Machine Learning, Estatística, Feature Engineering, Hyperparameter Tuning [4, 5]")
        st.write("- **Ferramentas:** Power BI, APIs, Excel for Corporate Finance [1, 4]")
        
        st.markdown("### 🎓 Educação")
        st.write("**Ciência de Dados** - Estácio (2024) [8]")
        
    with col_s2:
        st.markdown("### 🌍 Idiomas")
        st.write("- **Português, Inglês e Espanhol:** Nativo ou Bilíngue [1]")
        st.write("- **Francês:** Nível profissional limitado [1]")
        
        st.markdown("### 📜 Certificações")
        st.write("- Intro to Machine Learning")
        st.write("- Python para Análise de Dados e Data Science")
        st.write("- Dashboard Excel Especialista [1]")