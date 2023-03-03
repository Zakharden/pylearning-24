from zipfile import ZipFile
from pathlib import Path

"""Path("my-files").mkdir() #создание папки

with open("my-files/first.txt", "w") as my_file:
    my_file.write("This is first file") #создание файла

with open("my-files/second.txt", "w") as my_file:
    my_file.write("This is second file")"""

"""with ZipFile("my-files.zip", mode = "w") as my_zip_file:
    print(my_zip_file) #создание папки zip
    for file in Path('my-files').iterdir():
        print(file) #вывод всего, что в папке"""

"""with ZipFile("my-files.zip", mode = "w") as my_zip_file:
    for file in Path('my-files').iterdir():
        print(file)
        my_zip_file.write(file) #запись файлов в зиппапку"""

#распаковка
with ZipFile('my-files.zip', "r") as my_zip_file:
    my_zip_file.extractall('my-files-unzipped') #распаковка zip