import json

def parse(text):
    raw_data = text.splitlines()
    parsed_data = {}
    dict_len = 3

    # loop over all data in intervals of 3
    for i in range(0, len(raw_data), dict_len):
        # loop over single lifeskill data - 3 lines
        for j in range(dict_len):
            current_data = raw_data[i+j].strip()
            if "%" in current_data:
                percentage = current_data
            elif len(current_data.split()) == 2 and current_data.split()[1].isdecimal():
                level_name = current_data.split()[0]
                level_nr = current_data.split()[1]
            else:
                lifeskill = current_data.split()[-1]
                lifeskill = ''.join([c for c in lifeskill if c.isalpha()])
        parsed_data[lifeskill] = levels_to_float(level_name, level_nr, percentage)
    return parsed_data

def levels_to_float(level_name, level_nr, percentage):

    names = ["Begginer", "Apprentice", "Skilled", "Professional", "Artisan", "Master", "Guru"]
    added_levels = [0, 10, 20, 30, 40, 70, 120]
    levels_dict = dict(zip(names, added_levels))
    
    return levels_dict[level_name] + float(level_nr) + float(percentage[:-1])/100

def float_to_level(level_float):
    names = ["Begginer", "Apprentice", "Skilled", "Professional", "Artisan", "Master", "Guru"]
    added_levels = [0, 10, 20, 30, 40, 50, 80]
    levels_dict = dict(zip(added_levels, names))

    level_string = ""

    added_levels.reverse()
    for level in added_levels:
        if level_float > level:
            level_string += levels_dict[level]
            level_string += " " + str(int(level_float - level))
            level_string += " " + str( round(level_float - int(level_float), 4) * 100) + "%"
            return level_string

def simple_format(parsed_data):
    formatted_text = ""
    for key, value in parsed_data:
        formatted_text += key + " "
        formatted_text += float_to_level(value) + "\n"
    return formatted_text