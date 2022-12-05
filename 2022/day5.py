import numpy as np
import copy

# move list
with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_5.txt', 'r') as f:
    lines = f.readlines()

lines2 = [e.strip() for e in lines]

for i in range(len(lines2)):
    if lines2[i] == "":
        break

moves = lines2[(i+1):]

# initial state
with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_5.txt', 'r') as f:
    filedata = f.read().replace('    ', 'NA  ').replace("]", "] ")

with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_5_modified.txt', 'w') as f:
    f.write(filedata)

with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_5_modified.txt') as f:
    init = np.loadtxt(f, dtype = np.unicode_, max_rows=i-1)

init = np.array(init).T
init = np.fliplr(init).tolist()

def rm_na(x):
    for i in reversed(range(len(x))):
        if x[i] == "NA":
            x.pop(i)
    return(x)
init = [rm_na(e) for e in init]

state = copy.deepcopy(init)

# do changes
def do_moves(state, move):
    move = move.split()
    nm = int(move[1])
    fm = int(move[3]) - 1
    tm = int(move[5]) - 1
    for i in range(nm):
        state[tm].append(state[fm][len(state[fm]) - 1])
        state[fm].pop(len(state[fm]) - 1)
    return(state)

for i in range(len(moves)):
    state = do_moves(state, moves[i])

tops = [e[len(e)-1].replace("[", "").replace("]", "") for e in state]
print("".join(tops))
    
# part 2
def do_moves2(state, move):
    move = move.split()
    nm = int(move[1])
    fm = int(move[3]) - 1
    tm = int(move[5]) - 1
    state[tm] = state[tm] + state[fm][(len(state[fm]) - nm):(len(state[fm]))]
    for i in range(nm):
        state[fm].pop(len(state[fm]) - 1)
    return(state)

state2 = copy.deepcopy(init)

for i in range(len(moves)):
    state2 = do_moves2(state2, moves[i])

tops = [e[len(e)-1].replace("[", "").replace("]", "") for e in state2]
print("".join(tops))