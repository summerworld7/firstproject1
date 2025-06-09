import streamlit as st

# 🎬 타이틀
st.set_page_config(page_title="MBTI 영화 추천기 🎥", page_icon="🎈")
st.title("🎥 MBTI로 알아보는 명작 영화 추천! 💫")
st.markdown("**당신의 성격에 꼭 맞는 수학·과학 명작 영화를 추천해드려요!** 😎\n\nMBTI 4글자를 입력해보세요 👇")

# 📥 사용자 입력
mbti_input = st.text_input("🧬 MBTI 입력 (예: INFP)", max_chars=4).upper()

# 🎯 추천 영화 DB (간단 버전)
movie_dict = {
    "INTP": ("굿 윌 헌팅", "🧠 천재성과 깊은 사고를 지닌 당신에게 꼭 맞는 영화!"),
    "ENFP": ("인터스텔라", "🚀 상상력 넘치는 당신에게 우주여행은 필수죠!"),
    "ISTJ": ("이미테이션 게임", "🧮 논리적이고 신중한 당신에게 어울리는 이야기"),
    "INFJ": ("컨택트", "🌌 언어와 외계 문명의 심오한 이야기가 당신을 사로잡을 거예요"),
    "ENTJ": ("마션", "🛰 리더십과 실행력을 가진 당신은 화성에서도 살아남습니다!"),
    "ISFP": ("루시", "🧬 감성적이면서도 철학적인 과학 영화가 딱!"),
    "INTJ": ("2001: 스페이스 오디세이", "👁 깊은 사고와 미래적 통찰을 위한 걸작"),
    "ESFP": ("빅 히어로", "🎉 에너지 넘치고 따뜻한 당신에게 딱 맞는 로봇 히어로 무비!"),
}

# 🎉 추천 결과
if mbti_input:
    if mbti_input in movie_dict:
        title, desc = movie_dict[mbti_input]
        st.balloons()  # 🎈 풍선 효과
        st.success(f"🎬 추천 영화: **{title}**")
        st.write(f"💡 {desc}")
    else:
        st.error("😢 유효한 MBTI를 입력해주세요. (예: INFP, ENTJ)")
