import csv

with open("test.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['user_id', 'user_name'])
    writer.writerow(['1', 'Zakhar'])
    writer.writerow(['2', 'Dasha']) #Запись в csv

with open("test.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for line in reader: #чтение в виде списков
        print(line)


