import numpy as np
import copy

# load input
with open('/Users/jacobsocolar/Dropbox/Work/Code/advent_of_code/2022/inputs/day_8.txt') as f:
    lines = [[*e.strip()] for e in f.readlines()]

lines = [[int(x) for x in e] for e in lines]

my_array = np.array(lines)

# for part 2, we know that the all of the trees on the edge
# get zeros, so without loss of generality we replace them with
# heights of 10, so that we can ask where the closest tree that's 
# as tall as the focal tree is and get the length of the view even
# if the focal tree can see past the edge.
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

        # Out of curiosity, are the elves dumb? Have they asked me to find a max 
        # senic score that corresponds to a tree that can be seen from the outside?
        real_view_west = [e >= my_height for e in my_array[i, 0:j]]

        real_view_east = [e >= my_height for e in my_array[i, (j+1):d1]]

        real_view_north = [e >= my_height for e in my_array[0:i, j]]

        real_view_south = [e >= my_height for e in my_array[(i+1):d0, j]]



        senic_score = length_west * length_east * length_north * length_south
        if senic_score > max_senic:
            elves_dumb_north = not max(real_view_north)
            elves_dumb_south = not max(real_view_south)
            elves_dumb_east = not max(real_view_east)
            elves_dumb_west = not max(real_view_west)

        max_senic = max(max_senic, senic_score)


print(counter + 2*(d0 - 1) + 2*(d1 - 1))
print(max_senic)

print(elves_dumb_north)
print(elves_dumb_south)
print(elves_dumb_east)
print(elves_dumb_west)