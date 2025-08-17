#streamlit is an open source framework which create web apps for machine learning and data secince
#uses ml model can deployed easily and quickly
import streamlit as st


st.image("123.png")
#BASCI FEATURES: title,heasder,code latex,caption,markdown
#widgets FEATURES: checkbox,slider,button,radio,selectbox,time_input()
st.title("welcome to my web")
# title is used to set the title of the web app
st.header("this is header")
# this is used to set the header of the web app
st.subheader("this is sub header")
# this is used to set the sub header of the web app
st.info("this is info")
# this is used to set the info of the web app
st.warning("this is warning")
# this is used to set the warning of the web app
st.write("this is write")
# this is used to write the text in the web app
st.error("this is error")
# this is used to set the error of the web app
st.success("this is success")
# this is used to set the success of the web app
st.markdown(" # this is markdown")
# this is used to set the markdown of the web app
st.markdown("# this is markdown")
# this is used to set the markdown of the web app
st.markdown("::moon")
# this is used to set the markdown of the web appst
st.caption("this is caption")
# this is used to set the caption of the web app


st.latex(r'''E=mc^2''')
# this is used to set the latex of the web app

st.checkbox("this is checkbox")
# this is used to set the checkbox of the web app

st.button("this is button")
# this is used to set the button of the web app
st.radio("this is radio", ["option 1", "option 2", "option 3"])
# this is used to set the radio of the web app
st.selectbox("this is selectbox", ["option 1", "option 2", "option 3"])
# this is used to set the selectbox of the web app
st.multiselect("this is multiselect", ["option 1", "option 2", "option 3"])
# this is used to set the multiselect of the web app
st.slider("this is slider", 0, 100, 50)
# this is used to set the slider of the web app
st.select_slider("this is select slider", options=["option 1", "option 2", "option 3"])
# this is used to set the select slider of the web app
st.text_input("this is text input")
# this is used to set the text input of the web app
st.number_input("this is number input", 0, 100, 50)
# this is used to set the number input of the web app
st.text_input("this is text input", "default text")
# this is used to set the text input of the web app with default text   
st.text_area("this is text area")
# this is used to set the text area of the web app
st.date_input("this is date input")
# this is used to set the date input of the web app 
st.time_input("this is time input")
# this is used to set the time input of the web app 
st.file_uploader("this is file uploader")
# this is used to set the file uploader of the web app
st.color_picker("this is color picker")
# this is used to set the color picker of the web app
st.progress(50)
# this is used to set the progress of the web app
st.spinner("this is spinner")
# this is used to set the spinner of the web app
st.balloons()
# this is used to set the balloons of the web app
st.sidebar.title("Sidebar")
# this is used to set the sidebar of the web app
st.sidebar.header("Sidebar Header")
# this is used to set the sidebar header of the web app
st.sidebar.subheader("Sidebar Sub Header")
# this is used to set the sidebar sub header of the web app
st.sidebar.info("Sidebar Info")
# this is used to set the sidebar info of the web app
st.sidebar.warning("Sidebar Warning")
# this is used to set the sidebar warning of the web app
st.sidebar.success("Sidebar Success")
# this is used to set the sidebar success of the web app
st.sidebar.error("Sidebar Error")
# this is used to set the sidebar error of the web app  
st.sidebar.markdown(" # Sidebar Markdown")
# this is used to set the sidebar markdown of the web app
st.sidebar.caption("Sidebar Caption")
# this is used to set the sidebar caption of the web app
st.sidebar.latex(r'''E=mc^2''')
# this is used to set the sidebar latex of the web app
st.sidebar.checkbox("Sidebar Checkbox")
# this is used to set the sidebar checkbox of the web app
st.sidebar.button("Sidebar Button")
# this is used to set the sidebar button of the web app
st.sidebar.radio("Sidebar Radio", ["option 1", "option 2", "option 3"])
# this is used to set the sidebar radio of the web app
st.sidebar.selectbox("Sidebar Selectbox", ["option 1", "option 2", "option 3"])
# this is used to set the sidebar selectbox of the web app
st.sidebar.multiselect("Sidebar Multiselect", ["option 1", "option 2", "option 3"])
# this is used to set the sidebar multiselect of the web app
st.sidebar.slider("Sidebar Slider", 0, 100, 50)
# this is used to set the sidebar slider of the web app
st.sidebar.select_slider("Sidebar Select Slider", options=["option 1", "option 2", "option 3"])
# this is used to set the sidebar select slider of the web app
st.sidebar.text_input("Sidebar Text Input")
# this is used to set the sidebar text input of the web app
st.sidebar.number_input("Sidebar Number Input", 0, 100, 50)
# this is used to set the sidebar number input of the web app
st.sidebar.text_input("Sidebar Text Input", "default text")
# this is used to set the sidebar text input of the web app with default text
st.sidebar.text_area("Sidebar Text Area")
# this is used to set the sidebar text area of the web app
st.sidebar.date_input("Sidebar Date Input")
# this is used to set the sidebar date input of the web app
st.sidebar.time_input("Sidebar Time Input")
# this is used to set the sidebar time input of the web app
st.sidebar.file_uploader("Sidebar File Uploader")
# this is used to set the sidebar file uploader of the web app
st.sidebar.color_picker("Sidebar Color Picker")
# this is used to set the sidebar color picker of the web app
st.sidebar.progress(50)
# this is used to set the sidebar progress of the web app
st.sidebar.spinner("Sidebar Spinner")
# this is used to set the sidebar spinner of the web app
st.sidebar.balloons()

# this is used to set the sidebar balloons of the web app


