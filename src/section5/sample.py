import requests


def main():
    url = "http://127.0.0.1:8000"
    data = {"x": 1.0, "y": 2.0}

    res = requests.post(url, json=data)

    print(res.json())


if __name__ == "__main__":
    main()
