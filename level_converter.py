# Convert BDO level format to float
def level_to_float(level_name, level_nr, percentage):

    names = ["Begginer", "Apprentice", "Skilled", "Professional", "Artisan", "Master", "Guru"]
    added_levels = [0, 10, 20, 30, 40, 70, 120]
    levels_dict = dict(zip(names, added_levels))
    
    return levels_dict[level_name] + float(level_nr) + float(percentage[:-1])/100

# Convert float to BDO level format. Each stage has a number of levels included in it. The remainder is left as a number. 
# i.e. Guru starts from 80, so level 87 = Guru 7. Numbers after floating point turn into percentages.
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