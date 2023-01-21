import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://www.protoclea.com/wp-content/uploads/2019/10/Automatic-number-plate-recognition-icon.png", width=100)
st.sidebar.subheader("Models Used")
st.sidebar.markdown("##### YoloV7: Object detection model to detect the number plate")
st.sidebar.markdown("##### PaddleOCR: OCR to read the number plate")
st.sidebar.markdown("##### Deep SORT: Object tracking algorithm for video detection")

st.sidebar.markdown("##### The YOLOV7 Model was fine-tuned using the ANPR dataset to detect number plates. When a number plate is detected, PaddleOCR is used to read the number plate. For video detection, Deep SORT is used to handle object tracking")

st.sidebar.caption("Streamlit App by </Shahnab>")

st.subheader("Automatic Number Plate Recognition Engine")
# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://lohitkavuru14-anpr-yolov7.hf.space", width=1100, height=650, scrolling=True)
