a = "我十分赶得上"
c = a.count("我")
print(c,c.__class__)
print(a.endswith("上"))
print(a.index("得"))
print(a.split("分"))
print(a.find("得"))
print(a.__contains__("上"))
print(a.__add__("哈哈"))
print(a.__len__())
print(len(a))
print(a.__class__)
print(type(a))
c = 3
print(c.__eq__(3))
import re


a = "据官方首发hkfkdg首发fdsjk'"
c = re.findall("首发*",a)
print(c)


def run():
    a = "fsfsdgdgfs"
    return a.__len__()

if __name__ == '__main__':
    print(run())

