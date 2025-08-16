import streamlit as st
st.title("BMI Calculation")
st.markdown("---")

kg=st.number_input("น้ำหนัก (Kg.)",value=60.5,
                   min_value=10.0,max_value=200.0,
                   step=0.5)

cm=st.number_input("ส่วนสูง (cm.)",value=100,
                   min_value=1,max_value=200,
                   step=1)

if st.button("Calcualte"):
    bmi=kg/(cm/100)**2
    st.subheader(f"ค่าดัชนีมวลกายของคุณคือ {bmi:.1f}")
    if bmi<18.5:
        st.info("ผอมไป")
        st.warning("เสี่ยงโรคขาดสารอาหาร")
        st.image("1.png","ผอมไป")
    elif bmi <23:
        st.success("ปกติ")
        st.warning("_____")
        

    
