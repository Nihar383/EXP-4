def get_even_values(numbers):
    even_list = []

    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)

    return even_list


# Create a list
numbers = [10, 15, 22, 33, 40, 51, 64, 75, 80, 91]

print("Original List:")
print(numbers)

# Function call
result = get_even_values(numbers)

print("\nNew List with Even Values:")
print(result)
