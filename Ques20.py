#Write a python program that takes a list of numbers and returns their sum.
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


numbers = [1, 2, 3, 4, 5]
sum_of_numbers = calculate_sum(numbers)
print("The sum of the numbers is:", sum_of_numbers)
