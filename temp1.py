from ranking_handler import *
from test_handler import *
entries = [generate_random_entry_tuple() for i in range(50)]
my_entry = generate_random_entry_tuple()
print("My entry: " + str(my_entry))
# print(top_10(entries, ["Fishing", "Cooking"]))

print(rank_user(entries, my_entry))