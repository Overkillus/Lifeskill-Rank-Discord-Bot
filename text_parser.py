def parse(text):
    raw_data = text.splitlines()
    parsed_data = []

    # if "Mastery" in text:
    #     dict_len = 4
    # else:
    #     dict_len = 3

    dict_len = 3

    # loop over all data in intervals of 3
    for i in range(0, len(raw_data), dict_len):
        lifeskill_data = {}
        # loop over single lifeskill data - 3 lines
        for j in range(dict_len):
            current_data = raw_data[i+j].strip()
            if "%" in current_data:
                lifeskill_data["percentage"] =  current_data
            # elif "Mastery" in current_data:
            #     lifeskill_data["mastery"] =  current_data
            elif len(current_data.split()) == 2 and current_data.split()[1].isdecimal():
            # elif " " in current_data: # Level info is of format "[name] [number]"
                lifeskill_data["level"] =  current_data
            else:
                lifeskill_data["lifeskill"] =  current_data.split()[-1]
        parsed_data.append(lifeskill_data)
    # print(parsed_data)
    return parsed_data

def simple_format(parsed_data):
    formatted_text = ""
    for i in range(len(parsed_data)):
        current = parsed_data[i]
        formatted_text += current.get("lifeskill") +" "
        if current.get("mastery"):
                    formatted_text += current.get("mastery") +" "
        formatted_text += current.get("level") +" "+ current.get("percentage") + "\n"
    return formatted_text
    

#text="Mastery 1 \n 34.54% \n Artisan 2 \n Fishing"
#parse(text)
