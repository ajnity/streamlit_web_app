import streamlit as st
from PIL import Image

# text
st.title("おみくじアプリ")
st.caption("今日の運勢はどうかな？")

col1, col2 = st.columns(2)

with col1:

  st.subheader("使い方")
  st.text("右のフォームにあなたの情報を入力して,\n"
          "「GO！」ボタンを押してね。")

  # code = '''
  # import streamlit as st
  # st.title("apuli")
  # '''
  # st.code(code, language="python")

  # image
  image = Image.open("pic/pic.png")
  st.image(image, width=200)

with col2:
  with st.form(key="formu"):
    # textbox
    name = st.text_input("なまえ")
    # print(name)
    # address = st.text_input("jusho")

    # select
    age_category = st.radio(
      "今の気分",
      ("こども", "おとな"))

    # multi select
    hobby = st.multiselect(
      "趣味",
      ("スポーツ", "読書", "グルメ", "旅行", "その他"))

    # button
    submit_btn = st.form_submit_button("GO！")
    cansel_btn = st.form_submit_button("やめとく")

    # print(f"submit_btn:{submit_btn}")
    # print(f"cansel_btn:{cansel_btn}")
    if submit_btn:
      st.text("今日の運勢は、、、\n"
              f"{name}さん！あなたは「中吉」です！")
      result_image = Image.open("pic/chu-kichi.png")
      st.image(result_image, width=100)
      if hobby:
        st.text(f"{' '.join(hobby)}でも良い結果がでそうです！")
      st.text("今日も良い日でありますように～～")
      # st.text(f"shumiha {', '.join(hobby)}")
