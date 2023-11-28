import random#导入random
a = "剪刀"
b = "包袱"
c = "锤"
e = random.choice([a,b,c])#随机生成
d = random.choice([a,b,c])
print(e,d)
if e == a and d == b:
    print("e胜利")
elif e ==a and d==c:
    print("d胜利")
elif e==b and d==a:
    print("d胜利")
elif e==b and d==c:
    print("b胜利")
elif e==c and d==a:
    print("e胜利")
elif e==c and d ==b:
    print("e胜利")
else:
    print("平")
