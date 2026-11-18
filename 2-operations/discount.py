product_price = float(input("Цена товара: "))
discount_percentage = float(input("Процент скидки: "))

discounted_price = product_price - product_price*discount_percentage/100

print(discounted_price)