#Decimal to binary number converter

decimal = int(input("Insert a decimal number: "))
a = int(input("How many bits do you desire? "))

bits = [] #total bits, i used cards previously cause my professor gave examples of binary numbers using cards.
t = []
for i in range(a-1, -1,-1):
    bits.append(2**i)
    t.append(0)

r = decimal
g = 0

while r !=0:
    if r >= bits[g]:
        r = r - bits[g]
        t[g] = bits[g]
        if t[g] != 0:
            t[g] = 1
            print(r)
    g = g + 1
print("Yor decimal number converted to Binary is:", *t, sep ="")
