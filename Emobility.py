import streamlit as st

font = "Nanum pen Script"

st.set_page_config(layout="centered")

blank1, main, blank2 = st.columns([1,8,1])
with main:
    st.markdown("<h1 style='text-align: center;'>자율 주행 휠체어 <br>홍보 사이트</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>이모빌리티 폭격기</h4>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(['제작 동기', '제작 계획', '사업화 계획', '프로토타입 시연 정보'])

with tab1:
    with st.container(border=True): 
        st.subheader('1. 퍼스널 모빌리티의 시장성 증가')
        st.image('images/personal_mobility_device_market_size.png', caption='출처:https://spri.kr/posts/view/23237?code=industry_trend')
        st.markdown('소프트웨어정책연구소 SPRI에 한 기사에 따르면 퍼스널 모빌리티 시장 규모는 꾸준히 증가하는 추세를 보이며')
        col1, col2 = st.columns([5,5])

        with col1:
            st.subheader('2. 점차 늘어나는 기대 수명')
            '고령화 사회를 지나 초고령화 사회로 진입한 지금 노인 1인가구의 증가와 함께 문제되고 있는 장애인의 이동권 인식 보장 증가'
    
        with col2:
            st.subheader('3. 전동휠체어 검색량 변동 추이')
            st.image('images/personal_mobility_device_market_size.png')
    st.header('이러한 이유로')
    st.markdown('저희 팀은 다음과 같은 휠체어 제작을 목표로 두었습니다. :br 수동 휠체어에 자율주행 기술을 접목시키되 :br 제작 비용을 줄이고 교통 약자의 이동 편의성을 높인 자율 주행 휠체어')
     
with tab2:
        with st.container(border=True): 
            st.subheader('사업화 대상', divider= True)
            st.image('images/objective.png', width=670)
            
            st.markdown(':br :br :br')
            st.subheader('제품이 가지는 특징', divider= True)
            st.image('images/function.png', width=670)
with tab3:
    with st.container(border=True): 
            st.subheader('마케팅 전략', divider= True)
            st.image('images/marketing.png', width=670)
    
with tab4:
    with st.container(border=True):
        st.text('none') 
        """
        video_file = open()
        video_data = video_file.read()
        st.video(video_file)
        """
