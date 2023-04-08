import webbrowser

webbrowser.open("https://youtu.be/rCyou4Cz3J0")

print("Welcome to the Dojo !")
print("You will be facing off against the computer in a series of duels.")
print("The first player to win 3 duels will be crowned the champion of the dojo!")

# initialiser les scores
votre_score = 0
score_ordinateur = 0

while votre_score < 3 and score_ordinateur < 3:
    print("Score : You {} - {} Computer".format(votre_score, score_ordinateur))
    choix = input("Choose a card (1 = Ice, 2 = Water, 3 = Fire) ")

    if choix not in ["1", "2", "3"]:
        print("Invallid choice")
        continue

    choix = int(choix)

    if choix == 1:
        print("You played :  Ice")
    elif choix == 2:
        print("You played :  Water")
    else:
        print("You played :  Fire")

    import random

    choix_ordinateur = random.randint(1, 3)

    if choix_ordinateur == 1:
        print("The computer played :  Ice")
    elif choix_ordinateur == 2:
        print("The computer played :  Water")
    else:
        print("The computer played :  Fire")

    if choix == 1 and choix_ordinateur == 2 or choix == 2 and choix_ordinateur == 3 or choix == 3 and choix_ordinateur == 1:
        print("You won this round")
        votre_score += 1
    elif choix == choix_ordinateur:
        print("Tie")
    else:
        print("Computer won")
        score_ordinateur += 1

#score final
print("Final Score : You {} - {} Computer".format(votre_score, score_ordinateur))

if votre_score > score_ordinateur:
    print("You win !")
else:
    print("Computer won")
