def even_number_generator():
    """a generator function that yields
    even numbers indefinitely"""
    # Start with the first even number
    number = 0
    while True:
        yield number  # Yield the current even number
        number += 2  # Increment the number by 2 to get next even number


gen = even_number_generator()

for _ in range(10):
    print(next(gen))  # Print the next even number
