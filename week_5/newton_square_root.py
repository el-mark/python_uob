def newton():
    has_big_difference = True
    x = float(input("Enter a positive number: "))
    z = 1
    tolerance = 0.0000001

    while has_big_difference:
        z = (z + x / z) / 2
        print(z)
        difference = abs(x - z * z)
        if difference < tolerance:
            has_big_difference = False

newton()
