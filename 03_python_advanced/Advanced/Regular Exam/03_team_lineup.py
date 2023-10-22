def team_lineup(*args):
    teams_dict = {}
    result = []

    for player_name, player_country in args:
        if player_country not in teams_dict:
            teams_dict[player_country] = []
        if player_name not in teams_dict[player_country]:
            teams_dict[player_country].append(player_name)

    sorted_lineups = sorted(teams_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for country, players in sorted_lineups:
        result.append(f'{country}:')
        for player in players:
            result.append(f'  -{player}')

    return '\n'.join(result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print()

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print()

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

