input_dict = {1: 10, 2:20, 3: None, 4: 40, 5: None, 6: 60}

filtered_dict= {key: value for key, value in input_dict.items() if value is not None}

print("Dictionary with empty items dropped:")
print(f"({', '.join(f'{key}: {value}' for key, value in filtered_dict.items())})")
