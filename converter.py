#Decimal to binary number converter

decimal = int(input("Insert a decimal number: "))
a = int(input("How many bytes do you desire? "))

cards = []
t = []
for i in range(a-1, -1,-1):
    cards.append(2**i)
    t.append(0)

r = decimal
g = 0

while r !=0:
    if r >= cards[g]:
        r = r - cards[g]
        t[g] = cards[g]
        if t[g] != 0:
            t[g] = 1
            print(r)
    g = g + 1
print("Yor decimal number converted to Binary is:", *t, sep ="")
