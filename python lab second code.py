# Function to find the largest and smallest numbers in a list
def find_largest_smallest(lst):
    largest = lst[0]
    smallest = lst[0]

    
    for num in lst[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example
my_list = [23, 1, 34, -5, 12, 9]
largest, smallest = find_largest_smallest(my_list)

print("Largest number is:", largest)
print("Smallest number is:", smallest)
