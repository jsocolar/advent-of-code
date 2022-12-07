with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_6.txt', 'r') as f:
    filedata = [*f.read()]

for i in range(4, len(filedata)):
    sublist = filedata[(i-4):i]
    if len(sublist) == len(set(sublist)):
        break

print(i)

for i in range(14, len(filedata)):
    sublist = filedata[(i-14):i]
    if len(sublist) == len(set(sublist)):
        break

print(i)