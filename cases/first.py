

class Daine:
    def __init__(self, name):
        self.name = name

    def print(self):
        print("my name is %s" % self.name)

if __name__ == '__main__':
    Daine("james").print()