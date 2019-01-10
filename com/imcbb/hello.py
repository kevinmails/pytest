import sys
import pig
from datetime import date

print("hello world")


def test(name):
    print("hello", name)


def hello_world():
    print("hello world")


def get_name(my_name):
    return "my name is " + my_name


test("kevin")
name_str = get_name("中国!")
print(name_str)
print("w" in name_str)
print(name_str[10:13])
# print(name_str[100])

# in_str = input("please type:")
# print("用户输入：" + in_str)


if 1 > 2:
    print("1>2")
else:
    print("1>2 is false")

print(sys.path)
print(hello_world())
print(date.today())

red_pig = pig.Pig("red")
red_pig.get_gargs("a", "b", "c")
red_pig.get_args_kv(name="kevin", age=20)



