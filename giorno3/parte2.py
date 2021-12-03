def trova_ossigeno(lista, posizione):
    if len(lista) <= 1:
        return lista
    else:
        uni = []
        zeri = []
        for b in lista:
            if int(b[posizione]):
                uni.append(b)
            else:
                zeri.append(b)
        if len(zeri) <= len(uni):
            return trova_ossigeno(uni, posizione + 1)
        else:
            return trova_ossigeno(zeri, posizione + 1)


def trova_co2(lista, posizione):
    if len(lista) <= 1:
        return lista
    else:
        uni = []
        zeri = []
        for b in lista:
            if int(b[posizione]):
                uni.append(b)
            else:
                zeri.append(b)
        if len(zeri) <= len(uni):
            return trova_co2(zeri, posizione + 1)
        else:
            return trova_co2(uni, posizione + 1)


uni = []
zeri = []
with open('input.txt', 'r') as file:
    for line in file:
        if int(line[0]):
            uni.append(line)
        else:
            zeri.append(line)
print(uni, zeri)
if len(uni) >= len(zeri):
    o = trova_ossigeno(uni, 1)
    c = trova_co2(zeri, 1)
else:
    o = trova_ossigeno(zeri, 1)
    c = trova_co2(uni, 1)
oxygen_generator_rating = int(o[0], 2)
co2_scrubber_rating = int(c[0], 2)
print(oxygen_generator_rating, co2_scrubber_rating)
print(oxygen_generator_rating * co2_scrubber_rating)
