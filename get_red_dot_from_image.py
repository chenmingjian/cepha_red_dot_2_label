import cv2
import os
import numpy as np
import time

begin = time.time()

ROOT_DIR = 'C:/Users/chen/Desktop/red_dot/'
OUT_DIR = 'label/'
IMAGE_DIRS = ['1_350/','2_350/','3_348/']

scale_clear_size = {
    4:6,
    1:4
}

def get_red_dot_img_path(dirs):
    imgs = os.listdir(dirs)
    red_dot_imgs = []
    for i in imgs:
        if i[-5:] == '2.jpg':
            red_dot_imgs.append(i)
    return red_dot_imgs

def get_all_img_file_path():
    final_path = []
    for im_path in IMAGE_DIRS:
        path = ROOT_DIR + im_path
        num_path = os.listdir(path)
        for num in num_path:
            num = path + num
            red_dot_imgs = get_red_dot_img_path(num)
            for red_dot_img in red_dot_imgs:
                final_path.append(num + '/' +red_dot_img)
    return final_path

def find_center_point_by_scale(img, scale, thresh=240):
    point_size = scale_clear_size[scale]
    point_list = []
    for i,row in enumerate( img):
        for j,pixel in enumerate(row):
            if pixel >thresh:
                img[i-point_size:i+point_size, j-point_size:j+point_size] = 0
                point_list.append([j, i])
    
    point_list = np.array(point_list)
    return point_list  


paths = get_all_img_file_path()

for path in paths:

    img = cv2.imread(path,1)
 
    Lower = np.array([0, 0, 100])
    Upper = np.array([40, 40, 255])
    Binary = cv2.inRange(img, Lower, Upper)

    if img.shape[1]>2000:
        scale = 4
    else:
        scale = 1

    resolution = (int(img.shape[1]/scale),int(img.shape[0]/scale))
    #img_1k = cv2.resize(img,(resolution[0],resolution[1]))
    Binary_1k = cv2.resize(Binary,(resolution[0],resolution[1]))


    point_list = find_center_point_by_scale(Binary_1k,scale)
    point_list = point_list * scale + 6/4*scale
    print(path)
    save_txt_path = path[:29]+'/label'+path[29:-6]+'.txt'
    with open(save_txt_path,'w') as f :
        for i in point_list:
            f.write(str(int(i[0]))+','+str(int(i[1]))+'\n')

    #with open('path')

    # font=cv2.FONT_HERSHEY_SIMPLEX
    # for i, point in enumerate( point_list):
    #     cv2.circle (test, (int(point[0]), int(point[1])),1,(255,255,255),thickness=-1)
    #     cv2.putText(test,str(i+1),(int(point[0]), int(point[1])),font,0.5*scale,(255,255,255),int(1*scale))

         
end = time.time()
print("total time is ", end - begin)    