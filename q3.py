def increase_odd_elements(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            numbers[i] = numbers[i] + 5
    return numbers


# Create an integer list of 20 elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Original List:")
print(numbers)

# Function call
result = increase_odd_elements(numbers)

print("\nList after increasing odd elements by 5:")
print(result)
