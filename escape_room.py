import random

def announce_walls(row, col):
    if room[row - 1][col] == 'x':
        print("Wall to the north.")
    if room[row + 1][col] == 'x':
        print("Wall to the south.")
    if room[row][col + 1] == 'x':
        print("Wall to the east.")
    if room[row][col - 1] == 'x':
        print("Wall to the west.")

def puzzle():
    passwords = ["fire", "water", "earth", "wind"]
    correct = random.choice(passwords)
    for word in passwords:
        if word == correct:
            print(word.capitalize())
        else:
            print(word)
    while True:
        guess = input("Guess the password: ")
        if guess == correct:
            print("You got it!")
            return True  
        else:
            print("Wrong — try again!")


while True:
    print("Welcome to the Escape Room!")

    name = input("What is your name, adventurer? ")
    print(f"The heavy door slams behind you, {name}.")
    print(f"You are alone in the haunted mansion. No phone signal, no easy way out.")
    print(f"The only way out is to escape these dreaded obstacles. Are you up to the challenge {name}! ")
    correct_door = random.choice(["1","2","3"])

    door = input('Which door will you choose: (1, 2, or 3) ')
    while door != correct_door:
        print('Locked!')
        door = input('Which door will you choose: (1, 2, or 3) ')
    else:
        print('Escaped')
        words = ["red","blue","green"]
        password = random.choice(words)
        passcode_guesses = 3
        while passcode_guesses > 0:
            guess = input(f"Guess the passcode ({passcode_guesses} guesses left): ")
            if guess == password:
                print("Correct")
                break 
            
            passcode_guesses -= 1
            if passcode_guesses > 0:
                print("Wrong guess")
        else:
            print(f"Out of guesses! The correct passcode was '{password}'. You lose!")
            break
        

    # Global room layout used by announce_walls
    room = [
        "xxxxxxx",
        "x..x..x",
        "x.x...x",
        "x.p.x.e",
        "xxxxxxx"
    ]

    player_row = 1
    player_col = 1

    def move(current_row, current_col, direction, room):
        new_row = current_row
        new_col = current_col

        if direction == "up":
            new_row = current_row - 1
        elif direction == "down":
            new_row = current_row + 1
        elif direction == "left":
            new_col = current_col - 1
        elif direction == "right":
            new_col = current_col + 1
        else:
            return current_row, current_col

        if room[new_row][new_col] == 'x':
            print("Ouch — a wall.")
            return current_row, current_col
            
        return new_row, new_col

    
    while room[player_row][player_col] != 'e':
        announce_walls(player_row, player_col)
        
        direction = input("Which way? (up/down/left/right): ")
        player_row, player_col = move(player_row, player_col, direction, room)
        print(f"You are at ({player_row}, {player_col})")
        if room[player_row][player_col] == 'p':
            if not puzzle():
                game_over = True
                break  
            else:
                room[player_row] = room[player_row].replace('p', '.')

    
    print("You escaped!")

    play_again = input("Would you like to play again? (yes/no): ").lower().strip()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
