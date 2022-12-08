import numpy as np
import copy

# load input
with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_8.txt') as f:
    lines = [[*e.strip()] for e in f.readlines()]

lines = [[int(x) for x in e] for e in lines]

my_array = np.array(lines)

my_array2 = copy.deepcopy(my_array)
my_array2[0,:] = 10
my_array2[:,0] = 10
my_array2[my_array2.shape[0] - 1:] = 10
my_array2[:,my_array2.shape[1] - 1] = 10

d0 = my_array.shape[0]
d1 = my_array.shape[1]


counter = 0
max_senic = 0
for i in range(1,(d0 - 1)):
    for j in range(1,(d1 - 1)): #range over all the interior trees
        heights = [] # get the max heights between the tree and the edge in each direction
        heights.append(max(my_array[i, 0:j]))
        heights.append(max(my_array[i, (j+1):d1]))
        heights.append(max(my_array[0:i, j]))
        heights.append(max(my_array[(i+1):d0, j]))
        if min(heights) < my_array[i,j]:  # check that 
            counter += 1
        my_height = my_array[i, j]

        view_west = [e >= my_height for e in my_array2[i, 0:j]]
        view_west.reverse()
        length_west = view_west.index(True) + 1

        view_east = [e >= my_height for e in my_array2[i, (j+1):d1]]
        length_east = view_east.index(True) + 1

        view_north = [e >= my_height for e in my_array2[0:i, j]]
        view_north.reverse()
        length_north = view_north.index(True) + 1

        view_south = [e >= my_height for e in my_array2[(i+1):d0, j]]
        length_south = view_south.index(True) + 1

        senic_score = length_west * length_east * length_north * length_south
        max_senic = max(max_senic, senic_score)


print(counter + 2*(d0 - 1) + 2*(d1 - 1))
print(max_senic)
