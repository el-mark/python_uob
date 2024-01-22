def days_difference(day1, day2):
    """
    (int, int) -> int
    
    Return the number of days between day1 and day2, which are
    both in the range 1-365 (thus indicating the day of the year).

    >>> days_difference(200, 224)
    24
    >>> days_difference(50, 50)
    0
    >>> days_difference(100, 99)
    -1
    """
    return day2 - day1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
