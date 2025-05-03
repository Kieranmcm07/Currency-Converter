# Currency Converter by Kieran

# This program converts a given amount of money from one currency to another using exchange rates.
# The user can choose the currencies and the amount to convert.

import paste

def menu():

    print(f"{paste.heading}\n\nWelcome to the Currency Converter!\nPlease select the currencies you want to convert from and to.")
    print(f"You can choose from the following most traded currencies:\n {paste.currencies}\n")


    # User input for currency conversion
    from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
    amount = float(input("Enter the amount you want to convert: "))

menu()