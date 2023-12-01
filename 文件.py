# file=open("00.txt","w")
# file.write("dfsfsfdfds")
# file.close()
# file=open("00.txt","r")
# print(file.read(5))
# file.close()
# 打开老文件
file = input("请输入要备份的文件名")
oldfile = open(file, "r")
content = oldfile.read()
# 找到老文件后缀名
end = file.rfind(".")
nameend=file[end:]
name=file[:end]
# 新建新文件，名称为老文件-复制
newname = name + "-复制" + nameend
print(newname)
newfile = open(newname, "w")
for copy in file:
    newfile.write(copy)
oldfile.close()
newfile.close()
# 复制老文件到新文件
