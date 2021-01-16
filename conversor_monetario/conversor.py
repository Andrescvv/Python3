def money_Changer(currency, currency_value):

    currency_amount = float(input("How many " + currency + " do you have?: "))

    dolars = (currency_amount / currency_value)
    dolars = str(round(dolars, 2))

    print("You have $" + dolars + " dolars")
    
    return 

welcome_message = """ 
❤ Welcome to the currency changer ❤
Choose one of this three options to convert in dolars

1: Pesos colombianos 
2: Pesos argentinos 
3: Colones costarricenses 

Your option: """

chosen_option = int(input(welcome_message))

if chosen_option == 1:
    money_Changer("pesos colombianos", 3462.11)

elif chosen_option == 2:
    money_Changer("pesos argentinos", 85.74)

elif chosen_option == 3:
    money_Changer("colones costarricenses", 611.59)

else:
    print("Choose a correct number")
