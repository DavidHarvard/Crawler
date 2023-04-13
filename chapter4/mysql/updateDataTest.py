import pymysql 


data = {
    'id' : '200104122',
    'name' : 'david',
    'age' : '22'
}

db = pymysql.connect(host='localhost',user='root',password='davidis2b',port=3306,db='spiders')
cursor = db.cursor()

table = 'students'
keys = ','.join(data.keys())
values=','.join(['%s'] * len(data))
#update后面需要留一个空格
sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE '.format(table=table,keys=keys,values=values)
update = ','.join(["{key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql,tuple(data.values())*2):
       print('Successful')
       db.commit()
except Exception as e:
    print('Faild',e)
    db.rollback()
db.close()