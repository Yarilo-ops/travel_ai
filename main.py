import requests


def post(address, **kwargs):
    return requests.post(address, kwargs)


def get(address, **kwargs):
    return requests.get(address, kwargs)


token = "e54ece61-706e-4274-9daa-51a572cf8c7c"
dicts = {
    "points": [
        {
            "type": "walking",
            "x": 82.93057,
            "y": 54.943207
        },
        {
            "type": "bus",
            "x": 82.945039,
            "y": 55.033879
        }
    ]
}

if __name__ == "__main__":
    response = requests.post(f"https://routing.api.2gis.com/carrouting/6.0.0/global?key={token}", json=dicts)
    print(response.json()["result"])
