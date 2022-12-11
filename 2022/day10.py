import copy
with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_10.txt') as f:
    lines = [e.strip().split() for e in f.readlines()]

x = [1]
for i in lines:
    x.append(copy.deepcopy(x[len(x) - 1]))
    print(i)
    if i[0] == "addx":
        x.append(copy.deepcopy(x[len(x) - 1]) + int(i[1]))

cycles_use = [40*x + 20 for x in range(6)]    
strengths = [i*x[i - 1] for i in cycles_use]
print(sum(strengths))

render_chars = {
    True: "#",
    False: " "
}
x_split = [x[i*40 : (i+1)*40] for i in range(6)]
draw_tf = '\n'.join([''.join([render_chars[abs(e - x_split[i][e]) < 2] for e in range(40)]) for i in range(6)])
print(draw_tf)