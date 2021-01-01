import random
import json
import string

import constants

def add_zeros(n):
    if n < 10:
        return "0" + str(n)
    else: 
        return str(n)

def get_random_date():
    random_date = str(random.randint(1,12)) + "/" + str(random.randint(1,30)) + "/" + str(random.randint(2018, 2021)) + ", " + add_zeros(random.randint(1,13)) + ":" + str(random.randint(0,60)) + ":" + str(random.randint(0,60))
    return random_date

def generate_random_entry_tuple():
    rank_dict = {}
    for profession in constants.PROFESSIONS:
        rank_dict[profession] = random.randint(10000, 1700000)/10000
    lifeskill_json = json.dumps(rank_dict)
    user_id = random.randint(2, 100)
    nick = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    random_date = get_random_date()
    entry_tuple = (user_id, 1, nick, lifeskill_json, random_date)
    return entry_tuple




