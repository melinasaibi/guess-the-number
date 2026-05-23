import random
secret_number = random.randint(0, 100)
while True:
    player_number = int(input("enter the number: "))
    if secret_number < player_number:
        print(f"secret number is smaller than {player_number}")
    elif secret_number > player_number:
        print(f"secret number is greater than {player_number}")
    else:
        print(f"the number is {player_number}")
        break
