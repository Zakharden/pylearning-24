import random
import secrets
import string
print(random.random())
print(random.randint(1,12))
print(random.choice([1,2,3,1,12,12]))
print(random.choices([23,1,2,12,132,3131], k=3))
print(random.shuffle([23,1,2,12,132,3131])) #меняет порядок

#random генерирует псевдослучайные значения, а для генерации паролей это не подходит
#import secrets, import string
all_char = string.ascii_letters + string.digits + string.punctuation
print("".join(secrets.choice(all_char) for i in range(12)))