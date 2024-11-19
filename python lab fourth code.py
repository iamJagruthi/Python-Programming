# Function to split a list into two parts
def split_list(lst, length_of_first_part):
    first_part = lst[:length_of_first_part]
    second_part = lst[length_of_first_part:]
    return first_part, second_part

# Example
my_list = [1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 1]
length_of_first_part = 3
split_parts = split_list(my_list, length_of_first_part)
print("Splitted the list into two parts:", split_parts)
