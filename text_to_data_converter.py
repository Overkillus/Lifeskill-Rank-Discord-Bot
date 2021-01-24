import json
from level_converter import level_to_float

# Main function converting raw text from image recognition API to a dictionary
# Format: dictionary of pairs (skill_name, level) in form (string, float)
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
        parsed_data[lifeskill] = level_to_float(level_name, level_nr, percentage)
    return parsed_data