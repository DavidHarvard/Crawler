import pymysql 


data = {
    'id' : '20010411',
    'name' : 'david',
    'position' : 'where'
}

db = pymysql.connect(host='localhost',user='root',password='davidis2b',port=3306,db='spiders')
cursor = db.cursor()
#这个字典的长度是3
print(len(data))

table = 'students'
keys = ','.join(data.keys())
values=','.join(['%s'] * len(data))
sql = 'INSERT INTO {table} ({keys}) VALUES({values})'.format(table=table,keys=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
       print('Successful')
       db.commit()
except:
    print('Faild')
    db.rollback()
db.close()