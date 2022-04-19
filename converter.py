#Decimal to binary number converter

decimal = int(input("Insert a decimal number: "))
a = int(input("How many bytes do you desire? "))

bytes_t = [] #total bytes, i used cards previously cause my professor gave examples of binary numbers using cards.
t = []
for i in range(a-1, -1,-1):
    bytes_t.append(2**i)
    t.append(0)

r = decimal
g = 0

while r !=0:
    if r >= bytes_t[g]:
        r = r - bytes_t[g]
        t[g] = bytes_t[g]
        if t[g] != 0:
            t[g] = 1
            print(r)
    g = g + 1
print("Yor decimal number converted to Binary is:", *t, sep ="")
