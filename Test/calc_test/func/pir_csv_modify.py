# _*_ coding:utf-8 _*_
"""
@date: 20170622
@author: 李天琦
@update: 20170623
"""

import os
import csv
from .bw_to_pir import bw_to_pir
from .csv_to_dict import csv_to_dict

N = 4000    # 修改这个值后要将csv文件删除，否则文件行数不会更新

def pir_csv_modify(def_bw = None, spec_bw = None, bw_csv = None):
    """
    修改pir.csv文件

    参数：
        def_bw: 默认带宽值，对应大多数的一样的带宽值，不传此参数时，不对pir整体修改
        spec_bw: 指定特定的带宽值，字典类型，{"shaper编号（取0-4000）", 带宽值}
        bw_csv: 可指定包含带宽值的csv文件，格式为两列，第一列为shaper id，第二列为带宽值(M)
    输出: 
        csv文件
    """

    print("ready to modify...")

    # 如果csv文件不存在，创建一个全0的初始文件
    if not os.path.exists('pir.csv'):
        print("no pir.csv, creating a new file...")

        with open("pir.csv", 'w') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(N):
                writer.writerow(['0x0000'])
                
            print("successfully created!")

    def modify_with_def(def_bw, pir):
        """
        用默认值修改
        """
        def_pir = bw_to_pir(def_bw)
        for i in range(N):
            pir[i] = [def_pir]


    def modify_with_spec(spec_bw, pir):
        """
        用指定值修改
        """
        for i in spec_bw:
            print("modifying pir" + i + "...")
            spec_pir = bw_to_pir(spec_bw[i])
            pir[int(i)] = [spec_pir]


    def modify_with_file(bw_csv, pir):
        """
        用csv文件修改
        """
        # 转换csv到dict
        bw_dict = csv_to_dict(bw_csv)
        # 调用指定带宽模式
        modify_with_spec(bw_dict, pir)



    # 对csv文件修改
    print("opening pir.csv...")

    with open("pir.csv", 'r') as csvfile:
        print("successfully opened!")

        reader = csv.reader(csvfile)
        #writer = csv.writer(csvfile)

        print("reading pir...")

        pir = []
        # 读取pir值到数组
        for line in reader:
            pir.append(line)
        
        print("successfully read!")

        # 如果传入def_bw值，对所有pir值更新
        if def_bw != None:
            print("modifying default pir...")
            modify_with_def(def_bw, pir)
            print("done!")

        # 如果传入指定带宽，对相应pir值修改
        if spec_bw != None:
            print("modifying specified pir...")
            modify_with_spec(spec_bw, pir)
            print("done!")

        # 如果传入带宽文件，根据文件进行修改
        if bw_csv != None:
            print("modifying with " + bw_csv + '...')
            modify_with_file(bw_csv, pir)
            print("done!")

        with open("temp.csv", 'w') as tempfile:
            writer = csv.writer(tempfile)
            # 写入临时csv文件
            print("writing temp csv file..")
            for row in pir:
                writer.writerow(row)

            print("successfully writed!")

    # 临时文件覆盖原始文件
    print("overwriting original file...")
    os.remove("pir.csv")
    os.rename("temp.csv", "pir.csv")
    print("successfully overwrited!")

    print("completed!")


# 测试几种工作方式
if __name__ == "__main__":
    print("please select the mode:\n1.modify default bandwith only.\n2.modify specified bandwith only.\n3.modify both.\n4.modify with file.")
    mode = input()
    if mode == '1':
        def_bw = input("please input default bandwith:")
        pir_csv_modify(def_bw = def_bw)
    elif mode == '2':
        spec_bw = input("please input specified bandwith:")
        pir_csv_modify(spec_bw = eval(spec_bw))
    elif mode == '3':
        def_bw = input("please input default bandwith:")
        spec_bw = input("please input specified bandwith:")
        pir_csv_modify(def_bw = def_bw, spec_bw = eval(spec_bw))
    elif mode == '4':
        filename = input("please input file name:")
        pir_csv_modify(bw_csv = filename)
    else:
        print("error mode!")


