def fibonacci(n):
    if n <= 0:
        print("Invalid input. Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence:")
        print(0)
    else:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])

        print("Fibonacci sequence:")
        for num in sequence:
            print(num)

# Get user input
n = int(input("Enter the number of terms for the Fibonacci sequence: ").strip())

# Generate and display the Fibonacci sequence
fibonacci(n)
