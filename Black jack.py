print("---------------------------WELCOME TO BLACK JACK GAME -------------------------")

import random

cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']

# Function to calculate the total value of cards
def calculate_total(cards):
    total =sum(cards) 
    if 1 in cards and total + 10 <= 21:
        return total + 10
    return total

#Function to deal a card
def deal_card():
    return random.randint(1,13)
   
# Main game loop 
while True:
    # Initialize player and dealer hands
    player_hand =[deal_card(),deal_card()]   
    dealer_hand = [deal_card(),deal_card()]     
    
    # show initial hands
    print("your hand:",player_hand)
    print("Dealer's hand",[dealer_hand[0],"x"])  # Show only one of the dealer's cards
    
    
    #Player's Turn 
    while calculate_total(player_hand) < 21:
       choice = input("Do you want to hit or stand ? (h/s) :").lower()
       if choice == 'h':
           player_hand.append(deal_card())
           print("your hand :",player_hand)
       elif choice =='s':
           break
       
    player_total = calculate_total(player_hand)
    
    if player_total > 21:
        print("Bust! you lose.")
    else:
        # Dealer's Turn 
        while calculate_total(dealer_hand) < 17 :
            dealer_hand.append(deal_card())
        dealer_total = calculate_total(dealer_hand)  
        
        # show Final hands
        print("Your hand :",player_hand,"Total :",player_total)
        print("Dealer's hand:",dealer_hand,"Total :" ,dealer_total )    
        
        # Determine Winner
        if dealer_total > 21 or player_total > dealer_total:
            print("You Win!!")
        elif dealer_total > player_total :
            print("Dealer Wins.")
        else:
            print("It's a Draw.")    
            
    play_again = input("Do you want to play again ? (y/n):").lower()
    if play_again != 'y':
        break
               
               
    
  