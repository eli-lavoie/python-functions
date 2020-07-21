dollar_amount = 8.69

piggy_bank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def gimme_the_change(money):
    while money != 0:
        if money > .25:
            piggy_bank["quarters"] += 1
            money -= .25
        elif money > .10 and money < .25:
            piggy_bank["dimes"] += 1
            money -= .10
        elif money > .05 and money < .10:
            piggy_bank["nickels"] += 1
            money -= .05
        elif money > .01 and money < .05:
            piggy_bank["pennies"] += 1
            money -= .01
        elif money < .01:
            if money >= .009:
                piggy_bank["pennies"] += 1
                money = 0
            else:
                money = 0
    print(piggy_bank)

gimme_the_change(dollar_amount)