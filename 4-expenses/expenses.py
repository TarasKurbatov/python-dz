RUB_WORDS = {"руб", "рубль", "рубля", "рублей"}
KOP_WORDS = {"коп", "копейка", "копейки", "копеек"}

price = input("Введите сумму: ")
price_trim = " ".join(price.lower().split())
price_parts = price_trim.split()

if (len(price_parts) == 4
        and price_parts[1] in RUB_WORDS
        and price_parts[3] in KOP_WORDS
        and price_parts[0].isdigit()
        and price_parts[2].isdigit()):
    rub = int(price_parts[0])
    kop = int(price_parts[2])
    if 0 <= kop < 100:
        total = rub + kop / 100
        print(f"{total:.2f} ₽")
    else:
        print("Некорректный формат суммы")

elif (len(price_parts) == 2
        and price_parts[1] in RUB_WORDS
        and price_parts[0].isdigit()):
    rub = int(price_parts[0])
    print(f"{rub:.2f} ₽")

else:
    print("Некорректный формат суммы")