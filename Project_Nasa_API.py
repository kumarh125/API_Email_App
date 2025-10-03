import requests
import streamlit as st

api= "usayCTFEwDnB8u3etshVIJRIPLGvnbtwoC221KlS"

url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api}"

response1 = requests.get(url)

data = response1.json()

response2 = requests.get(data["url"])
imagebytes = response2.content
with open("image.jpeg", "wb") as file:
      file.write(imagebytes)

title = data["title"]
description = data["explanation"]



st.title(title)

st.write(description)
st.subheader("Today pic is...")
st.image("image.jpeg")


#st.session_state





#print(content)



