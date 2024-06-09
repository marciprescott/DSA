import time  # Import the time module to measure execution time


def execution_time_logger(func):
    """
    Decorator that logs the execution time of the decorated function.
    """

    def wrapper(*args, **kwargs):
        """
        Wrapper function that adds the timing functionality.
        """
        # Record the start time
        start_time = time.time()

        # Call the original function with its arguments and store the result
        result = func(*args, **kwargs)

        # Record the end time
        end_time = time.time()

        # Calculate the execution time
        execution_time = end_time - start_time

        # Log the execution time with the function's name
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")

        # Return the original function's result
        return result

    # Return the wrapper function
    return wrapper


# Example usage of the decorator
@execution_time_logger
def example_function(x, y, delay=1):
    """
    Example function that takes some time to execute.
    """
    time.sleep(delay)  # Simulate a delay
    return x + y  # Return the sum of x and y


# Call the decorated function
result = example_function(5, 3, delay=2)
print(f"Result: {result}")
