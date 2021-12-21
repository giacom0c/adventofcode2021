def fakemod(a, b):
    res = a % b
    if res:
        return res
    return b


p1 = 4
p2 = 8
s1 = s2 = rolls = 0
tablemod = 10
dicemod = 100
target = 1000
while s1 < target and s2 < target:
    rolls += 3
    d1 = fakemod(rolls - 2, dicemod)
    d2 = fakemod(d1 + 1, dicemod)
    d3 = fakemod(d2 + 1, dicemod)
    #print(d1, d2, d3)
    move = fakemod(d1 + d2 + d3, tablemod)
    if not rolls % 2:
        #print('secondo')
        p2 = fakemod(p2 + move, tablemod)
        s2 += p2
        #print(move, p2, s2)
    else:
        p1 = fakemod(p1 + move, tablemod)
        #print('primo')
        s1 += p1
        #print(move, p1, s1)
print(rolls)
print(p1, p2, s1, s2)
