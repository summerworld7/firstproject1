import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 여행지 추천기 🌍", page_icon="✈️")

# 제목
st.title("✈️ MBTI로 떠나는 여행지 추천 💼")
st.markdown("당신의 성격에 꼭 맞는 여행지를 알려드릴게요! 🗺️\n\n아래에서 MBTI를 선택해보세요 👇")

# MBTI 목록
mbti_list = [
    "INTP", "INFP", "INFJ", "INTJ",
    "ENTP", "ENFP", "ENFJ", "ENTJ",
    "ISTP", "ISFP", "ISFJ", "ISTJ",
    "ESTP", "ESFP", "ESFJ", "ESTJ"
]

# MBTI별 여행지 추천 데이터
travel_dict = {
    "INTP": ("아이슬란드 🇮🇸", "🧊 고요하고 신비로운 대자연 속 사색 여행!"),
    "INFP": ("스코틀랜드 하이랜드 🏞️", "🍃 낭만 가득한 자연 속 감성 충전 여행"),
    "INFJ": ("부탄 🇧🇹", "🧘 평화와 의미를 찾는 영적 여정"),
    "INTJ": ("도쿄 🇯🇵", "🧠 질서와 혁신이 공존하는 똑똑한 도시 여행"),
    "ENTP": ("뉴욕 🇺🇸", "🌆 창의력과 에너지 폭발! 도시가 놀이터"),
    "ENFP": ("페루 마추픽추 🇵🇪", "⛰️ 모험과 미지의 세계에 대한 열정 충만!"),
    "ENFJ": ("이탈리아 피렌체 🇮🇹", "🎨 역사와 사람과 감성의 조화로운 만남"),
    "ENTJ": ("싱가포르 🇸🇬", "📈 효율과 세련됨의 결정체, 전략가형 여행"),
    "ISTP": ("호주 태즈메이니아 🏕️", "🔧 직접 부딪히는 자연 탐험!"),
    "ISFP": ("발리 🇮🇩", "🌺 감성과 힐링, 예술적 무드 가득한 휴양"),
    "ISFJ": ("스위스 루체른 🇨🇭", "🕊️ 평화롭고 안전한 클래식 여행지"),
    "ISTJ": ("독일 뮌헨 🇩🇪", "🔍 체계적이고 전통적인 유럽 도시 여행"),
    "ESTP": ("두바이 🇦🇪", "🚀 빠르고 화려한 액션과 즐길 거리 가득!"),
    "ESFP": ("하와이 🌺", "🎉 인생은 축제! 놀고 즐기고 힐링하고"),
    "ESFJ": ("프랑스 파리 🇫🇷", "🥐 우아하고 감성적인 문화 탐방"),
    "ESTJ": ("런던 🇬🇧", "🧳 클래식한 도시 탐험과 완벽한 일정 관리!")
}

# 선택박스
selected_mbti = st.selectbox("💡 MBTI 유형을 선택하세요:", ["선택 안 함"] + mbti_list)

# 결과 출력
if selected_mbti != "선택 안 함":
    place, desc = travel_dict.get(selected_mbti, ("추천 없음", "🤷 여행지를 찾지 못했어요."))
    st.balloons()  # 풍선 효과 🎈
    st.success(f"🌍 추천 여행지: **{place}**")
    st.write(f"{desc}")
