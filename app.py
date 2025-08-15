import streamlit as st

st.title("サンプルアプリ②: 少し複雑なWebアプリ")

mode = st.radio(
    "動作モードを選択してください。",
    ("文字数カウント", "BMI値の計算")
)

if mode == "文字数カウント":
    text = st.text_input("文字数のカウント対象となるテキストを入力してください。")
    if st.button("実行"):
        st.write(f"文字数: {len(text)}")

elif mode == "BMI値の計算":
    height = st.number_input("身長(cm)", min_value=100, max_value=250, value=170)
    weight = st.number_input("体重(kg)", min_value=30, max_value=150, value=60)
    if st.button("実行"):
        bmi = weight / ((height/100) ** 2)
        st.write(f"BMI値: {bmi:.2f}")
