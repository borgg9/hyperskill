water_mat = 400 
milk_mat = 540 
coffe_mat = 120 
cups_mat = 9 
money_mat = 550

def machine_situation(water_mat, milk_mat, coffe_mat, cups_mat, money_mat):
    return("""The coffee machine has:
    {} of water
    {} of milk
    {} of coffee beans
    {} of disposable cups
    {} of money""".format(water_mat, milk_mat, coffe_mat, cups_mat, money_mat))


print(machine_situation(water_mat, milk_mat, coffe_mat, cups_mat, money_mat))

action = input('Write action (buy, fill, take):')    

if action == 'buy':
    coffe_type = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:'))    
    
    if coffe_type == 1:
        water_mat = water_mat - 250
        milk_mat = milk_mat - 0
        coffe_mat = coffe_mat - 16
        cups_mat = cups_mat - 1
        money_mat = money_mat + 4
        
    elif coffe_type == 2:
        water_mat = water_mat - 350
        milk_mat = milk_mat - 75
        coffe_mat = coffe_mat - 20
        cups_mat = cups_mat - 1
        money_mat = money_mat + 7
        
    elif coffe_type == 3:
        water_mat = water_mat - 200
        milk_mat = milk_mat - 100
        coffe_mat = coffe_mat - 12
        cups_mat = cups_mat - 1
        money_mat = money_mat + 6
        
    print(machine_situation(water_mat, milk_mat, coffe_mat, cups_mat, money_mat))
    
    
if action == 'fill':
    water_mat = water_mat + int(input('Write how many ml of water do you want to add:'))
    milk_mat = milk_mat + int(input('Write how many ml of milk do you want to add:'))
    coffe_mat = coffe_mat + int(input('Write how many grams of coffee beans do you want to add:'))
    cups_mat = cups_mat + int(input('Write how many disposable cups of coffee do you want to add:'))
        
    print(machine_situation(water_mat, milk_mat, coffe_mat, cups_mat, money_mat))
    

if action == 'take':
    print('I gave you ${}'.format(money_mat))
    money_mat = 0
    print(machine_situation(water_mat, milk_mat, coffe_mat, cups_mat, money_mat))
