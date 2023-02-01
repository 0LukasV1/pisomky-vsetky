from PIL import Image

sprava = "Ahoj svet#"
obr = Image.open("duha.png")
pixels = obr.load()

dlyka = 8

def priprav(sprava:str)->list:
    res = []
    for pismenko in sprava:
        cislo= bin(ord(pismenko))[2::]
        pn = dlyka - len(cislo)
        cislo = pn*"0"+cislo
        for j in cislo:
            res.append(int(j))

    return res

def drticka(sprava):
    spvds = priprav(sprava)
    for i in range(len(spvds)):
        sirka = obr.size[0]
        vyska = obr.size[1]
        x = i % sirka
        y = i // sirka
        pixelblue = pixels[x,y][2]
        newblue=int(bin(pixelblue)[2:-1:] + str(spvds[i]),2)
        newcolour =(pixels[x,y][0],pixels[x,y][1],newblue)
        print(pixels[x,y],newcolour)
        pixels[x,y] = newcolour
    obr.save


drticka(sprava)
