import streamlit as st
from streamlit_tags import st_tags 
from dynamic_tabs import dynamic_tabs
import time

def experience_form(experience_number):
    st.subheader(f"Опыт работы #{experience_number}")
    job_title = st.text_input("Job title")
    company_name = st.text_input("Company name")
    work_type = st.selectbox("Work-type", ["Полный рабочий день", "Частичная занятость", "Фриланс"])
    period = st.text_input("Period of work")
    skills = st.text_input("Skills")
    description = st.text_area("Description")

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

if 'experiences' not in st.session_state:
    st.session_state.experiences = []
st.header("Опыт работы")
experiences = []
add_experience = st.button("Добавить опыт работы")

experience_number = 1
while add_experience:
    st.session_state.experiences.append(experience_form(len(st.session_state.experiences) + 1))
    experience_number += 1
    add_experience = st.button("Добавить еще опыт работы")


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

