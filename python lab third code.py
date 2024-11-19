# Function to find duplicate values in a list
def find_duplicates(lst):
    duplicates = []
    seen = set()

    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)

    return duplicates

# Example 
my_list = [1, 2, 3, 4, 2, 2, 5, 6, 3, 7, 1]
duplicates = find_duplicates(my_list)
print("Duplicate values in the list are:", duplicates)
