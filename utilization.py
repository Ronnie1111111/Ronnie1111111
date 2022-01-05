import os
import csv
from pathlib import Path
list = []
p = Path(r'C:\Users\osullivan\Documents\WeChat Files\wxid_7lghsvhr1e6p21\FileStorage\File\2021-12\result_HLS_noOp\result_noOptimization_bucket')
for file in p.rglob('*.rpt'):
    flag = 'not process'
    with open(file,"r") as f:
        for line in f:
            if "Utilization Estimates" in line:
                flag = "process"
            if "Utilization (%)" in line:
                flag = 'not process'
            if flag == "process" and "Total" in line:
                string1 = line
                
                num_list_new = []   # 新建空列表，用以存储提取的数值
                a = ''   # 将空值赋值给a
                for i in string1:    # 将字符串进行遍历
                    if str.isdigit(i):    # 判断i是否为数字，如果“是”返回True，“不是”返回False
                        a += i   # 如果i是数字格式，将i以字符串格式加到a上
                    else:
                        a += " "  # 如果i不是数字格式，将“ ”（空格）加到a上

                num_list = a.split(" ")  
                
                for i in num_list:  
                    try:  
                        if int(i) > 0:
                            num_list_new.append(int(i))  
                        else:
                            pass     
                    except:
                            pass
    list.append(num_list_new)
    print(file)
    print("num_list is \n", num_list_new)    
    print("list is \n", list)             
'''string1.split('|')
        string1.replace('|', ' ')
        string2 = string1.replace('|', '')
        string3 = string2[0:5] + ',' + string2[24:26] + ',' + string2[30:33] + ',' + string2[36:41] + ',' + string2[42:48]
'''
with open("Utilization_test.csv","a+",newline='') as csvfile:          
    writer = csv.writer(csvfile)
    writer.writerow(["BRAM_18K","DSP48E","FF","LUT"])
    writer.writerows(list)

            
