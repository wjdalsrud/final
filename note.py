import streamlit as st

tab1, tab2= st.tabs(["물 권장량 알기", "노력"])
#tap 나누기


with tab1:
    st.write("# 물 마시기 프로젝트")
    st.write('물을 마시는 것은 우리 건강에 매우 중요합니다.')
    st.write('물은 체온 조절, 세포 기능 유지, 소화 개선 등 다양한 신체 기능에 도움을 줍니다. 건강한 생활을 위해 물을 마시는 습관을 들이고 몸에 충분한 수분을 공급합시다.')
    st.write('시작은 작지만 꾸준한 물 마시기 습관은 우리 몸 건강에 긍정적인 영향을 미칠 것입니다.')
    st.write('WTO 세계보건기구에 따르면 하루 물 섭취 권장량은 2L이지만 사람마다 하루 권장량이 다르므로 정확한 권장량을 계산하기 위해서는 몸무게에 0.03을 곱한 값만큼 물을 마시면 됩니다.')
    #tab1에서 보이는 문구

    name = st.text_input('이름을 입력하세요. ')
    #text_input : 이름 입력받기
    
    weight = st.number_input('몸무게를 입력하세요.', value = 0, step = 1, key='weight')
    #number_input : 몸무게 입력받기. 시작은 0부터 1씩 step. 고유 key 'weight' 부여

    personal = round(weight**0.03, 2)
    #본인의 하루 권장량. 몸무게에 0.03 곱하고 소숫점 둘째자리까지 표현

    if weight:
        st.write(name, '님의 하루 물 섭취 권장량은', personal, 'L 입니다.')
        st.write('[노력] 페이지에서 하루 물 섭취 권장량을 채워보세요!')
    #몸무게를 입력했을 때 나오는 문구

with tab2:
    st.write('# 물을 마실 때마다 기록해봅시다.')
    st.write('# ', name, '님의 목표 물 섭취량', personal*1000, 'ml')
    #tab2에서 보이는 문구
    
    total = st.session_state.get('total', 0)
    #session_state : 상태유지기능, 물을 얼마큼 마셨는지 입력할 때마다 누적하여 저장, 기본값 0

    amount = st.number_input("마신 물의 양을 입력하세요 (ml):", value = 0, step = 1, key='amount_input')
    #number_input : 마신 물의 양 입력받기. 시작은 0부터 1씩 step. 고유 key 'amount_input' 부여
    
    if amount > 0:
        total += amount
        #마신 물 입력할 때마다 total에 더하기
        remain = personal*1000 - total
        #본인의 하루 권장량(L -> ml) - 총 마신 물 = 목표까지 남은 물
        
        st.session_state['total'] = total
        #상태유지기능, 마신 물의 양을 누적하여 저장
        st.success("데이터가 저장되었습니다.")
        #초록색 창에 뜰 문구
        
        if total < personal*1000:
            st.write("누적 물 섭취량:", total, "ml")
            st.write("남은 물 섭취량:", remain, "ml")
        #총 마신 물이 본인의 하루 권장량을 넘지 못했다면 계속해서 누적, 남은 물 보여주기
            
        else:
            st.write("누적 물 섭취량:", total, "ml")
            st.write("축하합니다! 목표를 달성하셨습니다. 수고하셨어요!")
            st.balloons()
        #총 마신 물이 본인의 하루 권장량을 넘겼다면 누적 물의 양과, 목표 달성했다는 문구 보여주기
        #그리고 풍선 효과
        
