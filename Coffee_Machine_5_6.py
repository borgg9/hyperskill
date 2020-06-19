water_mat = 400 
milk_mat = 540 
coffe_mat = 120 
cups_mat = 9 
money_mat = 550

action = ''

while action != 'exit':
    action = input('Write action (buy, fill, take, remaining, exit):') 
    
    if action == 'buy':
        coffe_type = (input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'))    

        if coffe_type == '1':
            if water_mat >= 250 and milk_mat >= 0 and coffe_mat >= 16 and cups_mat >= 1:
                print('I have enough resources, making you a coffee!')
                water_mat = water_mat - 250
                milk_mat = milk_mat - 0
                coffe_mat = coffe_mat - 16
                cups_mat = cups_mat - 1
                money_mat = money_mat + 4
            else:
                if water_mat >= 250: print('Sorry, not enough water!')
                if milk_mat >= 0: print('Sorry, not enough milk!')
                if coffe_mat >= 16: print('Sorry, not enough coffee beans!')
                if cups_mat >= 1: print('Sorry, not enough cups!')
                    
        if coffe_type == '2':
            if water_mat >= 350 and milk_mat >= 75 and coffe_mat >= 20 and cups_mat >= 1:
                print('I have enough resources, making you a coffee!')
                water_mat = water_mat - 350
                milk_mat = milk_mat - 75
                coffe_mat = coffe_mat - 20
                cups_mat = cups_mat - 1
                money_mat = money_mat + 7
            else:
                if water_mat >= 350: print('Sorry, not enough water!')
                if milk_mat >= 75: print('Sorry, not enough milk!')
                if coffe_mat >= 20: print('Sorry, not enough coffee beans!')
                if cups_mat >= 1: print('Sorry, not enough cups!')

        if coffe_type == '3':
            if water_mat >= 200 and milk_mat >= 100 and coffe_mat >= 12 and cups_mat >= 1:
                print('I have enough resources, making you a coffee!')
                water_mat = water_mat - 200
                milk_mat = milk_mat - 100
                coffe_mat = coffe_mat - 12
                cups_mat = cups_mat - 1
                money_mat = money_mat + 6
            else:
                if water_mat >= 200: print('Sorry, not enough water!')
                if milk_mat >= 100: print('Sorry, not enough milk!')
                if coffe_mat >= 12: print('Sorry, not enough coffee beans!')
                if cups_mat >= 1: print('Sorry, not enough cups!')

        elif coffe_type == 'back':
            continue
                 
    if action == 'fill':
        water_mat = water_mat + int(input('Write how many ml of water do you want to add:'))
        milk_mat = milk_mat + int(input('Write how many ml of milk do you want to add:'))
        coffe_mat = coffe_mat + int(input('Write how many grams of coffee beans do you want to add:'))
        cups_mat = cups_mat + int(input('Write how many disposable cups of coffee do you want to add:'))

    if action == 'take':
        print('I gave you ${}'.format(money_mat))
        money_mat = 0
            
    if action == 'remaining':
        print("""The coffee machine has:
            {} of water
            {} of milk
            {} of coffee beans
            {} of disposable cups
            ${} of money""".format(water_mat, milk_mat, coffe_mat, cups_mat, money_mat))     
             
    if action == 'exit':
        break
