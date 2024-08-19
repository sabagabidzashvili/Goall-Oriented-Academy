def activate_slashing(numbers, indexes):
    """
    Displays only the numbers at the specified indexes from the given list.
    
    :param numbers: List of numbers.
    :param indexes: List of indexes to extract.
    :return: List of numbers at the specified indexes.
    """
    try:
        result = [numbers[i] for i in indexes if 0 <= i < len(numbers)]
        return result
    except IndexError as e:
        print(f"Error: {e}")
        return []

# Example usage
numbers = [10, 20, 30, 40, 50]
indexes = [1, 3]  # We want to display the numbers at index 1 and 3

result = activate_slashing(numbers, indexes)
print("Numbers at specified indexes:", result)
