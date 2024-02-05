import json

list_of_games = [
    {
        "title": "Spyro",
        "platform": "Playstation",
    },
    {
        "title": "Halo",
        "platform": "Xbox",
    },
    {
        "title": "Crash Bandicoot",
        "platform": "Playstation",
    },
    {
        "title": "Gears of War",
        "platform": "Xbox",
    }
]

xbox_games = list(filter(lambda d: d["platform"] == "Xbox", list_of_games))

playstation_games = list(filter(lambda d: d["platform"] == "Playstation", list_of_games))

with open('xbox.json', 'w') as f:
    content = json.dumps(xbox_games, indent = 4)
    f.write(content)
    f.close()

with open('playstation.json', 'w') as f:
    content = json.dumps(playstation_games, indent = 4)
    f.write(content)
    f.close()