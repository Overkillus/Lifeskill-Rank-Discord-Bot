import random 
import json
import string

import constants

def rank_user(entry_tuples, current_entry):
    # Format of tuple: (id, server_id, nick, lisfeskill_json, datetime)
    # Save nick of the user who calls the command
    current_nick = current_entry[2]
    # Unpack lifeskill json to a dictionary of pairs: (profession name, level)
    current_level_dict = json.loads(current_entry[3])
    # Initialise dict to store rank for each profession: (profession name, rank). Initial value is 1 for all professions
    rank_dict = {}
    user_number_dict = {}
    for profession in constants.PROFESSIONS:
        rank_dict[profession] = 1
        user_number = 1
        # Unpack lifeskill json and extract nick for each entry
    for entry in entry_tuples:
        level_dict = json.loads(entry[3])
        nick = entry[2]
        # Omit own entries
        if nick != current_nick:
            # Increment population
            user_number += 1
            # Iterate over each profession
            for key in current_level_dict.keys():
                # If somebody has larger level, add 1 to rank (drop rank)
                if level_dict[key] > current_level_dict[key]:
                    rank_dict[key] += 1
    # Conver floats to percentages
    for profession, value in rank_dict.items():
        if profession != "Barter":
            print(rank_dict[profession])
            print(user_number)
        level = str(round(rank_dict[profession] / user_number * 100, 2)) + "%"
        rank_dict[profession] = level
    return rank_dict

def top_10(entry_tuples, chosen_professions):
    # Initialise dictionary of form:
    # Key: profession
    # Value: list of empty list of pairs: [nick, level]
    top_entries = [[["", 0] for i in range(10)] for j in range(len(chosen_professions))]
    top_dict = dict(zip(chosen_professions, top_entries))
    # Load database data from entry_tuples list
    for entry in entry_tuples:
        nick = entry[2]
        level_dict = json.loads(entry[3])
        for profession in chosen_professions:
            # append to top list
            top_dict[profession].append([nick, level_dict[profession]])
            # sort by 2nd item in lists (level), descending order
            top_dict[profession].sort(key=lambda x: -x[1])
            # reject smallest level entry
            top_dict[profession].pop(10)
    return top_dict





    




