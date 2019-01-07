import random
import pig

a = 3
b = 4
d = 0.536
c = a+b
c2 = a + d
print(c)
print(c2)

# round(x [,n])浮点数x的四舍五入值,n则代表舍入到小数点后的位数。
print(round(c2, 2))


for v in range(10):
    r = random.choice(range(2, 10))
    print(r)


pig.Pig("red")


