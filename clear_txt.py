import os 

file_path = []

for root, dirs, files in os.walk(R"C:\Users\chen\Desktop\red_dot\label"):     
    for f in files: 
        file_path.append (os.path.join(root, f)) 

for i in file_path:
    os.remove(i)