main_list = ["Ahí voy", 1, 2, 3]
swap_list = []

for element in main_list:
    swap_list.insert(0, element)

print(" ".join(str(item) for item in swap_list))
