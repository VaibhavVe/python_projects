import requests
api = "223cc7faabfd403998fa9670de5acc8d"
query = input("What type of news are you interested in today")

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-10&sortBy=publishedAt&apiKey={api}"
#print(url)
r = requests.get(url)
data = r.json()
articles = data["articles"]
for index, article in enumerate(articles):
    print(index+1, article["title"], "\nLink:-", article ["url"])
    print("\n\n")


