from p1_random import P1Random

rng = P1Random()   #outside of loop

# print(rng.next_int(13) + 1)

game_continue = True
game_num = 0
num_player_wins = 0
num_dealer_wins = 0
num_tie_games = 0
total_gam_played = 0
pers_player_wins = 0

# Control the number of games the player will play
while game_continue:   # gmae #1, #2, #3
    game_num += 1
    print(f"START GAME #{game_num}")
    print()
    #2. deal a card to the player automatically
    player_hand = 0

    # deal a card to the player
    card = rng.next_int(13) + 1  # [0, 12] + 1 => [1, 13]

    if card == 1:
        player_hand = 1
        print("Your card is a ACE!")
        print(f"Your hand is: {player_hand}\n")
    elif 2 <= card <= 10:               # need to use a NESTED IF STATEMENT
        if card == 2:
            player_hand = 2
            print(f"Your card is a {card}!")
            print(f"Your hand is: {player_hand}\n")
        elif card == 3:
            player_hand = 3
            print(f"Your card is a {card}!")
            print(f"Your hand is: {player_hand}\n")
        elif card == 4:
            player_hand = 4
            print(f"Your card is a {card}!")
            print(f"Your hand is: {player_hand}\n")
        elif card == 5:
            player_hand = 5
            print(f"Your card is a {card}!")
            print(f"Your hand is: {player_hand}\n")
        elif card == 6:
            player_hand = 6
            print(f"Your card is a {card}!")
            print(f"Your hand is: {player_hand}\n")
        elif card == 7:
            player_hand = 7
            print(f"Your card is a {card}!")
            print(f"Your hand is: {player_hand}\n")
        elif card == 8:
            player_hand = 8
            print(f"Your card is a {card}!")
            print(f"Your hand is: {player_hand}\n")
        elif card == 9:
            player_hand = 9
            print(f"Your card is a {card}!")
            print(f"Your hand is: {player_hand}\n")
        elif card == 10:
            player_hand = 10
            print(f"Your card is a {card}!")
            print(f"Your hand is: {player_hand}\n")     # need to use a NESTED IF STATEMENT

    elif card == 11:
        player_hand = 10
        print("Your card is a JACK!")
        print(f"Your hand is: {player_hand}")
        print()
    elif card == 12:
        player_hand = 10
        print("Your card is a QUEEN")
        print(f"Your hand is: {player_hand}")
        print()
    elif card == 13:
        player_hand = 10
        print("Your card is a KING!")
        print(f"Your hand is: {player_hand}")
        print()
    #3. add card number to the players hand value
    #4. print hand value
    #5. keep playing the current game by prompting the player to chose menu option
    no_winner = True
    while no_winner:
        # print four menu options
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")
        # ask/prompt player for an input to choose a menu option
        option = int(input("Choose an option: "))
        print()
        if option == 1:
            # deal another card to the player
            card = rng.next_int(13) + 1
            # at RNG need to tell from [ACE JACK QUEEN KING]
            if card == 1:
                print("Your card is a ACE!")
                player_hand = player_hand + card
                print(f"Your hand is: {player_hand}\n")
            elif 2 <= card <= 10:  # need to use a NESTED IF STATEMENT
                if card == 2:
                    print(f"Your card is a {card}!")
                    player_hand = player_hand + card
                    print(f"Your hand is: {player_hand}\n")
                elif card == 3:
                    print(f"Your card is a {card}!")
                    player_hand = player_hand + card
                    print(f"Your hand is: {player_hand}\n")
                elif card == 4:
                    print(f"Your card is a {card}!")
                    player_hand = player_hand + card
                    print(f"Your hand is: {player_hand}\n")
                elif card == 5:
                    print(f"Your card is a {card}!")
                    player_hand = player_hand + card
                    print(f"Your hand is: {player_hand}\n")
                elif card == 6:
                    print(f"Your card is a {card}!")
                    player_hand = player_hand + card
                    print(f"Your hand is: {player_hand}\n")
                elif card == 7:
                    print(f"Your card is a {card}!")
                    player_hand = player_hand + card
                    print(f"Your hand is: {player_hand}\n")
                elif card == 8:
                    print(f"Your card is a {card}!")
                    player_hand = player_hand + card
                    print(f"Your hand is: {player_hand}\n")
                elif card == 9:
                    print(f"Your card is a {card}!")
                    player_hand = player_hand + card
                    print(f"Your hand is: {player_hand}\n")
                elif card == 10:
                    print(f"Your card is a {card}!")
                    player_hand = player_hand + card
                    print(f"Your hand is: {player_hand}\n")  # need to use a NESTED IF STATEMENT

            elif card == 11:
                card_value = 10
                print("Your card is a JACK!")
                player_hand = player_hand + card_value
                print(f"Your hand is: {player_hand}")
                print()
            elif card == 12:
                card_value = 10
                print("Your card is a QUEEN")
                player_hand = player_hand + card_value
                print(f"Your hand is: {player_hand}")
                print()
            elif card == 13:
                card_value = 10
                print("Your card is a KING!")
                player_hand = player_hand + card_value
                print(f"Your hand is: {player_hand}")
                print()
            # calculate the player's hand value
            # DONE in the NESTED IF_Statement!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # if player_hand == 21 , print winning message
            if player_hand == 21:
                print("BLACKJACK! You win!\n")
                num_player_wins += 1
                total_gam_played += 1
                break          # might not be a BREAK
            # elif player_hand > 21, print losing message
            elif player_hand > 21:
                print("You exceeded 21! You lose.\n")
                num_dealer_wins += 1
                total_gam_played += 1
                break          # might not be a BREAK ITS BREAK
            continue
            # update the number of games player/dealer wins    # need to DO THIS
            # set no_winner = False        # or is ir supposed to be continue!!!???
            # Or the above continue goes here at the end after the statistics calculations !!!
        elif option == 2:     # this might have to be part of the nested if statement!!!!
            # deal a card to the dealer
            dealer_hand = rng.next_int(11) + 16  # A random number in range [16,26]
            # compare player hand with dealer hand value
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            print()
            # and determine who wins the game
            if (dealer_hand > player_hand) and (dealer_hand <= 21):             # this won't work bc what if dealer is 22+
                print("Dealer wins!")
                print()
                num_dealer_wins += 1
                total_gam_played += 1
            elif dealer_hand == player_hand:
                print("It's a tie! No one wins!")
                print()
                num_tie_games += 1
                total_gam_played += 1
            elif dealer_hand > 21:
                print("You win!")
                print()
                num_player_wins += 1
                total_gam_played += 1
            elif (dealer_hand < 21) and (player_hand > dealer_hand):        # look again!!!
                print("You win!\n")
                num_player_wins += 1
                total_gam_played += 1
            # update number of games player/dealer wins
            # set no_winner = False
            break
        elif option == 3:
            # print stats: player_wins and dealer_wins. info      # and also the other info.
            print(f"Number of Player wins: {num_player_wins}")
            print(f"Number of Dealer wins: {num_dealer_wins}")
            print(f"Number of tie games: {num_tie_games}")
            print(f"Total # of games played is: {total_gam_played}")
            pers_player_wins = (num_player_wins / total_gam_played) * 100
            print(f"Percentage of Player wins: {pers_player_wins:.1f}%")
            print()
        elif option == 4:
            no_winner = False  # gets out side of the inner while loop
            game_continue = False  # get out of outer while loop
        else:
            # print invalid message
            print("Invalid input!\nPlease enter an integer value between 1 and 4.\n")
            continue
