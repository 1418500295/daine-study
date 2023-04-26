a = "萨达萨达"
from functools import wraps
import pickle



import openpyxl
import xlrd, xlwt
from xlutils.copy import copy

file_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(file_path, 'demo.xlsx')
print(base_path)
book = xlrd.open_workbook(base_path)
sheet = book.sheet_by_index(0)

xfile = openpyxl.load_workbook(base_path)
sheet1 = xfile.get_sheet_by_name("Sheet1")

for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        if i == 0:
            continue
        else:
            value = sheet.cell_value(i, j)
            print(value)
            sheet1["D"+str(i+1)] = 2
xfile.save(base_path)





# def done(level):
#     def decorator(one):
#         @wraps(one)
#         def wrapper():
#             if level == 3:
#                 print("这世界很酷")
#             one()
#         return wrapper
#     return decorator
#
# @done(level=3)
# def one():
#     print("我的世界")
# #
# one()

# class Request():
#     def __init__(self,one,url,method):
#         self.one = one
#         self.url = url
#         self.method = method
#     def __call__(self, *args, **kwargs):
#         print("哈哈")
#         self.one()
#
# def one():
#     print("呵呵")
#
# one()






