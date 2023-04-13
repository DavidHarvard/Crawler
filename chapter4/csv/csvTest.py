import csv

with open('/home/david/桌面/Crawler/chapter4/csv/data.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['1001','David','22'])
    writer.writerow(['1002','Bob','22'])
    writer.writerow(['1003','Jordan','21'])


#修改列与列之间的分割份符号 此时列于列之间就是以空格为分割副了

with open('/home/david/桌面/Crawler/chapter4/csv/data.csv','a') as csvfile:
    writer = csv.writer(csvfile,delimiter=' ')
    writer.writerow(['id','name','age'])
    writer.writerow(['1001','David','22'])
    writer.writerow(['1002','Bob','22'])
    writer.writerow(['1003','Jordan','21'])