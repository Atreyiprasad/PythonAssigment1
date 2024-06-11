def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage
numbers = [1, 2, 3, 4, 1, 2, 1]
element = 1
print(f"The element {element} occurs {count_occurrences(numbers, element)} times in the list.")
