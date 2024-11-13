def main():
    price = float(input("Enter price: "))
    discount = float(input("Enter discount: "))
    result = calculate_discount(price, discount)
    print(f"Amount to pay: {result}")


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    else:
        return price


if __name__ == "__main__":
    main()