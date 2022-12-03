#%%
from string import ascii_lowercase, ascii_uppercase 
alphabet = ascii_lowercase + ascii_uppercase
# cherry picked the above two lines from mbjoseph after eneumerating alphabet
# in my original solution

def alphabet_lookup(x):
    counter = 0
    for i in alphabet:
        counter = counter + 1
        if x == i:
            break
    return(counter)

with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_3.txt') as f:
    lines = f.readlines()

lines2 = [e.strip() for e in lines]
lengths = [len(e) for e in lines2]
lines_split = [[*e] for e in lines2]

c1 = [lines_split[i][:int(lengths[i]/2)] for i in range(len(lines2))]
c2 = [lines_split[i][int(lengths[i]/2):] for i in range(len(lines2))]

shareds = [set(c1[i]).intersection(c2[i]) for i in range(len(lines2))]

priorities = [alphabet_lookup(list(e)[0]) for e in shareds]
print(sum(priorities))

#%%
badges = [set(lines_split[3*i]).intersection(lines_split[3*i + 1]).intersection(lines_split[3*i + 2]) for i in range(int(len(lines_split)/3))]

priorities2 = [alphabet_lookup(list(e)[0]) for e in badges]
print(sum(priorities2))
