

import xlrd,xlwt
"""
读取properties文件
"""
class OperateProperties():

    def __init__(self,file_name):
        self.file_name = file_name
        self.properties = {}

    def read_file(self):
        with open(self.file_name,"r",encoding="utf-8")as f:
            data = f.readlines()
            print(data)
            for i in data:
                r = i.split('=')
                self.properties[r[0].strip()] = r[1].strip().replace("\n",'')

            return self.properties


if __name__ == '__main__':
    data = OperateProperties("application.properties").read_file()
    # # print(data)
    print(data['sex'])



    # sheet = xlrd.open_workbook("daine.xlsx")
    # table = sheet.sheet_by_index(0)
    # print(table.name)
    # print(table.nrows,table.ncols)
    # # 打印第三列的数据
    # print(table.col_values(2))
    # print(table.row_values(2))













