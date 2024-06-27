try:
    with open('input.txt', 'r') as sales_file:
        stores = {}
        sales = sales_file.readlines()
except FileNotFoundError:
    print('Файл не найден')


for i in sales:
     if ('{' not in i) and ('}' not in i):
        sale = i.split(':')
       
        if sale[0].strip() in stores:
            stores[sale[0].strip()] += int(sale[1].strip().strip(','))
        else:
            stores[sale[0].strip()] = int(sale[1].strip().strip(','))
    

with open ('output.txt', 'w') as count_file:
    for key, value in stores.items():
        count_file.write(f'{key}:{value}\n')