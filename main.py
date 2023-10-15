import streamlit as st
from streamlit_tags import st_tags
# from dotenv import load_dotenv
# import tiktoken
import datetime
from st_chat_message import message
import openai
from streamlit_pills import pills
import requests
# load_dotenv()

st.set_page_config(
    page_title="Freele App",
    page_icon="💼",
    # layout="wide",
    initial_sidebar_state="expanded",
)

# В конце ответь могу ли я расчитывать на ставку указанную ниже.
prompt_template = """Вы являетесь опытным AI HR специалистом. На протяжении всего разговора поддерживайте профессиональный и уважительный тон. Я - Фрилансер. Оцени пожалуйста мой профиль от 1 до 10. Будь со мной строг и объективен.
Распиши все мои плюсы и недостатки как можно подробнее. Я хочу стать лучше. Также я хочу узнать, какие у меня есть шансы найти работу в этой сфере. Предоставь мне пожалуйста рекомендации, как мне стать лучше.
Вот информация обо мне:
Я ищу работу на позицию: {position}, в сфере: {category};
Обо мне: {about};
Мой опыт работы: {job_experience};
Мое образование: {education};
Знание языков: {languages};
Мои Hard Skills: {hard_skills};
Мои Soft Skills: {soft_skills};
Я ориентируюсь на оплату в: {price} тенге в час.
"""

openai.api_key = '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'

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"
if "messages" not in st.session_state:
    st.session_state.messages = []

# if 'messages' not in st.session_state:
#     st.session_state['messages'] = []
#     st.session_state['messages'].append(
#         # {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown."}
#         {"role": "system", "content": "You are a helpful assistant."}
#     )

with st.sidebar:
    st.image("https://peopleworks.in/wp-content/uploads/2018/03/AI.jpg")

    st.title('💼 Freele')
    st.write('Freele - это сервис, который поможет вам найти работу мечты.')
    functionality = st.radio(
    "Выберите функционал",
    ["Анализ профиля фрилансера", "Подбор фрилансеров для проекта", "Подбор проектов для фрилансера"],
    captions = ["Рекомендации ИИ", "ИИ Алгоритм подбора фрилансеров", "ИИ Алгоритм подбора проектов"]
    )

if functionality == "Анализ профиля фрилансера":
    st.title("Профиль Фрилансера")
    selected = pills("", ["AI", "Tech"], ["🤖", "💻"])

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

    # st.markdown(st.session_state.job_experiences)
    # END JOB_EXPERIENCE

    # START EDUCATION
    st.header("Образование")
    if "num_education" not in st.session_state:
        st.session_state.num_education = 1
    if "educations" not in st.session_state:
        st.session_state.educations = {}

    for i in range(1, st.session_state.num_education + 1):
        key = f"education_{i}"
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
            profession = st.text_input("Специальность", key=f"profession_{i}")
            grade = st.number_input("Оценка", key=f"grade_{i}", step=0.5)
            achievements = st_tags(label="Достижения", text="Нажмите Enter чтобы ввести", key=f"achievements_{i}")

            st.session_state.educations[key] = [organization, edu_period, degree, grade, achievements, profession]

    add_education = st.button("Добавить данные об образование")
    if add_education:
        st.session_state.num_education += 1

    # st.markdown(st.session_state.educations)
    # END EDUCATION

    languages = st_tags(label="## Языки", text="Нажмите Enter чтобы ввести")

    hard_skills = st_tags(label="## Хард скилы", text="Нажмите Enter чтобы ввести")

    soft_skills = st_tags(label="## Софт скилы", text="Нажмите Enter чтобы ввести")

    st.header("Финансовая информация")
    hourly_rate = st.number_input("Базовая ставка, которую вы бы хотели получать в тенге/час", min_value=0, value=0)


    # def cut_text_by_tokens(text: str, limit: int = 4096):
    #     # Cut text for specific amount of tokens
    #     tokens = encoding.encode(data)
    #     current_part = []
    #     current_count = 0

    #     # SELECT AMOUNT OF TOKENS
    #     for token in tokens:
    #         current_part.append(token)
    #         current_count += 1
    #         if current_count >= limit:
    #             return "".join([encoding.decode_single_token_bytes(token).decode("utf-8", errors="replace") for token in current_part])

    #     return text


    # def make_response(data: str):
    #     cutted_text = cut_text_by_tokens(data)
    #     return llm.predict(cutted_text)


    submitted = st.button("Анализ Профиля", type="primary")
    if submitted:
        st.session_state.messages = []
        st.title("📑 Результаты анализа")
        
    # if submitted:
        # Здесь можно добавить код для анализа данных или их сохранения
        # hourly_rate domain job_category about
        job_data = st.session_state.job_experiences.values()
        edu_data = st.session_state.educations.values()
        langs = ",".join(languages)
        h_skills = ",".join(hard_skills)
        s_skills = ",".join(soft_skills)

        job_template = "Компания: {company} Должность: {domain}. Период работы: с {started_date} по {end_date}. Приобретенные навыки: {skills}. Описание работы: {description}"
        job_experiences = []
        index = 0
        for job in job_data:
            if (index == 2):
                break
            # [job_title, company_name, work_type, period, skills, description]
            job_experiences.append(job_template.format(
                company=job[1],
                domain=job[0],
                started_date=str(job[3][0]),
                end_date=str(job[3][1]),
                skills=",".join(skills),
                description=job[5]
            ))
            index += 1
        edu_template = "Учебное заведение: {company} Степень: {degree}. Период учебы: с {started_date} по {end_date}. Специальность: {profession}. GPA: {grade}"
        edu_experiences = []
        for edu in edu_data:
            # [organization, edu_period, degree, grade, achievements, profession] # skeleton of edu
            edu_experiences.append(edu_template.format(
                company=edu[0],
                degree=edu[2],
                started_date=str(edu[1][0]),
                end_date=str(edu[1][1]),
                profession=edu[5],
                grade=edu[3]
            ))

        data = prompt_template.format(
            position=domain, 
            category=job_category, 
            about=about, 
            languages=langs, 
            hard_skills=h_skills, 
            soft_skills=s_skills, 
            price=hourly_rate,
            education=".".join(edu_experiences),
            job_experience=".".join(job_experiences)
        )

        # st.write(data)

        st.session_state.messages.append({"role": "user", "content": data})
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

