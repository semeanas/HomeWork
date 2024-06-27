try:
    with open ('cities.txt', 'r') as city_file:
        cities = {}
        citys = city_file.readlines()
        for i in citys:
            city1 = i.split(':')
            cities[city1[0].strip()] = int(city1[1].strip())
except FileExistsError:
    print('Файл не найден')

popul = int(input())

for_del = []
for city, population in cities.items():
    
    if popul >= population:
        for_del.append(city)
for i in for_del:
    cities.pop(i)

sort = sorted(cities)

with open('filtered_cities.txt', 'w') as cleaned_list:
    for i in sort:
        cleaned_list.write(f'{i}\n')




