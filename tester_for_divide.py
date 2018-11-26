import os
import numpy as np 

ROOT = R'C:\Users\chen\Desktop\red_dot\label_tmp/'

tmp1 = np.loadtxt(ROOT + '_2.txt')
tmp2 = np.loadtxt(ROOT + '3.txt')

print(tmp1.shape, tmp2.shape)

def get_some_point(tmp1):
    tmp1_new_list = []
    for i in tmp1: 
        print(i)
        if i[0] > 0.6 and i[1] > 0.7:
            tmp1_new_list.append(i)
    tmp1_new_list = np.array(tmp1_new_list)
    return tmp1_new_list

tmp1 = get_some_point(tmp1)
tmp2 = get_some_point(tmp2)
print(tmp1.shape, tmp2.shape)

np.savetxt(ROOT + '_2_p.txt',tmp1)
np.savetxt(ROOT + '3_p.txt',tmp2)
