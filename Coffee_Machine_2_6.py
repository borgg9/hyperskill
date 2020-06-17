# entrada de pedido
cups = int(input('Write how many cups of coffee you will need:'))

# suministros necesarios / cup
water = 200
milk = 50
coffe_beans = 15

# suministros pedido 
water_cups = water * cups
milk_cups = milk * cups
coffe_beans_cups = coffe_beans * cups

print("""For {} cups of coffee you will need:
{} ml of water
{} ml of milk
{} g of coffee beans""".format(cups, water_cups, milk_cups, coffe_beans_cups))
