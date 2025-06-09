import streamlit as st

# MBTI별 추천 여행지 데이터 (예시)
mbti_travel_recommendations = {
    "INTJ": "교토, 일본 - 조용하고 역사 깊은 도시",
    "INTP": "하이델베르크, 독일 - 지적인 분위기의 대학 도시",
    "ENTJ": "뉴욕, 미국 - 빠르게 움직이는 대도시",
    "ENTP": "베를린, 독일 - 창의적인 에너지가 넘치는 곳",
    "INFJ": "레이캬비크, 아이슬란드 - 조용하고 자연과 연결된 도시",
    "INFP": "바르셀로나, 스페인 - 감성을 자극하는 예술 도시",
    "ENFJ": "파리, 프랑스 - 낭만과 소통이 어우러진 도시",
    "ENFP": "리우데자네이루, 브라질 - 활기차고 자유로운 분위기",
    "ISTJ": "취리히, 스위스 - 체계적이고 안정적인 도시",
    "ISFJ": "프라하, 체코 - 고요하고 아름다운 도시",
    "ESTJ": "시드니, 호주 - 질서와 여유가 공존하는 도시",
    "ESFJ": "로마, 이탈리아 - 전통과 사람 중심의 도시",
    "ISTP": "밴프, 캐나다 - 탐험과 독립을 즐길 수 있는 자연",
    "ISFP": "코펜하겐, 덴마크 - 감각적이고 아늑한 분위기",
    "ESTP": "라스베이거스, 미국 - 자극적이고 다이내믹한 도시",
    "ESFP": "발리, 인도네시아 - 즐거움과 모험이 가득한 곳"
}

# Streamlit 앱 시작
st.title("MBTI별 여행지 추천기")

# 사용자 입력 받기
mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_travel_recommendations.keys()))

# 결과 보여주기
if mbti:
    recommendation = mbti_travel_recommendations[mbti]
    st.subheader(f"추천 여행지 for {mbti}:")
    st.write(recommendation)
