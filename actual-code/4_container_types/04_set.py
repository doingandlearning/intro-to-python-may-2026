empty_set = set()
print(empty_set)
print(type(empty_set))

countries_in_the_room = {"England", "England", "Northern Ireland", "Spain"}
print(countries_in_the_room)
print(type(countries_in_the_room))

countries_in_the_uk = {"England", "Scotland", "Wales", "Northern Ireland"}

print(countries_in_the_uk.difference(countries_in_the_room))
print(countries_in_the_uk.intersection(countries_in_the_room))

list_of_items = ["bananas", "bananas", "pasta", "lettuce", "pizza", "pizza"]
print(list(set(list_of_items))) # deduplicate list
