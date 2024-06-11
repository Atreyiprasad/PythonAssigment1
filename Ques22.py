def find_min_max(lst):
    min_value = min(lst)
    max_value = max(lst)
    return min_value, max_value


numbers = [3, 7, 2, 9, 1, 6]
min_value, max_value = find_min_max(numbers)
print(f"The minimum value is {min_value} and the maximum value is {max_value}.")
