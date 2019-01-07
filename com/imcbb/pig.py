class Pig(object):

    color = "black"

    def __init__(self, color):
        self.color = color
        print(color + " pig init,")

    def info(self):
        print("pig info")

    if __name__ == "__main__":
        print("main run!")
