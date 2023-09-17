import numpy as np
import streamlit as st
import openai
openai.api_key = st.secrets["OPENAI_API_KEY"]

# from langchain.chat_models import ChatOpenAI
# chat_model - ChatOpenAI()

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'level' not in st.session_state:
    st.session_state.level = 1

if 'count' not in st.session_state:
    st.session_state.count = 0
    
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

st.set_page_config(
    page_title="방탈출"
)

st.header("금옥여자고등학교의 숨겨진 비밀")
# st.subheader("맛보기")


def chat_response(word):
    with st.chat_message("assistant"):
        st.markdown(word)
        # st.session_state.messages.append({"role": "assistant", "content":word})

# chat_response("안녕")
# chat_response("게임을 시작하고 싶으면 시작 이라고 외쳐봐")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "user", "content": "내 이름은 정근이라고 해"},
        {"role": "assistant", "content": "방탈출 챗봇"},
        {"role": "user", "content": "나는 금옥여자고등학교 학생이야"}
        ]
    print("Hello")
    


# 채팅창에 session_state 나타내기


prompt = st.chat_input("질문을 하세요.")

valid = False

if st.session_state.level == 1 and st.session_state.count == 0:
    st.session_state.messages.append({"role": "assistant", "content":"level 1 문제입니다"}) 
    st.session_state.count = 1

# if st.session_state.level == 2 and st.session_state.count == 0:
#     st.session_state.messages.append({"role": "assistant", "content":"level 2 문제입니다"}) 
#     st.session_state.count = 1

def quiz(level):
    st.session_state.level = level
    st.session_state.count = 0
    st.session_state.messages.append({"role": "assistant", "content":"level " + str(st.session_state.level) + " 문제입니다"})
    valid = True

if prompt :
    st.session_state.messages.append({"role": "user", "content":prompt})
    
    # 1번 문제
    if prompt == "1234" and st.session_state.level == 1:            
        st.session_state.messages.append({"role": "assistant", "content":"정답입니다"})
        st.session_state.level += 1
        st.session_state.count = 0

        quiz(2)

    # 2번 문제
    if prompt == "5678" and st.session_state.level == 2:            
        st.session_state.messages.append({"role": "assistant", "content":"정답입니다"})
        st.session_state.level += 1
        st.session_state.count = 0

        quiz(3)

    # else :         
    #     st.session_state.messages.append({"role": "assistant", "content":"틀렸습니다"})

        
# valid가 True가 될 시 인공지능과 대화    
if prompt and valid:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content":prompt})

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
            message_placeholder.markdown(full_response)
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content":full_response})


st.header("Stage  :  " + str(st.session_state.level))

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

print(st.session_state)
    