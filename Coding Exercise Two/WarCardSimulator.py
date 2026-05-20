import random

def compare(card1, card2):
    """
    Standard compare function.
    Returns:
     1 if Player 1 wins
    -1 if Player 2 wins
     0 if it's a tie
    """
    if card1 > card2:
        return 1
    elif card2 > card1:
        return -1
    else:
        return 0

def simulate_war():
    # Global accumulators across all 10 decks
    p1_total_wins = 0
    p2_total_wins = 0
    total_ties = 0
    
    # Run the simulation for a total of 10 decks
    for deck_num in range(10):
        
        # Requirement 1: Two arrays of 26 items with two sets of 1-13
        p1_array = list(range(1, 14)) + list(range(1, 14))
        p2_array = list(range(1, 14)) + list(range(1, 14))
        
        # Requirement 1 (cont.): Shuffle both arrays
        random.shuffle(p1_array)
        random.shuffle(p2_array)
        
        # Loop through the 26 cards in the deck
        for i in range(26):
            # Requirement 2: Draw top card and use standard compare function
            p1_card = p1_array[i]
            p2_card = p2_array[i]
            
            outcome = compare(p1_card, p2_card)
            
            # Requirement 2 & 3: Match syntax used to add to proper accumulator
            match outcome:
                case 1:
                    p1_total_wins += 1
                case -1:
                    p2_total_wins += 1
                case 0:
                    total_ties += 1

    # Calculation for statistics
    total_rounds = 10 * 26  # 10 decks * 26 cards = 260 total rounds
    p1_win_percentage = (p1_total_wins / total_rounds) * 100
    p2_win_percentage = (p2_total_wins / total_rounds) * 100

    # Requirement 5: Output Statistics
    print("=== WAR CARD GAME SIMULATION STATISTICS ===")
    print(f"Total Decks Played:   10 (Total Rounds: {total_rounds})")
    print(f"Player 1 Total Wins:  {p1_total_wins}")
    print(f"Player 2 Total Wins:  {p2_total_wins}")
    print(f"Total Ties:           {total_ties}")
    print(f"Player 1 Win Rate:    {p1_win_percentage:.2f}%")
    print(f"Player 2 Win Rate:    {p2_win_percentage:.2f}%")

if __name__ == "__main__":
    simulate_war()