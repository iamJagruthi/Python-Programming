# Function to traverse a list in reverse order and print elements with their original index
def traverse_reverse(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(f"{lst[i]} (original index: {i})")

# Example 
my_list = ['red', 'green', 'white', 'black']
print("Traverse the list in reverse order:")
traverse_reverse(my_list)
