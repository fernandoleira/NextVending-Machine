import requests
from bs4 import BeautifulSoup

PROFILE_URL = "https://venmo.com/fleira98"
LOGIN_URL = "https://venmo.com/login"
ACCOUNT_LOGIN_URL = "https://venmo.com/account/login"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

sess = requests.Session()

sess.post(
    LOGIN_URL + "?csrftoken2=ZdrMf55paUzKLTTPEUqRPyjz5VaVuSqr&return_json=true&password=Fern19_venmo&phoneEmailUsername=fernandoleiracortel%40outlook.com",
    headers=headers
)

sess.post(
    ACCOUNT_LOGIN_URL + "?csrftoken2=ZdrMf55paUzKLTTPEUqRPyjz5VaVuSqr&return_json=true&username=fleira98&password=Fern19_venmo",
    headers=headers
)
#req = requests.get(URL)
res = login_req.text

sess.close()
print(res)
