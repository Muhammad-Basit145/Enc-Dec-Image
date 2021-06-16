import streamlit as st
from PIL import Image

image = Image.open('encrypt.jpg')
st.image(image, width=700)

options = ["Select Option", "Encrypt", "Decrypt"]
choice = st.selectbox("Options", options)

if choice == "Select Option":
    st.subheader("")
elif choice == "Encrypt":
    st.subheader("Encrypt Your Image:")

    # take a input of image path
    img_path = st.text_input(r'Enter path of Image:')

    # take input key for an image encryption in 2 digit
    key = st.text_input('Enter Key for encryption or decryption of Image:')
    key = int(key)

    f = open(img_path, 'rb')

    image = f.read()
    f.close()

    image1 = bytearray(image)
    # perform XOR operation on each value of bytearray
    for index, values in enumerate(image1):
        image1[index] = values ^ key

    f1 = open(img_path, 'wb')

    # write encrypted data of image1
    f1.write(image1)
    f1.close()
    if st.button("submit"):
        st.success('Encryption Done...')
        st.write('Encryption key is: ', key)
elif choice == "Decrypt":
    st.subheader("Encrypt Your Image:")

    # take a input of image path
    img_path = st.text_input(r'Enter path of Image:')

    # take input key for an image encryption
    key = st.text_input('Enter Key for encryption or decryption of Image:')
    key = int(key)

    # open file to read data
    f = open(img_path, 'rb')

    # storing image data in image variable
    image = f.read()
    f.close()

    image1 = bytearray(image)
    # perform XOR operation on each value of bytearray
    for index, values in enumerate(image1):
        image1[index] = values ^ key
    f1 = open(img_path, 'wb')
    f1.write(image1)
    f1.close()
    if st.button("Submit"):
        st.success('Decryption Done...')
        st.write('Decryption key is: ', key)
