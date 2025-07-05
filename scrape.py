import requests
from bs4 import BeautifulSoup
import json

url = "https://www.bisafans.de/spiele/mobile/pokemon-go/events/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

events = []
event_boxes = soup.select("div.event-box")
for box in event_boxes:
    title = box.select_one("h3").text.strip() if box.select_one("h3") else "Kein Titel"
    date = box.select_one("p").text.strip() if box.select_one("p") else "Kein Datum"
    events.append({"title": title, "date": date})

with open("data/events.json", "w", encoding="utf-8") as f:
    json.dump(events, f, indent=2, ensure_ascii=False)
