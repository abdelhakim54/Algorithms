import pytest
import time
import tracemalloc
import os
import matplotlib.pyplot as plt
import pandas as pd
from memory_profiler import memory_usage
from PIL import Image
from Daily_Coding_Interviews.day_001 import brute_force_check_sum, two_pass_check_sum, one_pass_check_sum

# ✅ List of functions to test
functions = [brute_force_check_sum, two_pass_check_sum, one_pass_check_sum]

# ✅ Create Report Directory
REPORT_DIR = "report/day_001"
os.makedirs(REPORT_DIR, exist_ok=True)

# ✅ Functional Test Cases
@pytest.mark.parametrize("func", functions)
@pytest.mark.parametrize("nums, k, expected", [
    ([10, 15, 3, 7], 17, True),
    ([1, 2, 3, 4, 5], 9, True),
    ([1, 2, 3, 4, 5], 10, False),
    ([5, -2, 7, 10], 8, True),
    ([1, 1, 1, 1], 2, True),
    ([1, 2, 3], 6, False),
    ([], 5, False),
    ([5], 5, False),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19, True),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20, False),
])
def test_has_pair_with_sum(func, nums, k, expected):
    """Tests correctness of multiple implementations."""
    assert func(nums, k) == expected


# ✅ Performance Testing (Execution Time & Memory Usage)
def measure_performance(func, nums, k):
    """Measures execution time & memory usage of a function."""
    tracemalloc.start()  # Start memory tracking
    start_mem = memory_usage(-1, interval=0.01, timeout=1)

    start_time = time.perf_counter()
    func(nums, k)  # Run function
    end_time = time.perf_counter()

    end_mem = memory_usage(-1, interval=0.01, timeout=1)
    tracemalloc.stop()

    exec_time = end_time - start_time
    memory_used = max(end_mem) - min(start_mem)

    return exec_time, memory_used


def test_performance():
    """Runs performance tests on large inputs and saves results in `report/day_001/`."""
    big_input = list(range(10**4))  # Large dataset
    k = 1999999  # Large sum to check

    results = []

    for func in functions:
        exec_time, memory_used = measure_performance(func, big_input, k)
        results.append((func.__name__, exec_time, memory_used))

    # Convert results to DataFrame
    df = pd.DataFrame(results, columns=["Function", "Execution Time (s)", "Memory Used (MB)"])

    # Print Table Summary
    print("\nPerformance Summary:")
    print(df.to_string(index=False))

    # ✅ Generate & Save Performance Graphs in `report/day_001/`
    plt.figure(figsize=(10, 5))
    plt.bar(df["Function"], df["Execution Time (s)"], color='blue', label="Execution Time (s)")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time of Different Implementations")
    plt.legend()
    plt.savefig(f"{REPORT_DIR}/execution_time.png")

    plt.figure(figsize=(10, 5))
    plt.bar(df["Function"], df["Memory Used (MB)"], color='red', label="Memory Used (MB)")
    plt.ylabel("Memory Used (MB)")
    plt.title("Memory Usage of Different Implementations")
    plt.legend()
    plt.savefig(f"{REPORT_DIR}/memory_usage.png")

    # ✅ Combine Images into One (Optional)
    img1 = Image.open(f"{REPORT_DIR}/execution_time.png")
    img2 = Image.open(f"{REPORT_DIR}/memory_usage.png")

    new_img = Image.new("RGB", (img1.width, img1.height + img2.height))
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (0, img1.height))

    new_img.save(f"{REPORT_DIR}/performance_results.png")

    print(f"\nPerformance results saved in '{REPORT_DIR}/' 📊")
