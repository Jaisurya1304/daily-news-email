import content as content
import requests
from send_email import send_email

topics="tesla"

api_key="ac1b1af17c1c4d5fb8320dee002aeb34"
url="https://newsapi.org/v2/everything?"\
    f"q={topics}&" \
    "sortBy=publishedAt&" \
    "apiKey=ac1b1af17c1c4d5fb8320dee002aeb34&" \
    "language=en"

r=requests.get(url)

c=r.json()

body = "Subject: Today's News"+2*"\n"

for article in c["articles"][:15]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) +"\n"+article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

print(body)