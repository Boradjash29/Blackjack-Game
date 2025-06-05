import random

print("----- WELCOME TO BLACKJACK GAME -----")

# Function to deal a random card
def deal_card():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return random.choice(cards)

# Function to calculate total hand value
def calculate_total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            total += 11
            aces += 1
        else:
            total += int(card)

    # Adjust for Ace if total is more than 21
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

# Main game loop
while True:
    player = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]

    print("Your hand:", player)
    print("Dealer's hand: [", dealer[0], ", X ]")

    # Player's turn
    while calculate_total(player) < 21:
        choice = input("Hit or Stand? (h/s): ").lower()
        if choice == 'h':
            player.append(deal_card())
            print("Your hand:", player)
        else:
            break

    player_total = calculate_total(player)

    if player_total > 21:
        print("You busted! Dealer wins.")
    else:
        # Dealer's turn
        while calculate_total(dealer) < 17:
            dealer.append(deal_card())

        dealer_total = calculate_total(dealer)

        print("Your hand:", player, "Total:", player_total)
        print("Dealer's hand:", dealer, "Total:", dealer_total)

        # Decide winner
        if dealer_total > 21 or player_total > dealer_total:
            print("You win!")
        elif dealer_total > player_total:
            print("Dealer wins.")
        else:
            print("It's a draw.")

    # Play again?
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
