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

# START JOB_EXPERIENCE
st.header("Опыт работы")
if "num_experience" not in st.session_state:
    st.session_state.num_experience = 1
if "job_experiences" not in st.session_state:
    st.session_state.job_experiences = {}

for i in range(1, st.session_state.num_experience + 1):
    key = f"job_experience_{i}"
    defaults = st.session_state.job_experiences.get(key, ["", "", "Полный рабочий день", "", "", ""])

    with st.expander(f"Опыт работы #{i}", expanded=True):
        job_title = st.text_input("Должность", value=defaults[0], key=f"job_title_{i}")
        company_name = st.text_input("Название комании", value=defaults[1], key=f"company_name_{i}")
        work_type_options = ["Полный рабочий день", "Частичная занятость", "Фриланс"]
        work_type = st.selectbox("Тип занятости", work_type_options, index=work_type_options.index(defaults[2]), key=f"work_type_{i}")
        period = st.date_input(
            "Рабочий период",
            (datetime.date(2022, 1, 1), datetime.date(2023, 1, 7)),
            datetime.date(2022, 1, 1),
            datetime.date(2023, 1, 7),
            format="MM.DD.YYYY",
            key=f"period_{i}"
        )
        # skills = st.text_input("Skills", value=defaults[4], key=f"skills_{i}")
        skills = st_tags(label="Приобретенные навыки", text="Нажмите Enter чтобы ввести", key=f"skills_{i}")
        description = st.text_area("Описание", value=defaults[5], key=f"description_{i}")

        st.session_state.job_experiences[key] = [job_title, company_name, work_type, period, skills, description]

add_experience = st.button("Добавить опыт работы")
if add_experience:
    st.session_state.num_experience += 1

st.markdown(st.session_state.job_experiences)
# END JOB_EXPERIENCE

# START EDUCATION
st.header("Образование")
if "num_education" not in st.session_state:
    st.session_state.num_education = 1
if "educations" not in st.session_state:
    st.session_state.educations = {}

for i in range(1, st.session_state.num_education + 1):
    key = f"education_{i}"
    print(key)
    defaults = st.session_state.educations.get(key, ["", "", "Полный рабочий день", "", "", ""])

    with st.expander(f"Образование #{i}", expanded=True):
        organization = st.text_input("Organization", key=f"organization_{i}")
        edu_period = st.date_input(
            "Period of work",
            (datetime.date(2022, 1, 1), datetime.date(2023, 1, 7)),
            max_value=datetime.date(2023, 1, 7),
            format="MM.DD.YYYY",
            key=f"edu_period_{i}"
        )
        degree = st.selectbox(
            "Степень обучения",
            ("Среднее образование", "Бакалавр", "Магистр", "Доктор наук"),
            key=f"degree_{i}"
        )
        grade = st.number_input("Оценка", key=f"grade_{i}", step=0.5)
        achievements = st_tags(label="Достижения", text="Нажмите Enter чтобы ввести", key=f"achievements_{i}")

        st.session_state.educations[key] = [organization, edu_period, degree, grade, achievements]

add_education = st.button("Добавить данные об образование")
if add_education:
    st.session_state.num_education += 1

st.markdown(st.session_state.educations)
# END EDUCATION

languages = st_tags(label="## Языки", text="Нажмите Enter чтобы ввести")

hard_skills = st_tags(label="## Хард скилы", text="Нажмите Enter чтобы ввести")

soft_skills = st_tags(label="## Софт скилы", text="Нажмите Enter чтобы ввести")

st.header("Финансовая информация")
hourly_rate = st.number_input("Базовая ставка, которую вы бы хотели получать в тенге", min_value=0, value=0)

submitted = st.button("ИИ Анализ Профиля", type="primary")

if submitted:
    # Здесь можно добавить код для анализа данных или их сохранения
    st.success("Данные отправлены успешно!")

