import requests

URL = "https://httpbin.org/user-agent"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'
}

page = requests.get(URL,headers=headers)

print(page.text)

