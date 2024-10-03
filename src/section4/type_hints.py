from typing import Dict, List


def calc_price_including_tax(price: int, tax: float) -> int:
    return int(price * tax)


if __name__ == "__main__":
    price: int = 100
    tax: float = 1.1
    print(f"{calc_price_including_tax(price=price, tax=tax)}円")

    sample_list: List[int] = [1, 2, 3, 4]
    sample_dict: Dict[str, str] = {"user_name": "abcd"}
