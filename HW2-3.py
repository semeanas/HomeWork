try:
    with open('input1.txt', 'r') as file1_list:
        line1 = file1_list.readlines()
    
    with open ('input2.txt', 'r') as file2_list:
        line2 = file2_list.readlines()
except FileNotFoundError:
    print('Файл не существует')

length1= len(line1)
length2 = len(line2)
if length1 > length2:
      line1, line2 = line2, line1
lines = []
for i in range(length1):
      lines.append(line1[i].strip() + line2[i].strip())

sort1 = sorted(lines)

with open ('output.txt', 'w') as files_list:
      for i in sort1:
        files_list.write(f'{i}\n')
      

      