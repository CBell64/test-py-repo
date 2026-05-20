import random

def compare(val1, val2):
    """Standard compare function: returns 1 if val1 > val2, -1 if val2 > val1, 0 if tie."""
    if val1 > val2:
        return 1
    elif val2 > val1:
        return -1
    else:
        return 0

def simulate_war():
    player1_total_wins = 0
    player2_total_wins = 0
    total_ties = 0
    total_rounds = 0
    
    # Run the simulation for 10 decks
    for deck_num in range(1, 11):
        # Initialize arrays with two sets of 1-13 (26 cards total)
        p1_cards = list(range(1, 14)) * 2
        p2_cards = list(range(1, 14)) * 2
        
        # Shuffle the arrays
        random.shuffle(p1_cards)
        random.shuffle(p2_cards)
        
        # Play through the 26 cards in the current deck
        for i in range(26):
            result = compare(p1_cards[i], p2_cards[i])
            total_rounds += 1
            
            # Using match syntax for the outcome
            match result:
                case 1:
                    player1_total_wins += 1
                case -1:
                    player2_total_wins += 1
                case 0:
                    total_ties += 1

    # Calculate statistics
    p1_win_pct = (player1_total_wins / total_rounds) * 100
    p2_win_pct = (player2_total_wins / total_rounds) * 100

    # Output Results
    print(f"--- Simulation Results (10 Decks) ---")
    print(f"Total Rounds Played: {total_rounds}")
    print(f"Player 1 Total Wins: {player1_total_wins}")
    print(f"Player 2 Total Wins: {player2_total_wins}")
    print(f"Total Ties:          {total_ties}")
    print(f"Player 1 Win %:      {p1_win_pct:.2f}%")
    print(f"Player 2 Win %:      {p2_win_pct:.2f}%")

if __name__ == "__main__":
    simulate_war()