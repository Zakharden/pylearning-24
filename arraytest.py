from array import array

my_int_array = array('i', [1,2,4,6,3,34])  #создает массив
print(my_int_array)
print(type(my_int_array))

with open("my_array.bin", "wb") as my_file: #записывает массив в файл
    my_int_array.tofile(my_file)

imported_array = array('i')

with open("my_array.bin", 'rb') as my_file:  #читает массив из файла
    imported_array.fromfile(my_file, len(my_int_array))
    print(imported_array)

imported_array.reverse() #реверс
print(imported_array)