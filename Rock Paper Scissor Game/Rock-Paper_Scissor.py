import random

print("--------------- Welcome Player ---------------------")

def Game():
    while True:
        print("\n1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("4 - Exit")
        
        choice = int(input("Enter your choice: "))
        print()
        
        if choice == 4:
            print("------------- Thank you for playing! -------------")
            break
        
        if choice not in [1, 2, 3]:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
            continue
        
        com = random.randint(1, 3)
        print(f"Computer chose: {com}")
        
        match (choice, com):
            case (1, 1) | (2, 2) | (3, 3):
                print("It's a draw!")
            case (1, 3) | (2, 1) | (3, 2):
                print("You win! ")
            case (1, 2) | (2, 3) | (3, 1):
                print("Computer wins! ")
            case _:
                print("Some unexpected error occur!")

Game()
