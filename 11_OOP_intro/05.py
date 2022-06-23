shop_wallet = 50


class Products:

    def __init__(self, name, price, size, quantity):
        self.name = name
        self.price = price
        self.size = size
        self.quantity = quantity

    def try_product(self, user_size):
        if user_size == self.size:
            print("Product suits you")
        else:
            print("Product doesn't suits you")

    def buy_product(self):
        global shop_wallet
        self.quantity -= 1
        shop_wallet += self.price

    def return_product(self):
        global shop_wallet
        self.quantity += 1
        shop_wallet -= self.price

    def show_product(self):
        print(f'{self.name}, Price: {self.price}, Size: {self.size}, Quantity: {self.quantity}')


def main():
    shop = list()
    shop.append(Products('jacket', 20, 'L', 10))
    shop.append(Products('jeans', 15, 'XL', 10))

    for item in shop:
        item.show_product()
    shop[0].buy_product()
    print(shop_wallet)
    shop[0].show_product()
    shop[0].try_product('L')
    shop[0].return_product()
    print(shop_wallet)


if __name__ == '__main__':
    main()
