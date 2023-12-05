import os
#展示所有文件名
path = "./aa/"
a=print(os.listdir(path))
#循环修改所有文件名
for name in os.listdir(path):
    newname=("hah"+name)
    os.rename(path+name,path+newname)
print(os.listdir(path))
