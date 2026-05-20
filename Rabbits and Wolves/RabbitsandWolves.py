def simulate_island():
    # Initial Constants
    rabbits = 50.0
    wolves = 0.0
    
    r_growth = 0.10      # 10%
    w_growth = 0.08      # 8%
    predation = 0.01     # 1% per wolf
    w_death = 0.06       # 6%
    
    print(f"{'Year':<10} {'Rabbits':<15} {'Wolves':<15}")
    print("-" * 40)

    for year in range(1, 21):
        # Introduction of wolves in Year 5
        if year == 5:
            wolves = 10.0
            
        if year >= 5:
            # Rabbits: Growth - (Predation * number of wolves)
            # Note: Predation is often calculated as a rate per encounter
            rabbits_eaten = rabbits * (predation * wolves)
            rabbits = rabbits + (rabbits * r_growth) - rabbits_eaten
            
            # Wolves: Growth - Natural Death
            wolves = wolves + (wolves * w_growth) - (wolves * w_death)
        else:
            # Rabbit only growth
            rabbits = rabbits + (rabbits * r_growth)
            
        # Keep numbers realistic (no negative animals)
        rabbits = max(0, rabbits)
        wolves = max(0, wolves)

        print(f"{year:<10} {round(rabbits):<15} {round(wolves):<15}")

if __name__ == "__main__":
    simulate_island()
    