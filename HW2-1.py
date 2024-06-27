try:

    with open ('input.txt', 'r') as grade_list:
        line = grade_list.readlines()
        students = []
        for i in line:
            lines = i.split(',')
            students.append([lines[0].strip(), int(lines[1].strip())])
            flag = True


except FileNotFoundError:
    print('Файл отсутствует')
    flag = False


if flag:
    average = 0
    for i in students:
        average += i[1]
    ave = average / len(students)

    with open('output.txt', 'w') as name_list:
        for i in students:
            if i[1] >= ave:
                name_list.write(f"{i[0]} - {i[1]}\n")
