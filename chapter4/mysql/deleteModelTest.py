import pymysql 




db = pymysql.connect(host='localhost',user='root',password='davidis2b',port=3306,db='spiders')
cursor = db.cursor()


table = 'students'
condition = 'age >= 20'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition =condition)

try:
    cursor.execute(sql)
    print('Successful')
    db.commit()
except:
    print('Faild')
    db.rollback()
db.close()