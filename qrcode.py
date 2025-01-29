import random

def choose():
    words = ["rainbow", "computer", "science", "programming", "mathematics", "player", "condition", "reverse", "water", "board"]
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def thank(p1n, p2n, p1, p2):
    print(p1n, "Your score is: ", p1)
    print(p2n, "Your score is: ", p2)
    print("Thanks for playing")
    print("Have a nice day")

def play():
    p1name = input("Player-1, please enter your name: ")
    p2name = input("Player-2, please enter your name: ")
    pp1 = 0  # player-1 points
    pp2 = 0  # player-2 points
    turn = 0
    while True:
        # Computer's task
        picked_word = choose()
        # Create question
        qn = jumble(picked_word)
        print(qn)
        if turn % 2 == 0:  # it is the turn for the player-1
            print(p1name, "Your turn")
            ans = input("What is on my mind? ")
            if ans == picked_word:
                pp1 += 1
                print("Your current score is: ", pp1)
            else:
                print("Better luck next time. I thought: ", picked_word)
            c = int(input("Press 1 to continue and 0 to quit: "))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break
        else:  # it is the turn for the player-2
            print(p2name, "Your turn")
            ans = input("What is on my mind? ")
            if ans == picked_word:
                pp2 += 1
                print("Your current score is: ", pp2)
            else:
                print("Better luck next time. I thought: ", picked_word)
            c = int(input("Press 1 to continue and 0 to quit: "))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break
        turn += 1

# Lets Play the Game
play()

# Q.5. What is L1 after the function call?
def mystery(L):
    L = L[2:]
    return L

L1 = [7, 11, 13, 17, 19, 21]
mystery(L1)
# L1 remains [7, 11, 13, 17, 19, 21] because slicing creates a new list

# Q.6. What is L1 after the function call?
def mystery(L):
    L[0] = 5
    return L

L1 = [7, 11, 13, 17, 19, 21]
mystery(L1)
# L1 becomes [5, 11, 13, 17, 19, 21] because the list is modified in place