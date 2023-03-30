import random
import webbrowser

# Banger Music 🥶
webbrowser.open("https://youtu.be/rCyou4Cz3J0")

# Cartes
ICE = 0
WATER = 1
FIRE = 2

CARD_NAMES = ["Glace", "Eau", "Feu"]


def get_player_card():
    # Choix carte par le joueur
    valid_choice = False
    while not valid_choice:
        choice = input("Choose a card (1 = Ice, 2 = Water, 3 = Fire) : ")
        if choice in ["1", "2", "3"]:
            valid_choice = True
            if choice == "1":
                return ICE
            elif choice == "2":
                return WATER
            else:
                return FIRE
        else:
            print("Invallid choice")


def get_computer_card():
    # Carte de l'ordinateur
    return random.randint(0, 2)


def compare_cards(card1, card2):
    # Compare les cartes
    if card1 == card2:
        return 0
    elif (card1 == ICE and card2 == WATER) or (card1 == WATER and card2 == FIRE) or (card1 == FIRE and card2 == ICE):
        return 1
    else:
        return -1


def play_round(player_score, computer_score):
    # Met à jour le score après avoir joué un tour
    player_card = get_player_card()
    computer_card = get_computer_card()
    print("You played : ", CARD_NAMES[player_card])
    print("Computer played : ", CARD_NAMES[computer_card])
    result = compare_cards(player_card, computer_card)
    if result == 1:
        print("You won this round")
        player_score += 1
    elif result == -1:
        print("Computer won this round")
        computer_score += 1
    else:
        print("Tie")
    print("Score : You", player_score, "-", computer_score, "Computer")
    if player_score == 3:
        print("You won this round")
        return False
    elif computer_score == 3:
        print("Computer won this round")
        return False
    else:
        return True


def main():
    # Partie complète
    print("Welcome to the Dojo !")
    print("You will be facing off against the computer in a series of duels.")
    print("The first player to win 3 duels will be crowned the champion of the dojo!")
    player_score = 0
    computer_score = 0
    game_on = True
    while game_on:
        game_on = play_round(player_score, computer_score)


# Lancer le jeu
main()
