def simulate_island():
    rabbits = 50
    wolves = 0
    
    # Constants
    R_GROWTH_RATE = 0.10      # 10%
    W_GROWTH_RATE = 0.08      # 8%
    PREDATION_RATE = 0.01     # 1% per wolf
    W_DEATH_RATE = 0.06       # 6%

    for year in range(1, 21):
        # 1. Calculate Rabbit Growth first
        rabbits = rabbits + (rabbits * R_GROWTH_RATE)
        
        # 2. Handle Wolf Introduction / Growth
        if year == 5:
            wolves = 10
        elif year > 5:
            wolves = wolves + (wolves * W_GROWTH_RATE)
            
        # 3. Apply Decreases (Predation and Wolf Deaths)
        # Rabbits lose 1% for every wolf present
        rabbits = rabbits - (rabbits * (wolves * PREDATION_RATE))
        
        if year >= 5:
            wolves = wolves - (wolves * W_DEATH_RATE)
            
        # 4. Truncate decimals to match exact example output
        rabbits = int(rabbits)
        wolves = int(wolves)

        print(f"Year {year}: Rabbits - {rabbits}, Wolves - {wolves}")

if __name__ == "__main__":
    simulate_island()