import copy
import re
import numpy
with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_11.txt') as f:
    lines = [e.strip() for e in f.readlines()]

# parse input

inits = []
operations = []
tests = []
action_t = []
action_f = []

for i in lines:
    r = re.compile("^Starting items")
    if r.match(i) != None:
        inits.append([int(e) for e in i.strip("Staring ems:").split(", ")])
    r = re.compile("^Operation")
    if r.match(i) != None:
        operations.append(i[17:])
    r = re.compile("^Test")
    if r.match(i) != None:
        tests.append(int(re.findall(r'\d+', i)[0]))
    r = re.compile("^If true")
    if r.match(i) != None:
        action_t.append(int(re.findall(r'\d+', i)[0]))
    r = re.compile("^If false")
    if r.match(i) != None:
        action_f.append(int(re.findall(r'\d+', i)[0]))

n_inspect = [0]*len(inits)

test_prod = numpy.prod(tests)

for i in range(10000):
    for m in range(len(inits)):
        n_inspect[m] += len(inits[m])
        for j in range(len(inits[m])):
            old = inits[m][0]
            worry_level = eval(operations[m])
            worry_level = worry_level % test_prod
            inits[m].pop(0)
            if(worry_level % tests[m] == 0):
                inits[action_t[m]].append(worry_level)
            else:
                inits[action_f[m]].append(worry_level)
n_inspect.sort()
n_inspect.reverse()
print(n_inspect[0] * n_inspect[1])
            