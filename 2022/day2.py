#%%
with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_2.txt') as f:
    lines = f.readlines()

lines2 = [e.strip() for e in lines]
my_throws = [e.split()[1] for e in lines2]
their_throws = [e.split()[0] for e in lines2]

wins = ["A Y", "B Z", "C X"]
draws = ["A X", "B Y", "C Z"]
losses = ["A Z", "B X", "C Y"]

win_pts = sum(x in wins for x in lines2) * 6
draw_pts = sum(x in draws for x in lines2) * 3
throw_pts = (sum([e == 'X' for e in my_throws]) +
    2 * sum([e == 'Y' for e in my_throws]) +
    3 * sum([e == 'Z' for e in my_throws]))

print(win_pts + draw_pts + throw_pts)

#%%
their_throws2 = [int(0) if x=="A" else int(1) if x=="B" else int(2) for x in their_throws]

print(my_throws[0])

my_throws2 = my_throws.copy()
for i in range(len(my_throws2)):
    print(i)
    if my_throws[i] == "X":
        my_throws2[i] = losses[their_throws2[i]].split()[1]
    elif my_throws[i] == "Y":
        my_throws2[i] = draws[their_throws2[i]].split()[1]
    else:
        print("hello")
        my_throws2[i] = wins[their_throws2[i]].split()[1]

throw_pts2 = (sum([e == 'X' for e in my_throws2]) +
    2 * sum([e == 'Y' for e in my_throws2]) +
    3 * sum([e == 'Z' for e in my_throws2]))
win_pts2 = sum(x == "Z" for x in my_throws) * 6
draw_pts2 = sum(x == "Y" for x in my_throws) * 3
print(throw_pts2 + win_pts2 + draw_pts2)