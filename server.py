from bs4 import BeautifulSoup
import requests
from flask import *
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home_page():
    data_set = {"Page": "Homepage of Cricbuzz Basic API", "Status": "Success!"}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route("/basic", methods=["GET"])
def basic_details():
    url = "https://www.cricbuzz.com"
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    gamesList = soup.findAll("li", class_="cb-view-all-ga cb-match-card cb-bg-white")
    games = []
    for game in gamesList:
        gameText = game.text
        arr = gameText.split(" • ")
        match = arr[0].replace("   ", "")
        leftArr = arr[1].split("   ")
        title = leftArr[0]
        score = leftArr[1]
        data_set = {"Match": match, "Title": title, "Score": score}
        games.append(data_set)
    json_dump = json.dumps(games)
    return json_dump


if __name__ == "__main__":
    app.run()
