# load input
with open('/Users/jacobsocolar/Dropbox/Work/Code/AoC_2022/inputs/day_1_1.txt') as f:
    lines = f.readlines()

# part 1
a = b = 0
for i in range(len(lines)): # can use `e in lines`, since we never need the index
    e = lines[i]
    if e == "\n":
        b = max(b, a)
        a = 0
    else:
        a = a + int(e)
b = max(b, a)
print(b)

# part 2
a = b1 = b2 = b3 = 0
for e in lines:
    if e == "\n":
        if a >= b1:
            b3 = b2
            b2 = b1
            b1 = a
        elif a >= b2:
            b3 = b2
            b2 = a
        else:
            b3 = max(b3, a)
        a = 0
    else:
        a = a + int(e)

L = [b1, b2, b3, a]
L.sort()
print(sum(L[1:4]))