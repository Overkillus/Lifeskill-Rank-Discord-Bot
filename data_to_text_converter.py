from level_converter import float_to_level

# Convert all level data of 1 user to easily readable format
def simple_format(parsed_data):
    formatted_text = ""
    for key, value in parsed_data:
        formatted_text += key + " "
        formatted_text += float_to_level(value) + "\n"
    return formatted_text

def get_rank_message(rank_dict):
    msg = ""
    for key, value in rank_dict.items():
        msg += key + ": " + value + "\n"
    return msg


