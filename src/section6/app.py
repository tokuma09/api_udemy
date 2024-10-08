from email.policy import default

import numpy as np
import pandas as pd
import streamlit as st

number = st.sidebar.slider(label="Pick a number", min_value=0, max_value=100, value=25)
st.sidebar.write(f"number = {number}")
left_column, right_column = st.columns(2)

left_column.slider("slider", 0, 100, 25)
right_column.write("right column")


# st.title("sample app")

# if st.button("Click me"):
#     st.write("Button clicked!")

# if st.checkbox("Check me"):
#     st.write("Checkbox checked!")


# options = st.multiselect(
#     label="What are your favorite colors", options=["Green", "Yellow", "Red", "Blue"], default=["Yellow", "Red"]
# )
# st.write(f"選択肢: {options}")

# number = st.slider(label="Pick a number", min_value=0, max_value=100, value=25)
# st.write(f"number = {number}")

# df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)


# st.markdown("""
#             # 見出し1
#             ## 見出し2
#             ### 見出し3

#             - 箇条書き1
#             - 箇条書き2
#             - 箇条書き3
#             """)

# st.code("""
#         a=123
#         import numpy as np
#         import pandas as pd
#         df = pd.DataFrame()
#         """)

# df = pd.DataFrame(np.random.randn(50, 20), columns=["col %d" % i for i in range(20)])

# st.dataframe(df.style.highlight_max(axis=0))


# st.json({"foo": "bar", "stuff": ["stuff1", "stuff2"], "level1": {"level2": {"level3": {"a": "b"}}}})
# st.json({"foo": "bar", "stuff": ["stuff1", "stuff2"], "level1": {"level2": {"level3": {"a": "b"}}}})
