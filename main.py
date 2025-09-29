import requests
from send_email import send_email
import smtplib, ssl

api = "1d0bda63cd0b42919489ac78c98ba423"

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2025-08-29&" \
      "sortBy=publishedAt&" \
      "apiKey=1d0bda63cd0b42919489ac78c98ba423&" \
      "language=en"    #go to api url properties and under api documents find endpoints

#make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()        #content = request.txt use json() for more readable format

#Access the article titles and authors
body = ""
for article in content["articles"][:4]:
    if article["title"] is not None:
        body = "Subject: Todays news" + "\n" \
               + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"
body = body.encode('utf-8')
send_email(message = body)
    #print(article["author"])
    #print(article["title"])



print(type(content))
#print(content["articles"])     #use debugger to see the details of the data structure