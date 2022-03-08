import streamlit as st
import time

st.title("Title")
st.write("ProgressBar")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

"DONE!"

left_column, right_column = st.columns(2)
button = left_column.button("show right column")
if button:
    right_column.write("right column")

expander1 = st.expander("inquiry1")
expander1.write("answer of inquiry1")
expander2 = st.expander("inquiry2")
expander2.write("answer of inquiry2")
expander3 = st.expander("inquiry3")
expander3.write("answer of inquiry3")
