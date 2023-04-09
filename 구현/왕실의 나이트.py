loca = input()
yloc = int(loca[1])
xloc = int(ord(loca[0])) - int(ord('a')) + 1

types = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0

for type in types:
    nxloc = xloc + type[0]
    nyloc = yloc + type[1]
    if 1 <= nxloc <= 8 and 1 <= nyloc <= 8:
        count += 1

print(count)