def fibonacci():
    a = 0
    b = 1

    print("First 15 terms of Fibonacci series:")

    for i in range(15):
        print(a, end=" ")
        a, b = b, a + b


# Function call
fibonacci()
