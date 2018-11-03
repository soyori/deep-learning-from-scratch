class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y

        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy


class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy


if __name__ == "__main__":
    uprice_apple = 100
    uprice_mikan = 150
    num_apple = 2
    num_mikan = 3
    tax = 1.1

    mul_apple = MulLayer()
    mul_mikan = MulLayer()
    add_all = AddLayer()
    mul_tax = MulLayer()

    # forward
    price_apple = mul_apple.forward(uprice_apple, num_apple)
    price_mikan = mul_mikan.forward(uprice_mikan, num_mikan)
    price_all = add_all.forward(price_apple, price_mikan)
    price = mul_tax.forward(price_all, tax)

    print("forward: %s" % price)

    # backward
    dprice = 1
    dprice_all, dtax = mul_tax.backward(dprice)
    dprice_apple, dprice_mikan = add_all.backward(dprice_all)
    duprice_apple, dnum_apple = mul_apple.backward(dprice_apple)
    duprice_mikan, dnum_mikan = mul_mikan.backward(dprice_mikan)

    print(dnum_apple, duprice_apple, dnum_mikan, duprice_mikan, dtax)

