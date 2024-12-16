def sum_of_even_numbers(numbers):
    """Calculate the sum of all even numbers in the list using list comprehension."""
    return sum([num for num in numbers if num % 2 == 0])


def main():
    # Example list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Call the function and print the result
    result = sum_of_even_numbers(numbers)
    print(f"Sum of even numbers: {result}")


# NOTE: Donot Change anything below this line.
# Test cases
def test_sum_of_even_numbers():
    print("Running tests for sum_of_even_numbers...")
    # Test case 1: Standard case
    assert sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30, "Test case 1 failed"
    
    # Test case 2: All even numbers
    assert sum_of_even_numbers([2, 4, 6, 8]) == 20, "Test case 2 failed"
    
    # Test case 3: All odd numbers
    assert sum_of_even_numbers([1, 3, 5, 7]) == 0, "Test case 3 failed"
    
    # Test case 4: Mixed numbers with negatives
    assert sum_of_even_numbers([-2, -4, -6, 1, 3, 5]) == -12, "Test case 4 failed"
    
    # Test case 5: Empty list
    assert sum_of_even_numbers([]) == 0, "Test case 5 failed"
    
    # Test case 6: Single even number
    assert sum_of_even_numbers([10]) == 10, "Test case 6 failed"
    
    # Test case 7: Single odd number
    assert sum_of_even_numbers([7]) == 0, "Test case 7 failed"
    
    print("All tests passed!")

if __name__ == "__main__":
    main()
    test_sum_of_even_numbers()
