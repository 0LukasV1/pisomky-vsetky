game = {('A','X'):4, ('A','Y'):8, ('A','Z'):3,('B','X'):1,('B','Y'):5,('B','Z'):9,('C','X'):7,('C','Y'):2,('C','Z'):6}
fr = open('vstup uloha 2','r')
suma = 0
for row in fr:
    chars = row.strip().split()
    suma += game[(chars[0],chars[1])]
print(suma)
