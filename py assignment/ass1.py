def recursive_sum(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    else:
        return n + recursive_sum(n - 1)

# Sum of first 10 numbers
result = recursive_sum(10)
print("Sum of first 10 numbers is:", result)
