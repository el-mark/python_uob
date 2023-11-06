def find_max(values):
    max_value = 0
    for value in values:
        if value > max_value:
            max_value = value
    return max_value

assert find_max([1, 2, 6, 4, 5]) == 6, 'The returned number is not the max number'