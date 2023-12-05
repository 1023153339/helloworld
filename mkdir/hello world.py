# print("hello world")
# 你好世界
# 变量+格式化输出
# xiaoming = 5
# xiaohong = 6.6
# xiaoqiang = 7
# print("一共%.2f块" % xiaohong)
# print(xiaoming+xiaohong+xiaoqiang)
# age = 15
# name = "xiaoming"
# score = 99.55
# print("我叫{}，我今年{},我的数学成绩为{}" .format(name, age, score))
# name = "破烂"
# QQ = 1265654
# iPhone = 1354850471
# company = "汉峪金谷铁投大厦"
# print("================我的名片=================\n姓名:{}\nQQ:{}\n手机号:{}\n公司地址:{}\n================我的名片=================".format(name,QQ,iPhone,company))
# a = input("请输入你的名字")
# print("你的名字是{}".format(a))
# 赋值运算
# a = 205
# b = 3
# c = 30
#  print(a%b)
# b+=a
# print(b)
# a = input("请输入内容")
# a = eval(a)
# print(type(a))
# a=int(a*100)
# print(type(a))
# print(a/100)
# print(not a==b)
# a = input("请输入你的年龄")
# if语句
# if eval(a) >= 18:
#     print("可以进入")
# else:
#     print("出去")
# print("***********SiDAs设备诊断系统*********")
# a = input("请输入您的设备使用年限")
# b = input("请输入您的设备报警等级")
# c = input("请输入您的设备故障次数")
# a = int(a)
# b = int(b)
# c = int(c)
# if a >= 3:
#     a = 20
# elif a < 3:
#     a = 30
# if b == 1:
#     b = 30
# elif b == 2:
#     b = 20
# elif b == 3:
#     b = 10
# elif b == 0:
#     b = 40
# else:
#     b = 0
# if 10 < c <= 50:
#     c = 20
# elif c <= 10:
#     c = 30
# elif c == 0:
#     c = 40
# else:
#     c = 0
# print(a, b, c)
# a += b + c
# print("您的设备得分为{}".format(a))
# a = input("是否有车票，有车票输入1")
# a = int(a)
# if a == 1:
#     print("请进车站进行安检")
#     b = input("请输入安检包裹重量")
#     b = int(b)
#     if b < 10:
#         print("请等待上车")
#     else:
#         print("包裹过重")
# else:
#     print("没有车票请离开")
# while循环
# i = 0
# while i < 100:
#     i += 1
#     print("小破烂")
# i = 2
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i += 2
# print("1到100偶数累加和为{}".format(sum))
# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print("1到100累加为{}".format(sum))
# i=0
# for i in range(0,100):
#     i+=1
#     if i == 20:
#         continue#终止本次循环
#     print(f"小破烂{i}")
# i=0
# while True:
#     i+=1
#     if i ==10:
#         break
#     print("小破烂")

# text = "abcdefg"
# print(text[:-1:2])#展示0到倒数第二的数步长为2
# # print(text[0:])#位置可以不写值
# print(text[::-1])#从后往前展示所有值，步长为1
# text = "sda1"
# print(text.find("1sdd"))
# text = " hello Word"
# print(text.find("e"))#查找text中e的位置
# print(text.index("h"))#查找text中h的位置
# print(text.count("o"))#查找text中o的次数
# print(text.replace("o","e",2))#将text中o替换为e,替换2次
# print(text.split(" "))#依据空格切分
# print(text.capitalize())#第一个单词首字母改成大写，其他的小写
# print(text.title())#所有单词首字母大写
# print(text.startswith("p"))#判断是否以“p”开头
# print(text.endswith("d"))#判断是不是以d结尾
# print(text.lower())#全小写
# print(text.upper())#全大写
# print(text.lstrip(" "))#删除左侧空格
# print(text.rstrip("d"))#删除右侧d
# print(text.isdigit())#判断text是不是纯数字
# print("f".join(text))#在每个元素后加上内容

# 列表
# names = ["zhangsan","lisi","wangwu"]
# print(names[0])#按坐标查找
# for name in names:
# #     print(name)#轮询列举列表内所有元素
# len = len(names)
# print(len)#打印长度
# for i in range(len):
#     print(i)#打印各个位置
#     print(names[i])#使用当前的迭代变量 i 作为索引来从 names 列表中取出一个元素
# len=len(names)
# i=0
# while i<len:
#     print(i)
#     print(names[i])
# #     i+=1
# text = ["张三","李四","王五"]
# a = input("请输入你要找的人")
# if a in text:#判断在或不在
#     b = text.index(a)
#     print(f"{a}存在,位置在第{b+1}位")
# elif a not in text:
#     print(f"{a}不在列表中")
# del text[2]#删除位置
# print(text)
# print(text.pop(0))#删除位置
# print(text.remove("张三"))#删除元素值
# text = ["张三","李四","王五"]
# text.sort(reverse=True)#倒叙排列text
# print(text)
# 字典
text = {"姓名": "张三", "年龄": "20", "身高": "160"}
# print(text["姓名"])#查找键为”姓名“元素
# print(text.get("姓名的"))#查找键为”姓名的“元素
# text["姓名"]="hahha"#修改姓名为hahha
# print(text)
# del text["年龄"]#删除键为“年龄”的元素
# print(text)
# del text#删除字典
# print(text)
# text.clear()#删除字典内所有内容
# print(text)
# print(len(text))
# print(text.keys())
# print(text.values())
# print(text.items())
for key in text.keys():
    print(key)
for values in text.values():
        print(values)
for items in text.items():
    print(items)
for value,key in text.items():
    print(f"key值为{key},对应的键值为{value}")