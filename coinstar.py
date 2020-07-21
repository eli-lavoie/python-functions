def calc_dollars(**coins):
    dollar_value = 0
    for key, value in coins.items():
        if key == "pennies":
            penny_val = value * .01
            dollar_value += penny_val
        elif key == "nickels":
            nickel_val = value * .05
            dollar_value += nickel_val
        elif key == "dimes":
            dime_val = value * .01
            dollar_value += dime_val
        elif key == "quarters":
            quarter_val = value * .25
            dollar_value += quarter_val
    print(dollar_value)

calc_dollars(pennies = 930, nickels = 107, dimes = 220, quarters = 94)