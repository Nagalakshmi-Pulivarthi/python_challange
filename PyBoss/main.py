import os
import csv
EmpId=[]
Name=[]
new_list=[]
new_name=["  " , " "]
DOB=[]
SSN=[]
State=[]
csvpath=os.path.join("../PyBoss","employeetest.csv")
with open(csvpath,newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
         EmpId.append(row[0])
         Name.append(row[1])
         new_name= row[1].split(" ")[0]
         
         new_list.append(new_name[0])

         #myList = [i.split('\t')[0] for i in myList] 
         # newList.append(i.split('\t')[0])
   # print(EmpId)
   # print(Name)
    print(new_list)