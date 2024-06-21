import streamlit as st
import streamlit_shadcn_ui as ui

#---VARIÁVEIS---
resume_file = 'assets/Andres Michelangelli - CV [english].pdf'
resume_file_name = 'CV_AndresMichelangelli.pdf'
profile_pic = 'assets/profile_pic.png'

css_file = 'styles/main.css'

name = 'Andrés Arturo Michelangelli'
description = 'Mechanical Engineer with international work experience developing multidisciplinary engineering projects, with a strong focus on project management and data analytics approaches'
email = 'andresmiche17@gmail.com'

layout = 'centered'
page_title = 'Portfolio | Andrés Arturo'
page_icon = '🔍'

social_media = {
    'LinkedIn': 'https://www.linkedin.com/in/andr%C3%A9s-michelangelli/',
    'Github': 'https://github.com/aamichelangellib',
}

projetos = {
    '☑️ File management project using Python': 'https://www.linkedin.com/posts/andr%C3%A9s-michelangelli_por-oi-rede-hoje-gostaria-de-comentar-activity-7190814989530632192-hGu4?utm_source=share&utm_medium=member_desktop',
    '☑️ Full End-to-end Business Intelligence project using Power BI': 'https://www.linkedin.com/posts/andr%C3%A9s-michelangelli_por-conclu%C3%AD-com-sucesso-o-curso-de-python-activity-7190821431172087809-WV_v?utm_source=share&utm_medium=member_desktop'
}

#---CONFIGURAÇÃO---
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

#---LEITURA DO PDF---
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()

#---LEITURA DO CSS---
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#---CABEÇALHO---    
col1, col2 = st.columns(2)

with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(name)
    st.write(description)
    st.write(' ')
    st.download_button(
        label='⬇️ Download CV Resume',
        data=PDFbyte,
        file_name=resume_file_name
    )
    st.write('📩', email)

st.write(' ')

#---BOTÕES COM LINKS REDES SOCIAIS---
cols = st.columns(len(social_media))

for index, (platform, link) in enumerate(social_media.items()):
    with cols[index]:
        ui.link_button(text=platform, url=link, key=f'lnik_btn_{platform}')

#---PROJETOS---
st.write('##')
st.subheader('Projects')
st.write("---")

for project, link in projetos.items():
    st.write(f'[{project}]({link})')

#---HABILIDADES---
st.write('##')
st.subheader('Key technical skills')
st.write('---')
st.write(
    '''
- 📊 BI and Data Analytics: Microsoft Excel, Microsoft Power BI, Power Query, DAX. 
- 💻 Programming Languages: Python, SQL, VBA. 
- 💡 Other skills: MS Project, Project Management, Microsoft Office, Business Operations, Strategy.
- 🗣️ Languages: English, Portuguese and Spanish. 
- 🤓 Soft skills: Problem-solving, Decision making, Strong analytic skills, Adaptability, Teamwork, Time 
management, Critical thinking, Communication, Commitment.
    '''
)

#---EXPERIENCIA---
st.write('##')
st.subheader('Work Experience')
st.write('---')

#---TRABALHO 1---
st.write('👨‍💼','**Mechanical Engineer I**')
st.write('11/2021 – present')
st.write(
    '''
- ✅ Analyze project data to develop and verify documentation.
- ✅ Support project coordination with data-driven planning, budgeting, and forecasting.  
- ✅ Understand client needs and deliver data-driven solutions and insights for digital 
transformation projects.
    '''
)
st.write(
    '''
- 🎯 Achievement: Led a high-profile project for an international client, overseeing a team of 10, 
leveraging data analytics and business intelligence tools.

- 🏆 Key Project: Valves Human Factor Study for FPSO units; Yinson Production (Singapore). 
    '''
)
#---TRABALHO 2---
st.write('👨‍💼','**Engineering Analyst**')
st.write('02/2021 – 11/2021')
st.write(
    '''
- ✅ Elaborate and verify project documentation.
- ✅ Conduct detailed engineering projects and field surveys.  
    '''
)
st.write(
    '''
- 🎯 Achievement: Perform first detailed project in Brazil for a high-profile client (Shell) in the gas 
industry, with tight deadlines.

- 🏆 Key Project: R2D2-B Route 2 Delivery to Bridge UTGCAB; Shell/Petrobras (Brazil). 
    '''
)

#---TRABALHO 3---
st.write('👨‍💼','**Piping Specialist**')
st.write('04/2018 – 01/2020')
st.write(
    '''
- ✅ Develop engineering projects using CAD tools.
- ✅ Support manufacturing and operations teams with detailed engineering data.  
    '''
)
st.write(
    '''
- 🎯 Achievement:  Achieved a 50% reduction in engineering processing time on a $180 million 
project through data optimization.

- 🏆 Key Project: 3 Combined Cycles for Energy Generation; MSU Energy (Argentina). 
    '''
)