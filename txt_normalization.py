import cv2 
import os
import numpy as np


txt_path_list = []
for root, dirs, files in os.walk(R"C:\Users\chen\Desktop\red_dot\label"):
    for i, f in enumerate(files) : 
        txt_path_list.append(os.path.join(root, f))

img_path_list = []
for txt_path in txt_path_list:
    img_path_list.append((txt_path[:29]+txt_path[29+6:])[:-4]+'-2.jpg')

target_path_list = []
for txt_path in txt_path_list:
    target_path_list.append(txt_path[:29]+'\label_norm'+txt_path[29+6:])

for i in range(len(txt_path_list)):
    (y, x) = cv2.imread(img_path_list[i],0).shape
    normed_list = []
    with open(txt_path_list[i]) as f:
        lines = f.readlines()
    for line in lines :
        tmp = np.array(line.split(','),dtype =int)
        normed = tmp / np.array([x, y])
        normed_list.append(normed)
    normed_list = np.array(normed_list)
    with open(target_path_list[i],'w') as f: 
        for norm in normed_list:
            tmp = '%16.7e %15.7e'%(norm[0], norm[1])
            f.write(tmp + '\n')

            
    

