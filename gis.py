import json
import requests

def PublicTransport(url):
    d = {
        "locale": "ru",
        "source":
        {
            "name": "Point A",
            "point":
            {
                "lat": 51.734588,
                "lon": 36.149328
            }
        },
        "target":
        {
            "name": "Point B",
            "point":
            {
                "lat": 51.734183,
                "lon": 36.176865
            }
        },
        "transport": ["bus", "tram"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    resp = requests.post(url, json=d, headers=headers)
    return resp