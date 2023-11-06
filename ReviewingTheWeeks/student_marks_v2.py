def split_lines_by_comma(split_by_line):
    elements_array = []
    for x in split_by_line:
        if x != "" : elements_array.append(x.split(",") )
    return elements_array

def generate_student_list(split_by_comma):
    student_list = []
    name_index = 0
    mark1_index = 1
    mark2_index = 2
    mark3_index = 3
    for line in split_by_comma:
        student_list.append(
            [
                line[name_index],
                int(line[mark1_index]),
                int(line[mark2_index]),
                int(line[mark3_index])
            ]
        )

    return student_list

#Data Structures
def split_data():
    f = open("students.txt", 'r')
    contents = f.read()
    split_by_line = contents.split("\n")
    split_by_comma = split_lines_by_comma(split_by_line)

    """
    there is a much better way of performing the above line -> try and find out how - it may impact 
    the calc_avg() function so be aware of that
    """
    return generate_student_list(split_by_comma)

def calc_avg(student_list):
    for each in student_list:
        sum = each[1] + each[2] + each[3]
        avg = sum / 3
        each.append(int(avg))
    return student_list
def find_low_high(avg_marks):
    low = 100
    high = 0
    for each in avg_marks:
        if each[4] > high:
            high = each[4]
        if each[4] < low:
            low = each[4]
    return low, high
def create_dict(student_list):
    name = []
    avg = []
    for each in student_list:
        name.append(each[0])
        avg.append(each[4])
    dict_list = {name[i]: avg[i] for i in range(len(student_list))}
    for key in dict_list.keys():
        print(key, dict_list[key])

def extract_surname(student_list):
    """
    this method must extract the name from the all_students list
    break the name up so that only the surname remains in a new list call surname_list
    return this list to main()
    :param all_students:
    :return: surname_list
    """
    surname_list = []

    for student in student_list:
        lastname = student[0].split(" ")[-1]
        surname_list.append(lastname)

    return surname_list


def write_to_file(students_avg):
    """
    this method must write the data - including the student average to a file called all_student_data.txt
    pass the relevant parameters into the method
    """
    with open('all_student_data.txt', 'w') as file:
        for student in students_avg:
            joined_student = ", ".join([str(i) for i in student])
            file.write(joined_student)
            file.write("\n")

def main():
    student_list = split_data()
    while True:
        print("\nStudent File Menu:")
        print("1. Split student data into a list")
        print("2. Calculate average")
        print("3. Find min and max")
        print("4. Student with average")
        print("5. Extract surname")
        print("6. Write updated averages to file")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print(student_list)
        elif choice == '2':
            students_avg = calc_avg(student_list)
            print(students_avg)
        elif choice == '3':
            low_high = find_low_high(students_avg)
            print(low_high)
        elif choice == '4':
            create_dict(students_avg)
        elif choice == '5':
            surname_list = extract_surname(student_list)
            print(surname_list)
        elif choice == '6':
            write_to_file(students_avg)
        elif choice == '7':
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()