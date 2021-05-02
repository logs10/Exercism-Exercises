def tabulate(matches):
    """
    Take in a list of match results and return a organized dictionary of unique
    teams containing relevant match history statistics. This dictionary will be used in final
    data output.
    """
    scores = {'win': 3,
              'loss': 0,
              'draw': 1}
    summary = [x.split(';')[0:3] for x in matches]
    teams = [x[0:2] for x in summary]
    unique_teams = set([x for y in teams for x in y])
    team_dict = {key: {'win': 0, 'loss': 0, 'draw': 0, 'matches': 0, 'points': 0}
                 for key in unique_teams}
    # Loop through each match played and update team outcomes in the team dictionary.
    for match in summary:
        team1, team2 = match[0], match[1]
        if match[2] == 'draw':
            team_dict[team1]['draw'] = team_dict[team1]['draw'] + 1
            team_dict[team2]['draw'] = team_dict[team2]['draw'] + 1
        elif match[2] == 'win':
            team_dict[team1]['win'] += 1
            team_dict[team2]['loss'] += 1
        elif match[2] == 'loss':
            team_dict[team1]['loss'] += 1
            team_dict[team2]['win'] += 1
    # Once all matches results have been assigned to respective teams, compute count total matches
    # and assign points based on given score parameters.
    for entry in team_dict.items():
        match_count, points = [], []
        for vals in entry[1]:
            if vals in ['win', 'loss', 'draw']:
                match_count.append(entry[1][vals])
                points.append(entry[1][vals] * scores[vals])
        team_dict[entry[0]]['matches'] = sum(match_count)
        team_dict[entry[0]]['points'] = sum(points)
    return team_dict


def tally(rows):
    """
    Given a computed team dictionary, return a summarized table of match results
    """
    ledger = tabulate(rows)
    # Sort first by points desc and then by team name
    sorted_ledger = dict(sorted(
        ledger.items(), key=lambda item: (-item[1]['points'], item[0])))
    header = "Team                           | MP |  W |  D |  L |  P"
    finish = [header]
    for team in sorted_ledger:
        finish.append(team + " " * (30 - len(team)) + " |  " + str(sorted_ledger[team]['matches']) + " |  " + str(sorted_ledger[team]['win']) + " |  " +
                      str(sorted_ledger[team]['draw']) + " |  " + str(sorted_ledger[team]['loss']) + " |  " + str(sorted_ledger[team]['points']))
    return finish
