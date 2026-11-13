# Part A 모범답안 (채점기 기준 50점 만점)


def delivery_fee(total, distance):
    if total >= 30000:
        return 0
    elif distance < 2:
        return 2000
    elif distance < 5:
        return 3000
    else:
        return 5000


def find_winners(numbers):
    winners = []
    for i in range(len(numbers)):
        if 10 <= numbers[i] <= 17:
            winners.append(i + 1)
    return winners


def order_total(menu, orders):
    total = 0
    unknown = 0
    for name in orders:
        if name in menu:
            total += menu[name]
        else:
            unknown += 1
    return total, unknown


class SoldOutError(Exception):
    pass


class UdonKiosk:
    PRICE = 7000

    def __init__(self, stock):
        self.stock = stock
        self.sold = 0

    def order(self, text):
        if self.stock == 0:
            raise SoldOutError("매진되었습니다.")
        count = int(text)            # "abc", "1.5" 는 여기서 ValueError 발생
        if count < 1:
            raise ValueError("1 이상의 정수만 주문할 수 있습니다.")
        if count > self.stock:
            raise ValueError("남은 수량보다 많이 주문할 수 없습니다.")
        self.stock -= count
        self.sold += count
        return count * self.PRICE

    def total_sales(self):
        return self.sold * self.PRICE


def main():
    print("문제 1 :", delivery_fee(12000, 3))
    print("문제 2 :", find_winners([10, 20, 17, 9]))
    menu = {"비빔우동": 7000, "튀김우동": 8000, "유부초밥": 4000}
    print("문제 3 :", order_total(menu, ["비빔우동", "유부초밥", "비빔우동", "돈까스"]))
    kiosk = UdonKiosk(3)
    print("문제 4 :", kiosk.order("2"))
    print("문제 4 :", kiosk.stock, kiosk.sold)
    print("문제 4 :", kiosk.total_sales())


if __name__ == "__main__":
    main()
