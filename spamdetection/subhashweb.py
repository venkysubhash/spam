import streamlit as st
import pickle

# from tkinter import Tk, Label, PhotoImage
# wind = Tk()
# wind.geometry("400x400")
# wind.config(bg="123.png")

# my_image = PhotoImage(file="123.png")
# lbl = Label(wind, image=my_image).pack



# from tkinter import PhotoImage
# root = tkinter.Tk()
# # root.title("Spam Detector")
# root.geometry("400x400")

# Load the logo image
# image_path = PhotoImage(file = "123.png")  # Ensure you have a logo.png file in
# bg_image=tkinter.Label(root, image=image_path)
# bg_image.place(relheight=1, relwidth=1)

# text_label =tkinter.Label(root,text="Welcome to Spam Detector",font=("Arial", 20),bg="white",fg="black")
# text_label.pack()



# Load the trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Streamlit app

st.title('Email/Message Spam Detector')
st.image("img.jpg")

st.balloons()
# this is used to set the balloons of the web app

st.sidebar.date_input("Today's Date")
# this is used to set the date input of the web app in the sidebar
st.sidebar.time_input("Current Time")

st.sidebar.selectbox("Type", ["Email", "Message"])


# User input
st.subheader("Cut through the noise! Detect the deception! Deliver only what matters.......")
message = st.text_area("Enter the email/message to classify as SPAM or HAM:", height=200)

if st.button('Detect'):
    if message:
        # Preprocess and transform the input message
        transformed_message = vectorizer.transform([message])
        prediction = model.predict(transformed_message)[0]

        if prediction == 1:
            result = "SPAM"
        else:
            result = "HAM"

        st.write(f'This email is classified as: **{result}**')
    else:
        st.write("Please enter a message to classify.")
    # python -m streamlit run subhashweb.py
# wind.mainloop()
st.info("Thanks for using the Spam Detector!")
st.checkbox("click here if you like this web app")