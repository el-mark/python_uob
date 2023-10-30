def find_mean(list_argument):
    if len(list_argument) == 0:
        return 0
    else:
        total_sum = sum(list_argument)
        return total_sum / len(list_argument)

def find_media(list_argument):
    if len(list_argument) == 0:
        return 0
    else:
        list_argument.sort()
        midpoint = len(list_argument) // 2
        if len(list_argument) % 2 == 1:
            return list_argument[midpoint]
        else:
            return (list_argument[midpoint - 1] + list_argument[midpoint])/2

# def find_mode(list_argument):

def main(example_list):
    print(f"The mean is: {find_mean(example_list)}")
    print(f"The media is: {find_media(example_list)}")

example_list = [1, 7, 5, 8, 2, 3, 10, 3]
# example_list = []
main(example_list)
