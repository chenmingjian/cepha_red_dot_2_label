
import os 
g = os.walk(R'C:\Users\chen\Desktop\red_dot\label_norm')  

frequency = {}
count = []
path_list = []
for path,dir_list,file_list in g:  
    for file_name in file_list:  
        tmp = os.path.join(path, file_name)
        if tmp[-3:] == 'txt':
            with open(tmp) as f:
                count.append(len(f.readlines()))
                path_list.append(tmp)

for word in count:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1

model = {}
print(set(count))
tmp_sorted_key = sorted(frequency.keys())
for i in tmp_sorted_key:
    check = i
    #print(frequency)
    a = count.index(check)
    #print(path_list[a])
    if check not in model:
        model[check] = path_list[a]

print(model)