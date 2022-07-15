stock = {}
final_stock = {}
command = input()
while not command == 'buy':
    product, price, quantity = command.split()
    if product not in stock:
        stock[product] = []
        stock[product].append(float(price))
        stock[product].append(int(quantity))
    else:
        stock[product][0] = float(price)
        stock[product][1] += int(quantity)
    total_price = stock[product][0] * stock[product][1]
    final_stock[product] = total_price

    command = input()
for key, value in final_stock.items():
    print(f'{key} -> {value:.2f}')