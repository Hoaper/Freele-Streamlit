import streamlit as st
from streamlit_tags import st_tags 

def experience_form(experience_number):

    with st.expander(f"Опыт работы #{experience_number}", expanded=True):
        st.header(f"Опыт работы #{experience_number}")
        job_title = st.text_input("Job title", key=f"job_title_{experience_number}")
        company_name = st.text_input("Company name", key=f"company_name_{experience_number}")
        work_type = st.selectbox("Work-type", ["Полный рабочий день", "Частичная занятость", "Фриланс"], key=f"work_type_{experience_number}")
        period = st.text_input("Period of work", key=f"period_{experience_number}")
        skills = st.text_input("Skills", key=f"skills_{experience_number}")
        description = st.text_area("Description", key=f"description_{experience_number}")

    return {
        "job_title": job_title,
        "company_name": company_name,
        "work_type": work_type,
        "period": period,
        "skills": skills,
        "description": description
    }

st.title("Форма для ввода данных фрилансера")

st.header("Основная информация")
domain = st.text_input("В какой сфере ты хочешь работать")


st.header("Опыт работы")
if 'experiences' not in st.session_state:
    st.session_state.experiences = []
add_experience = st.button("Добавить опыт работы")
if add_experience:
    st.session_state.experiences.append(experience_form(len(st.session_state.experiences) + 1))



st.header("Образование")
organization = st.text_input("Organization")
edu_period = st.text_input("Period of education")
degree = st.text_input("Degree")
grade = st.text_input("Grade")
achievements = st.text_area("Achievements")

st.header("Языки")
languages = st_tags(label="Languages", text="Нажмите Enter чтобы ввести")

st.header("Hard Skills")
hard_skills = st_tags(label="Hard Skills", text="Нажмите Enter чтобы ввести")

st.header("Soft Skills")
soft_skills = st_tags(label="Soft Skills", text="Нажмите Enter чтобы ввести")

st.header("Финансовая информация")
hourly_rate = st.number_input("Базовая ставка, которую вы бы хотели получать в тенге", min_value=0, value=0)

submitted = st.button("Анализ")

if submitted:
    # Здесь можно добавить код для анализа данных или их сохранения
    st.success("Данные отправлены успешно!")

