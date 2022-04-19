#this is the converter that i talked about in the converter.py file, it converts binary numbers to decimal numbers
#you just need to insert the binary number and the bits that contains it

bi = str(input("Insert a binary number: "))
bits = int(input("How many Bits does it take to represent your number? "))
a = len(bi)

s = []
cards = []

for i in range(bits - 1, -1, -1):
    cards.append(2 ** i)
    s.append(0)

c = 0
b = 1
for z in range(a):
    g = bi[c:b]
    c = c + 1
    b = b + 1
    if g == "1":
        s[z] = cards[z]
r = sum(s)
print(f"Your binary number converted to decimal is:{r}")
