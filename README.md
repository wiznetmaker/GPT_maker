# GPT_maker
Applications for efficient GPT use

# GPT 기반 텍스트 변환 및 분석 도구

GPT를 쓰다보면 Self-Instruction 을 여러개를 사용하고 싶지만 안타깝게도 한개밖에 지원이 안되기 때문에 그걸 해결 보안하고자 어플리케이션으로 만들었습니다.

OpenAI의 GPT 모델을 활용하여 다양한 텍스트 변환 및 분석 기능을 제공하는 웹 애플리케이션입니다. 사용자는 텍스트를 입력하고, 원하는 기능을 선택하여 GPT 기반의 인공지능이 처리한 결과를 받아볼 수 있습니다.  
미리 Prompt Engineering 을 해둔 상태이고 현재 GPT-4-Vision 기능을 제외하고 모두 실행이가능합니다.  

---
<img src="https://github.com/jh941213/blog_service/assets/112835087/d21388f2-2032-4099-9ecf-d75beabd3ecd" width="50%" height="auto">

<img src="https://github.com/jh941213/blog_service/assets/112835087/e1f38a46-3e68-4830-924b-32c3408bad6f" width="50%" height="auto">



## 주요 기능

- **SEO 최적화 블로그 글 작성**: 사용자 입력에 기반하여 SEO에 최적화된 블로그 글을 생성합니다.
- **문체 변환**: 주어진 텍스트를 문어체로 변환합니다.
- **요약 및 번역**: 입력된 글을 요약하거나 영어, 일본어로 번역합니다.
- **이메일 및 공지 작성**: 특정 형식의 이메일이나 공지사항을 작성합니다.
- **프로젝트 기획서 작성**: 기본적인 아이디어를 바탕으로 프로젝트 기획서를 작성합니다.
- **웹 크롤링 및 데이터 파싱**: 주어진 URL에서 데이터를 크롤링하고, 이를 분석합니다.
- **DALL-E 이미지 생성 및 GPT-4-Vision 이미지 해석**: 텍스트를 기반으로 이미지를 생성하거나 이미지를 해석합니다.

## 사용 방법

1. **환경 설정**: 필요한 라이브러리를 설치하고 Streamlit을 실행합니다.
2. **API 키 입력**: OpenAI API 키를 입력합니다.
3. **텍스트 입력 및 기능 선택**: 원하는 기능을 선택하고, 필요한 텍스트를 입력합니다.
4. **결과 확인**: 버튼을 클릭하여 결과를 확인합니다.

## 기술 스택

- Python
- Streamlit
- OpenAI GPT 모델
- BeautifulSoup (웹 크롤링)
- HTML/CSS (프론트엔드 스타일링)

## 로컬 환경에서 실행하기

```bash
!git clone https://github.com/wiznetmaker/GPT_maker.git
cd gptmaker
pip install -r requirements.txt
streamlit run app.py
```
## 튜토리얼
1. [OpenAI API 홈페이지](https://openai.com/blog/openai-api)에 접속을해서 신용카드 등록  
<img src="https://github.com/wiznetmaker/GPT_maker/assets/112835087/70492776-b496-447e-902e-70de4d890d9f" width="50%" height="auto">

3. API key 생성 (주의 : 한번 발급 후 같은키는 또 생성이 안되니 적어둘것)


<img src="https://github.com/wiznetmaker/GPT_maker/assets/112835087/4b5bb1a4-7ec6-40c2-85d7-9f3bac65f628" width="50%" height="auto">

5. 로컬환경에서 설정하기 그대로 실행
6. API 키란에 API를 입력하고 내용을 입력후 원하는 Task 버튼 실행
