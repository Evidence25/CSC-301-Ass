def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Generate first 8 Fibonacci numbers
result = fibonacci_series(8)
print("Fibonacci series of 8 terms:", result)
