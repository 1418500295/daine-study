import json
import os

def getJson(file):
    path = r"C:\Users\ASUS\PycharmProjects\daine-study"
    filename = path + file
    with open(filename, "r",encoding="utf-8")as f:
        data = json.load(f)
        return data
if __name__ == '__main__':
    data = getJson("/test/a.json")
    print(data)
    print(data[0]["name"])
