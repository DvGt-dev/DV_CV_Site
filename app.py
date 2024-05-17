from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "DJONTSO Victorien.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | DJONTSO Victorien"
PAGE_ICON = ":wave:"
NAME = "DJONTSO Victorien"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "dvrchipro@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCEjNkwkwYXZ68FmCqfin7lQ",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com/DvGt-dev",
    "Twitter": "https://twitter.com",
    "Instagram": "https://instagram.com",
}
PROJECTS = {
    "🏆": "https://youtu.be/Sb0A9i6d320",
    "🏆": "https://youtu.be/3egaMfE9388",
    "🏆": "https://youtu.be/LzCfNanQ_9c",
    "🏆": "https://pythonandvba.com/mytoolbelt/",
    "🏆 test link image": r"assets\\profile-pic.png",
}




st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


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
- ✔️ De Mars 2021 à Septembre 2022 : consultant chez « ZF 
ARCHITECTS ».
ZF ARCHITECT de ZAUGU FOFACK J I, architecte ONAC n°325 Ref : 
https://www.zf-architects.com/
__________________
- ✔️ Mars 2019 à Mars 2021 (02 ans) : Stage professionnel en vue 
de l’inscription au tableau de l’Ordre National des Architectes du 
Cameron (ONAC)
Mission : Programmeur, projeteur, coursier, architecte de suivi etc.
Cabinet Serge ELOUNDOU – SETREC AUI Sarl de M. LUNDOU 
GAMBOGO Serge A., ONAC n°1996/142. Ref : A servi une dizaine 
d’années à la BEAC centrale- Yaoundé-Cameroun.
__________________

- ✔️ 08 Octobre 2019 au 15 Décembre 2019(02 Mois) : Stage
Personnel dans le but de Suivre de près le chantier de la construction 
de la cathédrale de Bafoussam.
Missions: Assistant architecte de suivi, projeteur
Cabinet Bureau d’étude Architecte (BEA) de M. Guy R. PUAKAMI K., 
ONAC n° 1978/020 Ref : Suivi de chantier de la cathédrale de Bafoussam 
(En cours) ; Maison du parti à Bafoussam
__________________
- ✔️ Du 03 Aout 2017 au 30 Septembre 2017 (02 Mois)
Stage académique.
Missions: Projeteur, programmeur
Cabinet Urbatech Conseil de M.DJINHGA Vi C., Architecte ONAC n° 
2002/183 ; Ingénieur du Génie Civil 0NIG n° 03557. Ref : construction de 
l'immeuble de la Direction Générale des Impôts (DGI), YaoundéCameroun
Encadré par : M. Kamte Mekontchou Boris Hermann, Architecte ONAC
n°2018/321. Ref : Participant et lauréat de divers concours
internationaux en architecture et design (premier prix du Taipei
International Design Awards 2017 entre autres)

__________________
- ✔️ 02 Juin 2017 05 Juillet 2017 Participation au projet pour 
la proposition d’un monument et l’aménagement d’un site 
commémoratif pour le cinquantenaire de l’unité du Cameroun à 
Bandjoun- Ouest Cameroun
Mission : programmeur, projeteur 
SOCERCON BTP Sarl de M, Kundem Billes, Chef d’entreprise.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 
- 📊 
- 📚 
- 🗄️ 
- nalyse de données, cartographie, 
programmation, Composition et 
aménagement des espaces.
Développement du projet 
(Esquisse-PEO) images et vidéos.
Suivi, relevés, mise en œuvre 
d’éléments en béton armé.
Utilisation desinformations 
climatiques et topographiques
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- ► -----------------$3
- ► -----------------$3
- ► -----------------$3
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► -----------------$3
- ► -----------------$3
- ► -----------------$3
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► -----------------$3
- ► -----------------$3
- ► -----------------$3
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# autres 