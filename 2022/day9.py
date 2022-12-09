import copy
# load input
with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_9.txt') as f:
    lines = [e.strip().split() for e in f.readlines()]

hp = [0,0]
tp = [0,0]

def move_head(hp, dir):
    if dir == "R":
        hp[0] += 1
    elif dir == "L":
        hp[0] += -1
    elif dir == "U":
        hp[1] += 1
    elif dir == "D":
        hp[1] += -1
    else:
        raise(Exception)
    return(hp)

def move_tail(hp, tp):
    xdif = hp[0] - tp[0]
    ydif = hp[1] - tp[1]
    if (abs(xdif) < 2) & (abs(ydif) < 2): # no need to move
        return(tp)
    else:
        if hp[0] > tp[0]:
            tp[0] += 1
        if hp[0] < tp[0]:
            tp[0] += -1
        if hp[1] > tp[1]:
            tp[1] += 1
        if hp[1] < tp[1]:
            tp[1] += -1
    return(tp)

tail_positions = [[0,0]]
for i in lines:
    for j in range(0, int(i[1])):
        hp = move_head(hp, i[0])
        tp = move_tail(hp, tp)
        tail_positions.append(copy.deepcopy(tp))

tp_set = set(map(tuple, tail_positions))
print(len(tp_set))


positions = [[0,0] for e in range(0,10)]
tail_positions = [[0,0]]
for i in lines:
    for j in range(0, int(i[1])):
        positions[0] = move_head(positions[0], i[0])
        for k in range(1,10):
            positions[k] = move_tail(positions[k-1],positions[k])
        tail_positions.append(copy.deepcopy(positions[9]))
tp_set2 = set(map(tuple, tail_positions))
print(len(tp_set2))