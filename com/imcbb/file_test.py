f = open("/Users/kevin/Desktop/temp.txt", "r")

with f as v2:
    # v2.writelines("我更新了文件，哈哈！")
    print(v2.read())

# with 会自动关闭流 所以下面的读取会失败
# for v in f:
#     print(v.strip())


with open("/Users/kevin/Desktop/python_auto_gen.txt", "w") as f:
    f.writelines("这个文件是python自动生成")
    print("文件已经生成。。。")
