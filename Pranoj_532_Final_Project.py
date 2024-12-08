import numpy as np
import timeit

def basic_loop_sum(arr):
    """
    Sum the elements of an array using a basic loop.
    """
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

def unrolled_loop_sum(arr, step=4):
    """
    Sum the elements of an array using loop unrolling.
    
    Parameters:
    - arr: The array to sum.
    - step: The unrolling factor (default is 4).
    """
    total = 0
    length = len(arr)
    remainder = length % step

    # Process chunks of size 'step'
    for i in range(0, length - remainder, step):
        for j in range(step):  # Manual unrolling
            total += arr[i + j]

    # Handle the remaining elements
    for i in range(length - remainder, length):
        total += arr[i]

    return total

def vectorized_sum(arr):
    """
    Sum the elements of an array using NumPy's vectorized operations.
    """
    return np.sum(arr)

def measure_performance(func, arr, *args, num_runs=5):
    """
    Measure the performance of a given function using timeit.
    
    Parameters:
    - func: The function to test.
    - arr: The array to pass to the function.
    - args: Additional arguments for the function.
    - num_runs: Number of repetitions for timing (default is 5).
    
    Returns:
    - Average execution time in seconds.
    """
    timer = timeit.Timer(lambda: func(arr, *args))
    total_time = timer.timeit(number=num_runs)
    return total_time / num_runs

if __name__ == "__main__":
    # Create a large array of random integers
    size = 10_000_000
    arr = np.random.randint(1, 100, size=size)

    # Performance measurements
    basic_time = measure_performance(basic_loop_sum, arr)
    unrolled_time_4 = measure_performance(unrolled_loop_sum, arr, 4)
    unrolled_time_8 = measure_performance(unrolled_loop_sum, arr, 8)
    vectorized_time = measure_performance(vectorized_sum, arr)

    # Results display
    print(f"Basic Loop: Average Time: {basic_time:.6f} seconds")
    print(f"Unrolled Loop (Factor 4): Average Time: {unrolled_time_4:.6f} seconds")
    print(f"Unrolled Loop (Factor 8): Average Time: {unrolled_time_8:.6f} seconds")
    print(f"Vectorized (NumPy): Average Time: {vectorized_time:.6f} seconds")

    # Calculate performance improvement
    improvement_4 = (basic_time - unrolled_time_4) / basic_time * 100
    improvement_8 = (basic_time - unrolled_time_8) / basic_time * 100
    improvement_vec = (basic_time - vectorized_time) / basic_time * 100

    print("\nPerformance Improvement:")
    print(f"  Unrolled (Factor 4): {improvement_4:.2f}%")
    print(f"  Unrolled (Factor 8): {improvement_8:.2f}%")
    print(f"  Vectorized (NumPy): {improvement_vec:.2f}%")
