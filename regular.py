import re
"""stroka = "Hello, my name is Zakhar!"
stroka2 = "Hello, my name is Zakhar, Zakhar."

res = re.search("Zakhar", stroka)
res1= re.search("Z....r", stroka)
res2 = re.search("Z$", stroka)
res3 = re.search("^H.*is", stroka) #искать именно точку /.
print(res3)

my_pattern = re.compile(r'Z....r\!$')
my_pattern2 = re.compile(r'Z....r')
print(my_pattern)
print(my_pattern.search(stroka))
print(my_pattern.match(stroka2)) #проверка на совпадение
print(my_pattern.findall(stroka2)"""


#проверка email  c помощью регулярного выражения
"""email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
email_check_pattern = re.compile(email_regexp)
print(email_check_pattern.fullmatch("zakhardenn@gmail.com"))"""

def check_email(mail):
    if type(mail) != str:
        raise TypeError("This is not string")
    email_expml = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_expml_pattern = re.compile(email_expml)
    if email_expml_pattern.fullmatch(mail):
        return "Good!"
    else:
        return "Not good!"

print(check_email("zakhardenngmail.com"))