# Rion Shionyu
# Level 10 Assignment of College Football Results

import pandas as pd
# Read the college football CSV file
football_data = pd.read_csv("cfb.csv")

# Ask the user which season to analyze
season = input("Enter a season to analyze: ").strip()

# Find the teams for the selected season
season_data = football_data[football_data["Season"].astype(str) == season]

# Check if the season exists
if season_data.empty:
    print("Sorry, that season was not found.")

else:
    teams = {"10 or more wins": [], "8-9 wins": [], "6-7 wins": [], "Fewer than 6 wins": []}
    for index, row in season_data.iterrows():
        team_name = row["Team"]
        wins = row["Win"]
        
        if wins >= 10:
            teams["10 or more wins"].append(team_name)
        elif wins >= 8:
            teams["8-9 wins"].append(team_name)
        elif wins >= 6:
            teams["6-7 wins"].append(team_name)
        else:
            teams["Fewer than 6 wins"].append(team_name)

    # Display the results for the selected season
    print()
    print("College Football Results for", season)

    # Print the teams in each category
    for category, team_list in teams.items():
        print()
        print(category + ":")

        for team in team_list:
            print(team)
