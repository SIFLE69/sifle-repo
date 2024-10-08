def fibonacci(n):
  
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


num_terms = 10  
fib_sequence = fibonacci(num_terms)
print(f"Fibonacci sequence with {num_terms} terms: {fib_sequence}")
