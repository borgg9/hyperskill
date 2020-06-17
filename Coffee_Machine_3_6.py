import math

print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")

# 1 cup  
water = 200
milk = 50
coffe_beans = 15

# material disponible
water_mat = int(input('Write how many ml of water the coffee machine has:'))
milk_mat = int(input('Write how many ml of milk the coffee machine has:'))
coffe_beans_mat = int(input('Write how many grams of coffee beans the coffee machine has:'))

# cups solicitadas
cups = int(input('Write how many cups of coffee you will need:'))

# Material necesario para las cups solicitadas
water_cups = water * cups
milk_cups = milk * cups
coffe_beans_cups = coffe_beans * cups

# material sobrante (después de producir las cups solicitadas)
water_sobra = water_mat - water_cups
milk_sobra = milk_mat - milk_cups
coffe_beans_sobra = coffe_beans_mat - coffe_beans_cups

# cups disponibles (después de producir las cups solicitadas)
water_sobra_cups = water_mat / water
milk_sobra_cups = milk_mat / milk
coffe_beans_sobra_cups = coffe_beans_mat / coffe_beans
disponibles = water_sobra_cups, milk_sobra_cups, coffe_beans_sobra_cups
min_disponibles = []
for num in disponibles:
    num = math.floor(num)
    if num >= 0:
        min_disponibles.append(num)
min_disponibles = min(min_disponibles)

# cups adicionales
water_adicional = water_sobra/water
milk_adicional = milk_sobra/milk
coffe_beans_adicional = coffe_beans_sobra/coffe_beans
adicional = water_adicional, milk_adicional, coffe_beans_adicional
min_adicional = (min(adicional))


if water_cups <= water_mat and milk_cups <= milk_mat and coffe_beans_cups <= coffe_beans_mat:
    if min(disponibles) > 1:
        print("Yes, I can make that amount of coffee (and even {} more than that)".format(math.floor(min_adicional)))
    else:
        print("Yes, I can make that amount of coffee")
if water_cups > water_mat or milk_cups > milk_mat or coffe_beans_cups > coffe_beans_mat:
    print("No, I can make only {} cups of coffee".format(math.floor(min_disponibles)))
