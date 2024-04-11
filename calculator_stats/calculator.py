def generate_statistics(names, goals, goals_avoided, assists):
    """
    This function processes the statistics and enters them into a list of dictionaries.

    Args:
        names: String with the name of each player.
        goals: List with the goals of each player.
        goals_avoided: List with the goals avoided by each player.
        assists: List with the assists of each player.
        
    Return
        A list of dictionaries with the statistics of each player.
    """
    
    names_list = names.split(", ")
    players_stats = list(map(lambda name, goal, goal_avoided, assist: 
        {"name": name, "goals": goal, "goals_avoided": goal_avoided, "assists": assist},
        names_list, goals, goals_avoided, assists))
    
    return players_stats

def top_scorer (players_stats):
    """
    This function finds the player with the most goals and returns his name and number of goals.

    Args:
        players_stats: List of dictionaries with the statistics of each player.
    
    Return:
        Tuple with the name and goals of the scorer.
    """
    scorer = max (players_stats, key= lambda x: x["goals"])
    return scorer["name"], scorer["goals"]


def most_influential_player (players_stats):
    """
    This function searches for the most influential player by calculating the weighted average.

    Args:
        players_stats: List of dictionaries with the statistics of each player.
    
    Return:
        A string with the name of the most influential player.
    """
    most_influential = max(players_stats, key=lambda x: (x["goals"] * 1.5 + x["goals_avoided"] * 1.25 + x["assists"]) / 3 )
    return most_influential["name"]
