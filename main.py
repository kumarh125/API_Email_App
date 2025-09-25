import requests

api = "1d0bda63cd0b42919489ac78c98ba423"

url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=1d0bda63cd0b42919489ac78c98ba423"

#make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()        #content = request.txt use json() for more readable format

#Access the article titles and authors

for article in content["articles"]:
    print(article["author"])
    print(article["title"])


print(type(content))
#print(content["articles"])     #use debugger to see the details of the data structure