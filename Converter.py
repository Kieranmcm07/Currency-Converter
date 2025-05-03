# 🌟 Currency Converter by Kieran 🌟

# This program converts a given amount of money from one currency to another using exchange rates.
# The user can choose the currencies and the amount to convert.

# 💱 Exchange rates for the most traded currencies
exchange_rates = {
    "USD": 1.0,      # 🇺🇸 United States Dollar
    "GBP": 0.7534,   # 🇬🇧 British Pound Sterling
    "EUR": 0.8509,   # 🇪🇺 Euro
    "JPY": 155.22,   # 🇯🇵 Japanese Yen
    "CNY": 7.2706,   # 🇨🇳 Chinese Yuan Renminbi
    "AUD": 1.3819,   # 🇦🇺 Australian Dollar
    "CAD": 1.3819,   # 🇨🇦 Canadian Dollar
    "CHF": 0.8265,   # 🇨🇭 Swiss Franc
    "HKD": 7.2706,   # 🇭🇰 Hong Kong Dollar
    "SEK": 10.84     # 🇸🇪 Swedish Krona
}

import paste  # Custom module for additional functionality (e.g., headings, currency lists)

def convert(from_currency, to_currency, amount):
    """
    Converts a given amount from one currency to another using exchange rates.
    """
    try:
        # Convert 'amount' in 'from_currency' to USD first
        usd_amount = amount / exchange_rates[from_currency]

        # Then, convert USD to the target 'to_currency'
        converted_amount = usd_amount * exchange_rates[to_currency]
        return converted_amount
    except KeyError:
        # Handle invalid currency codes
        print("\n❌ Invalid currency code. Please use one from the list.")
        return None

def is_valid_amount(amount):
    """
    Validates if the entered amount is a valid number (handles commas).
    """
    try:
        float(amount.replace(",", ""))  # Remove commas and check if it's a valid float
        return True
    except ValueError:
        return False

def menu():
    """
    Main menu for the currency converter. Allows users to perform multiple conversions.
    """
    while True:  # Loop for continuous conversions
        # Display the heading and instructions
        print(f"{paste.heading}\n\n🌍 Welcome to the Currency Converter! 🌍")
        print("💡 Please select the currencies you want to convert from and to.")
        print("\n📅 NOTE: The exchange rates are based on the latest available data as of Sunday, 4 May 2025.\n")
        print(f"💱 You can choose from the following most traded currencies:\n{paste.currencies}\n")

        # Get the currency to convert from
        from_currency = input("🔤 Enter the currency you want to convert from (e.g., USD): ").upper()
        if from_currency not in exchange_rates:
            print("\n❌ Invalid currency code entered for 'from' currency. Please choose from the listed currencies.")
            continue

        # Get the currency to convert to
        to_currency = input("🔤 Enter the currency you want to convert to (e.g., EUR): ").upper()
        if to_currency not in exchange_rates:
            print("\n❌ Invalid currency code entered for 'to' currency. Please choose from the listed currencies.")
            continue

        # Get the amount to convert
        amount = input("💰 Enter the amount you want to convert: ")

        # Validate the entered amount
        if not is_valid_amount(amount):
            print("\n❌ Invalid amount entered. Please enter a valid number.")
            continue

        # Perform the conversion
        result = convert(from_currency, to_currency, float(amount.replace(",", "")))

        # Display the result if the conversion was successful
        if result:
            print(f"\n✅ Conversion Successful!")
            print(f"💱 {amount} {from_currency} = {result:.2f} {to_currency} 🌟")

        # Ask if the user wants to perform another conversion
        again = input("\n🔄 Would you like to perform another conversion? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Goodbye! Thank you for using the Currency Converter! 🌟")
            break

# 🚀 Run the menu function to start the program
menu()