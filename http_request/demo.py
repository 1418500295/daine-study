

class Study():

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __run(self):
        print("hello")

    def sing(self):
        print("sing")

class Man(Study):

    def play(self):
        print("play")


    def drink(self):
        # super().sing()
        super(Man,self).sing()

    def sing(self):
        print("hha")
    



if __name__ == '__main__':
    s = Study("daine",12)
    s.sing()
    # 调用私有方法
    s._Study__run()

    m = Man("james",11)
    m.drink()
    m.sing()



