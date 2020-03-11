import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

querystring = {"deck_count":"6"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "51e024f2-f814-4715-aff3-55b15e1d3a8e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
