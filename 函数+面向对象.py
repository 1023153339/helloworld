# def caiquan(a,b,c) :
#     d=a + b - c
#     return d #返回给调用函数的地方,后边的内容都不运行
# print(caiquan(1,10,3))
# class WangZhe():#类
#     def __init__(self,name,jineng):
#        self.name=name
#        self.jineng=jineng
#     def ac(self):
#         print(self.name)
#     def info(self):  # 添加一个info方法来打印对象的属性
#             print(self.name)
#             print(self.jineng)
# car1 = WangZhe("鲁班","大炮")#使用者为对象
# print(id(car1))
# car1.info()
# car2 = WangZhe("后裔","c")#使用者为对象
# print(id(car2))
# car2.info()
# class Book:
#     def __init__(self,name,number):
#         self.name = name
#         self.number = number
#     def __str__(self):
#         return f"name:{self.name},number:{self.number}"
#     def __del__(self):
#         print(f"书名为{self.name}，编号为{self.number}")
# # book1 = Book("小王子","01")
# # print(book1)  # 输出：name:小王子,number:01
# # 删除对象
# # del book1  # 输出：书名为小王子，编号为01
# class Kokk(Book):
#     pass
# kokk=Kokk("fafa","fd")

#练习
class A:
    def __init__(self):
        self.Ab="会做A类汉堡"
        self.coffee="会做A类咖啡"
    def __str__(self):
        return f"{self.Ab}，并且{self.coffee}"
class B:
    def __init__(self):
        self.Bb="会做B类汉堡"
        self.coffee="会做B类咖啡"
    def __str__(self):
        return f"{self.Bb}也会做{self.coffee}"
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.Cb="会做C类汉堡"
        self.coffee="会做多样咖啡"

    def __str__(self):
            return f"{self.Bb}也会做{self.coffee}和{self.Ab}{self.Cb}"
c=C()
print(c)