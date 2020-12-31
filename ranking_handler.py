def rank_user(current_level_dict, level_dicts):
    for key in current_level_dict.keys():
        current_rank = 1
        for level_dict in level_dicts:
            if level_dict[key] > current_level_dict[key]:
                current_rank += 1
