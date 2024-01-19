import streamlit as st
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import os
from vision import *
import tempfile

def read_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()
    return prompt

def generate_response(client, model, prompt, user_input):
    if not user_input:
        return "Not found text. Please input text."

    try:
        completion = client.chat.completions.create(
            model=model,  
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.1,  
            max_tokens=4096
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        raise Exception("프롬프트 처리 중 오류가 발생했습니다.")

def create_dalle_image(client, prompt):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url  
    except Exception as e:
        return str(e)


st.title("📝 GPT_Maker")
st.markdown('<p style="font-size: small;">Made by Simon</p>', unsafe_allow_html=True)
st.markdown('[WIZnet Tech Blog](https://wiz-tech.tistory.com/)')
st.markdown('[WIZnet Maker Site](https://maker.wiznet.io/)')
st.markdown('[WIZnet Chatbot Test](http://www.iamacorn.p-e.kr:8501/)')
st.markdown("""
    <style>
    button.st-emotion-cache-7ym5gk {
        display: inline-block;   /* 버튼을 인라인 블록 요소로 설정하여 내용물에 맞춰 크기 조정 */
        min-width: 120px;       /* 버튼의 최소 너비 설정 */
        margin: 10px;           /* 주변 요소와의 간격 설정 */
        padding: 8px 16px;      /* 내부 여백을 설정하여 버튼 내용물과 경계 사이의 공간을 조정 */
        font-size: 16px;        /* 글자 크기 설정 */
        background: linear-gradient(to bottom, #a8c461, #36cd9c); /* 그라데이션 적용 */
        border: none;
        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5);
        color: white;
        font-weight: bold;
        text-align: center;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        white-space: nowrap;     /* 글자가 버튼 밖으로 나가지 않도록 설정 */
    }

    button.st-emotion-cache-7ym5gk::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(to bottom, rgba(255, 255, 255, 0.2), transparent);
        transform: translateY(-100%);
        transition: transform 0.3s ease;
    }

    button.st-emotion-cache-7ym5gk:hover::before {
        transform: translateY(0);
    }

    button.st-emotion-cache-7ym5gk:hover {
        background: linear-gradient(to bottom, #36cd9c, #a8c461); /* 호버 효과 */
    }
    </style>
    """, unsafe_allow_html=True)



with st.sidebar:
    model_choice = st.selectbox("모델 선택", ["gpt-3.5-turbo-16k", "gpt-4","gpt-4-1106-preview"], key="model_select")

    user_api_key = st.text_input("OpenAI API Key", type="password")

    url = st.text_input("크롤링 URL입력(GPT-4-1106 권장)", key="url_input")
   
    user_input = st.text_area("여기에 글을 입력하세요", height=1000, key="input_text")

    char_count = len(user_input)

    st.caption(f"현재 글자 수: {char_count}")
    
    uploaded_image = st.file_uploader("이미지 업로드", type=["png", "jpg", "jpeg"], key="image_uploader")
    print(uploaded_image)

if user_api_key:
    client = OpenAI(api_key=user_api_key)
else:
    st.error("API 키가 필요합니다.")

def crawl_url(url):
    if url:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
   
            return soup.get_text()
        except Exception as e:
            return str(e)
    return "URL이 입력되지 않았습니다."
st.write("")

st.header("WIZnet ChatGPT 글쓰기 도우미")
st.write("")
buttons = ["SEO 최적화 블로그 글 작성하기",
             "문어체로 작성하기",
             "그룹웨어에 작성할 글 요약하기",
             "영어로 번역 작성하기",
             "일본어로 번역 작성하기",
             "이메일 전체공지 작성하기",
             "FaQ Data Set 제작하기",
             "크롤링 데이터 파싱하기",
             "DALL-E 이미지 생성하기",
             "GPT-4-Vision 이미지 해석하기"
             ]

result_containers = [st.empty() for _ in range(10)]

col1, col2 = st.columns(2)
with col1:
    if st.button("SEO 최적화 블로그 글 작성하기"):
        try:
            file_path = "prompts/0_prompt.txt"
            prompt = read_prompt(file_path)
            response = generate_response(client, model_choice, prompt, user_input)
            result_containers[0].text_area("변환결과", response, height=600)
        except Exception as e:
            st.error("오류가 발생했습니다. Prompt를 확인해주세요.")
            print(e)
with col2:
    if st.button("문어체로 작성하기"):
        try:
            file_path = "prompts/1_prompt.txt"
            prompt = read_prompt(file_path)
            response = generate_response(client, model_choice, prompt, user_input)
            result_containers[1].text_area("변환결과", response, height=600)
        except Exception as e:
            st.error("오류가 발생했습니다. Prompt를 확인해주세요.")

col1, col2 = st.columns(2)
with col1:
    if st.button("그룹웨어에 작성할 글 요약하기"):
        try:
            file_path = "prompts/2_prompt.txt"
            prompt = read_prompt(file_path)
            response = generate_response(client, model_choice, prompt, user_input)
            result_containers[2].text_area("변환결과", response, height=600)
        except Exception as e:
            st.error("오류가 발생했습니다. Prompt를 확인해주세요.")
with col2:
    if st.button("영어로 번역 작성하기"):
        try:
            file_path = "prompts/3_prompt.txt"
            prompt = read_prompt(file_path)
            response = generate_response(client, model_choice, prompt, user_input)
            result_containers[3].text_area("변환결과", response, height=600)
        except Exception as e:
            st.error("오류가 발생했습니다. Prompt를 확인해주세요.")

col1, col2 = st.columns(2)
with col1:
    if st.button("일본어로 번역 작성하기"):
        try:
            file_path = "prompts/4_prompt.txt"
            prompt = read_prompt(file_path)
            response = generate_response(client, model_choice, prompt, user_input)
            result_containers[4].text_area("변환결과", response, height=600)
        except Exception as e:
            st.error("오류가 발생했습니다. Prompt를 확인해주세요.")
with col2:
    if st.button("이메일 전체공지 작성하기"):
        try:
            file_path = "prompts/5_prompt.txt"
            prompt = read_prompt(file_path)
            response = generate_response(client, model_choice, prompt, user_input)
            result_containers[5].text_area("변환결과", response, height=600)
        except Exception as e:
            st.error("오류가 발생했습니다. Prompt를 확인해주세요.")

col1, col2 = st.columns(2)
with col1:
    if st.button("FaQ Data Set 제작하기"):
        try:
            file_path = "prompts/6_prompt.txt"
            prompt = read_prompt(file_path)
            response = generate_response(client, model_choice, prompt, user_input)
            result_containers[6].text_area("변환결과", response, height=600)
        except Exception as e:  
            st.error("오류가 발생했습니다. Prompt를 확인해주세요.")

with col2:
    if st.button("크롤링 데이터 파싱하기"):
        try:
            file_path = "prompts/7_prompt.txt"
            prompt = read_prompt(file_path)
            crawl_data = crawl_url(url)
            print("프린터확인:",crawl_data)
            response = generate_response(client, model_choice, prompt, crawl_data)
            result_containers[7].text_area("변환결과", response, height=600)
        except Exception as e:
            st.error("오류가 발생했습니다. Prompt를 확인해주세요.")

col1, col2 = st.columns(2)
with col1:
    if st.button("DALL-E 이미지 생성하기"):
        try:
            prompt = user_input 
            image_url = create_dalle_image(client, prompt)
            if image_url:
                result_containers[8].image(image_url, caption=prompt)
            else:
                result_containers[8].write("이미지 생성 실패")
        except Exception as e: 
            st.error(e)
with col2:
    if st.button("GPT-4-Vision 이미지 해석하기"):
        try:
            if uploaded_image is not None:
                # 임시 파일 생성
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                    tmp_file.write(uploaded_image.read())
                    tmp_file_path = tmp_file.name  # 임시 파일의 경로 저장
                text = analyze_image_with_gpt4_vision(tmp_file_path, user_api_key)  # 임시 파일 경로를 함수에 전달
                result_containers[9].text_area("변환결과", text, height=600)

                # 임시 파일 삭제 (옵션)
                os.remove(tmp_file_path)
            else:
                st.error("이미지를 업로드해주세요.")
        except Exception as e:
            st.error(e)

