import os

OUT_DIR = R'C:\Users\chen\Desktop\red_dot\label_may_be_fanal/'
RESULTS = "transformed_model.txt"
CFG ="red_dot.ini"
DECT = {50: 218, 51: 173, 38: 6, 54: 77, 53: 90, 44: 24, 45: 41, 46: 27, 52: 88, 47: 38, 49: 84, 48: 28, 56: 52, 55: 43, 43: 16, 37: 3, 39: 3, 42: 15, 59: 3, 40: 5, 57: 3, 41: 2, 35: 2, 58: 2, 28: 1, 67: 1, 61: 1, 68: 1}

KEYS = [28, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 67, 68]

DST ={28: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\3_348\\1-100\\71.txt', 35: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\2_350\\301-350\\5.txt', 37: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\201-300\\212.txt', 38: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\11.txt', 39: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\2_350\\1-100\\20.txt', 40: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\2_350\\101-200\\36.txt', 41: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\2_350\\301-350\\48.txt', 42: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\2_350\\1-100\\5.txt', 43: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\78.txt', 44: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\14.txt', 45: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\17.txt', 46: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\20.txt', 47: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\31.txt', 48: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\51.txt', 49: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\41.txt', 50: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\1.txt', 51: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\10.txt', 52: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\30.txt', 53: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\13.txt', 54: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\12.txt', 55: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\56.txt', 56: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\1_350\\0-100\\52.txt', 57: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\2_350\\101-200\\40.txt', 58: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\3_348\\1-100\\41.txt', 59: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\2_350\\1-100\\96.txt', 61: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\3_348\\201-300\\281.txt', 67: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\3_348\\201-300\\256.txt', 68: 'C:\\Users\\chen\\Desktop\\red_dot\\label_norm\\3_348\\300-348\\338.txt'}

def get_transform():
    os.system('.\gmmreg_demo.exe  \"TPS_L2\"')

def comput_distance():
    pass

def find_the_nearest():
    pass

def change_src_and_dst_in_cfg(src, dst):
    #src = model = 18 
    #dst = scene = 19 
    with open(CFG,'r') as f: 
        tmp = f.readlines()
    tmp[18] = src
    tmp[19] = dst
    with open(CFG,'w') as f: 
        f.writelines(tmp)


print ('ok')