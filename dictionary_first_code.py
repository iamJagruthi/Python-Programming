# Dictionary with test data
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Function to calculate the mean of dictionary values
def calculate_mean(dictionary):
    total = sum(dictionary.values())
    count = len(dictionary)
    mean = total / count
    return mean

# Example
mean_value = calculate_mean(test_dict)
print("The mean of the dictionary values is:", mean_value)
