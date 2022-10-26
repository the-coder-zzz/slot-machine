from functions import *


def main():
    print('------------------------------------------')
    print('|             =SLOT MACHINE=             |')
    print('------------------------------------------')
    balance = deposit()
    while True:
        print(f"\nCurrent balance is ${balance}")
        answer = input("Press enter to play and 'q' to quit: ").lower()
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
  
main()  
