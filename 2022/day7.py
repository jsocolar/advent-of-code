import re
import copy
# load input
with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_7.txt') as f:
    lines = [e.strip() for e in f.readlines()]

# Do we ever enter the same directory twice from below?
r = re.compile("^\$ cd [A-Za-z/]")
cds = list(filter(r.match, lines))
print(len(cds) == len(set(cds))) # yes, we do

def cd_check(i):
    r = re.compile("^\$ cd")
    return(r.match(i))

def enter_check(i):
    if not cd_check(i):
        raise Exception("enter_check applied to non-cd statement")
    else:
        r = re.compile("\.\.$")
        return(r.search(i) == None)

def get_entered_dir(i):
    if not enter_check(i):
        raise Exception("get_entered_dir applied to non-entering statement")
    else:
        return(i.lstrip("\$ cd "))

def ls_check(i):
    r = re.compile("^\$ ls")
    return(r.match(i))

dir_paths = [] # will become a list of unique paths
dir_checked = [] # will tell us whether we've already run ls from the corresponding directory
dir_sizes = [] # will tell us the size of the directory
current_path = [] # will store the current path

checking = False # if we see a file size, should we add it to the size of the directory?
# (designed to handle what happens if we run ls when dir_checked is already True)
for i in lines:
    if bool(cd_check(i)) or bool(ls_check(i)):
        checking = False
    if cd_check(i):
        checking = False
        if enter_check(i):
            if i == "cd /":
                current_path = ["/"]
            else:
                current_path.append(get_entered_dir(i))
            if not (current_path in dir_paths):
                dir_paths.append(copy.deepcopy(current_path))
                dir_checked.append(False)
                dir_sizes.append(0)
        else:
            current_path.pop()
        dpi = dir_paths.index(current_path)
    else:
        if bool(ls_check(i)) & (not dir_checked[dpi]):
            checking = True
    if checking:
        r = re.compile("^\d+")
        match = r.search(i)
        if match:
            dir_sizes[dpi] = dir_sizes[dpi] + int(match.group())

collapsed_paths = ['/'.join(e) for e in dir_paths]

dir_sizes2 = copy.deepcopy(dir_sizes)
for i in range(len(dir_sizes)):
    for j in range(len(dir_sizes)):
        if i != j:
            if re.match(re.escape(collapsed_paths[j]), re.escape(collapsed_paths[i])):
                dir_sizes2[j] += dir_sizes[i]


answer = 0
for i in dir_sizes2:
    if i <= 100000:
        answer += i
print(answer)

used_space = sum(dir_sizes)
need_to_delete = used_space - 40000000

answer2 = float('inf')
for i in dir_sizes2:
    if i >= need_to_delete:
        answer2 = min(answer2, i)
print(answer2)