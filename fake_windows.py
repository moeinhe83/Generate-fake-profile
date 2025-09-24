# Generate Fake Name And Email

# Library
from faker import Faker
from os import system as sys
from pyfiglet import figlet_format
from termcolor2 import colored

# Clear Terminal
sys('cls')

# Intro
print('                                                  ')
print(colored(figlet_format('Generates Fake Profile'), color='cyan'))
print(colored('======================================================================', color='green'))
print('                                                  ')

# While True
while True:

    # Call Faker
    fake = Faker()

    # Production
    print(f"Your Fake Email ===> {fake.email()}")
    print(f"Your Fake Name ===> {fake.name()}")

    # Try Again
    print('                                               ')
    con = input(colored('Do you want try again [y/n] ===> ', color='blue'))

    # IF For Try Again
    if con == 'y' or con == 'Y':
        continue

    elif con == 'n' or con == 'N':
        print(colored(
            '======================================================', color='blue'))
        print(colored(figlet_format('Good Luck'), color='light_red'))
        break

# Finish
# Create By Moein Heshmati
# moeinit.com
