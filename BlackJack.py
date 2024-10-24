import random


def cards():
    points = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    return random.choice(points)


def Calculate_Score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            score += 11
            ace_count += 1
        elif card in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            score += card
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
    return score


users_hand = [cards(), cards()]
users_Score = Calculate_Score(users_hand)
print("User's hand: {}".format(users_hand))
print("User's Score: {}".format(users_Score))

dealers_hand = [cards(), cards()]
dealers_score = Calculate_Score(dealers_hand)
print("Dealer's hand: {}".format(dealers_hand))
print("Dealer's Score: {}".format(dealers_score))

Hit = input("Do u want to withdraw another card.Y/N")
while Hit == "y" or Hit == "Y":
    users_hand.append(cards())  # Add a new card to the user's hand
    users_Score = Calculate_Score(users_hand)
    print(users_hand)
    print(users_Score)
    if users_Score > 21:
        print("You loose")
        break
    else:
        Hit = input("Do u want to withdraw another card.Y/N")

while dealers_score < 17:
    dealers_hand.append(cards())
    dealers_score = Calculate_Score(dealers_hand)

if users_Score <= 21:
    if dealers_score > 21:
        print("Dealer busts! You win.")
    elif dealers_score > users_Score:
        print("Dealer wins!")
    elif dealers_score < users_Score:
        print("You win!")
    else:
        print("It's a tie!")