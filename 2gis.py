import requests
import settings


def getSights(x, y):
    url = settings.getSights + f"q=Достопримечательность&sort_point={x},{y}&key={settings.token}"
    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.InvalidSchema:
        return {"status": "400"}


def getRoute(args, way="multimodal"):
    url = f"https://2gis.ru/directions/points/"
    for val in args:
        url += f"{val[0]}%2C{val[1]}%3B{val[2]}" + "%7C"
    print(url)


print(getSights(37.630866, 55.752256))
getRoute([
    [60.59020, 56.830297, 70000001018760705],
    [37.617774, 55.755836, 4504222397630173],
    [30.422045, 59.838077, 70000001007029916]
])