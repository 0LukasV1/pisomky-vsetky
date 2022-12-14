fr = open('vstupla.txt','r')
max_elf = 0
elf = 0
zoz = []

for row in fr:
    temp = row.strip()
    if temp.isdigit():
        elf += int(temp)
    else:
        if elf > max_elf:
            max_elf = elf
        zoz.append(elf)
        elf = 0
utzoz = sorted(zoz,reverse=True)
print(utzoz)
print(sum(utzoz[0:3:1]))
