fr = open('vstupla.txt','r')
max_elf = 0
elf = 0
for row in fr:
    temp = row.strip()
    if temp.isdigit():
        elf += int(temp)
    else:
        if elf > max_elf:
            max_elf = elf
        elf = 0
print(max_elf)
