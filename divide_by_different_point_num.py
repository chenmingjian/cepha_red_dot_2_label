import os 
import numpy as py

SRC_ROOT = R"C:\Users\chen\Desktop\red_dot\label_norm"
DST_ROOT = R"C:\Users\chen\Desktop\red_dot\label_classify_by_point_num"
KEYS = [28, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 67, 68]

txt_path_list = []
for root, dirs, files in os.walk(SRC_ROOT):
    for i, f in enumerate(files) : 
        txt_path_list.append(os.path.join(root, f))

def get_same_num_point(targer = 50):
    match_path_list = []
    for txt_path in txt_path_list:
        with open(txt_path) as f: 
            point_num = len( f.readlines())
        if point_num ==  targer:
            match_path_list.append(txt_path)
    return match_path_list

def cp_list_to_new_path(src_path_list, dst_path):
    for src_path in src_path_list:
        new_file_name = src_path[41:].replace('\\', '_')
        dst_file_name = dst_path + '\\' + new_file_name
        print (dst_file_name)
        os.system("copy %s %s"%(src_path, dst_file_name))
        
def label_classify_by_point_num():
    for i in KEYS:
        point_i = get_same_num_point(targer = i)
        dir_name = "\\" + str(i)
        if not os.path.exists(DST_ROOT + dir_name):
            os.makedirs(DST_ROOT + dir_name)
        cp_list_to_new_path(point_i, DST_ROOT + dir_name)

