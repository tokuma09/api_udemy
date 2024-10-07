import requests


def main():
    url = "http://127.0.0.1:8000/item/"
    body = {"name": "T-shirt", "description": "This is a T-shirt", "price": 5980, "tax": 1.1}

    res = requests.post(url, json=body)
    print(res.json())


if __name__ == "__main__":
    main()
