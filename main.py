# Task1
def spisok(lst):
    spisok = set(lst)
    return list(spisok)
lst = [1, 2, 5, 2, 3, 1, 4, 5]
print(spisok(lst))

# Task2
def convert_temperature(c):
    f = c * 9/5 + 32
    return f 

с = 13
f = convert_temperature(с)
print(f'Градус селсий {с} в франгет {f}')

# Task
import re 
def search(tex,slov):
    result = re.findall(slov,tex)
    return len(result)
    

text = "Hello hello hello world world "
print(search(text,'hello'))