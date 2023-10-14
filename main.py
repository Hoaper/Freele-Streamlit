import streamlit as st
from streamlit_tags import st_tags 
import datetime

st.title("Форма для ввода данных фрилансера")

st.header("Основная информация")
domain = st.text_input("Позиция", placeholder="Например, веб-разработка")
job_category = st.selectbox(
   "Категория",
   ("Веб разроботка", "Мобильная разработка", "Программирование", "Веб дизайн", "Data Science", "Дизайн", "Маркетинг", "Администрирование", "Продажи", "Контент", "Переводы", "Видео", "Аудио", "Бизнес-услуги", "Другое"),
   index=None,
   placeholder="Выберите категорию",
)
about = st.text_area("Расскажите о себе", placeholder="Например, я начинающий веб-разработчик, который хочет найти работу в этой сфере")

st.header("Опыт работы")

if "num_experience" not in st.session_state:
    st.session_state.num_experience = 1
if "job_experiences" not in st.session_state:
    st.session_state.job_experiences = {}

for i in range(1, st.session_state.num_experience + 1):
    key = f"job_experience_{i}"
    defaults = st.session_state.job_experiences.get(key, ["", "", "Полный рабочий день", "", "", ""])

    with st.expander(f"Опыт работы #{i}", expanded=True):
        job_title = st.text_input("Job title", value=defaults[0], key=f"job_title_{i}")
        company_name = st.text_input("Company name", value=defaults[1], key=f"company_name_{i}")
        work_type_options = ["Полный рабочий день", "Частичная занятость", "Фриланс"]
        work_type = st.selectbox("Work-type", work_type_options, index=work_type_options.index(defaults[2]), key=f"work_type_{i}")
        period = st.date_input(
            "Period of work",
            (datetime.date(2022, 1, 1), datetime.date(2023, 1, 7)),
            datetime.date(2022, 1, 1),
            datetime.date(2023, 1, 7),
            format="MM.DD.YYYY",
            key=f"period_{i}"
        )
        # skills = st.text_input("Skills", value=defaults[4], key=f"skills_{i}")
        skills = st_tags(label="Skills", text="Нажмите Enter чтобы ввести", key=f"skills_{i}")
        description = st.text_area("Description", value=defaults[5], key=f"description_{i}")

        st.session_state.job_experiences[key] = [job_title, company_name, work_type, period, skills, description]

add_experience = st.button("Добавить опыт работы")
if add_experience:
    st.session_state.num_experience += 1

st.markdown(st.session_state.job_experiences)


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

submitted = st.button("ИИ Анализ Профиля", type="primary")

if submitted:
    # Здесь можно добавить код для анализа данных или их сохранения
    st.success("Данные отправлены успешно!")

