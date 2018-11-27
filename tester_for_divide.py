###############
# sad warning #
###############

import os
import numpy as np 

ROOT = R'C:\Users\chen\Desktop\red_dot\label_tmp/'

txt_1 = np.loadtxt(ROOT + '_2.txt')
txt_2 = np.loadtxt(ROOT + '3.txt')

print(txt_1.shape, txt_2.shape)


def get_some_point(txt_1, point_range):
    distance_list = []
    coordinate_list = []
    for i in txt_1: 
        tmp = (1-i[0])**2 + (1-i[1])**2 + \
                i[0]**2 + i[1]**2  +\
                (1-i[0])**2 + i[1]**2 +\
                i[0]**2 + (1-i[1])**2
        distance_list.append(tmp)
        coordinate_list.append(i)
    coordinate_list = np.array(coordinate_list)
    sorted_distance_list = sorted(distance_list)
    tmp = [distance_list.index(sorted_distance_list[i]) for i in range(point_range[0],point_range[1])]
    return coordinate_list[tmp]

_range = [25,35]
txt_1 = get_some_point(txt_1,_range)
txt_2 = get_some_point(txt_2,_range)
print(txt_1.shape, txt_2.shape)

np.savetxt(ROOT + '_2_p.txt',txt_1)
np.savetxt(ROOT + '3_p.txt',txt_2)
