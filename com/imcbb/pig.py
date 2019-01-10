class Pig(object):
    color = "black"

    def __init__(self, color):
        self.color = color
        print(color + " pig init,")

    def info(self):
        print("pig info")

    if __name__ == "__main__":
        print("main run!")

    # 可变参数
    def get_gargs(self, *args):
        for arg in args:
            print(arg, end=",")

    def get_args_kv(self, **kwargs):
        for k, v in kwargs.items():
            print("{0}={1}".format(k, v))

