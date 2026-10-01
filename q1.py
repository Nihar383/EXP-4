def find_second_largest_smallest(numbers):
    # Initialize largest and smallest
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for num in numbers:
        # Find largest and second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

        # Find smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_largest, second_smallest


# Input 10 integers
numbers = []

print("Enter 10 integers:")
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

# Function call
second_largest, second_smallest = find_second_largest_smallest(numbers)

print("\nList:", numbers)
print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)
