with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_4.txt') as f:
    lines = f.readlines()

lines2 = [e.strip() for e in lines]
lines3 = [e.split(",") for e in lines2]
first_elf = [e[0].split("-") for e in lines3]
second_elf = [e[1].split("-") for e in lines3]

number_complete_overlaps = 0
number_partial_overlaps = 0
for i in range(len(lines)):
    if (int(first_elf[i][0]) <= int(second_elf[i][1])) & (int(second_elf[i][0]) <= int(first_elf[i][1])):
        number_partial_overlaps = number_partial_overlaps + 1
    if (int(first_elf[i][0]) >= int(second_elf[i][0])) & (int(first_elf[i][1]) <= int(second_elf[i][1])):
        number_complete_overlaps = number_complete_overlaps + 1
    elif (int(first_elf[i][0]) <= int(second_elf[i][0])) & (int(first_elf[i][1]) >= int(second_elf[i][1])):
        number_complete_overlaps = number_complete_overlaps + 1

print(number_complete_overlaps)
print(number_partial_overlaps)