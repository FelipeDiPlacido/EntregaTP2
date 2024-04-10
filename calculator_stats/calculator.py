def generate_statistics(names, goals, goals_avoided, assists):
    """
    This function processes the statistics and enters them into a list of dictionaries

    Args:
        names: String with the name of each player.
        goals: List with the goals of each player.
        goals_avoided: List with the goals avoided by each player.
        assists: List with the assists of each player.
        
    Return
        A list of dictionaries with the statistics of each player
    """
    
    names_list = names.split(", ")
    player_stats = list(map(lambda name, goal, goal_avoided, assist: 
        {"name": name, "goals": goal, "goals_avoided": goal_avoided, "asissts": assist},
        names_list, goals, goals_avoided, assists))
    
    return player_stats
