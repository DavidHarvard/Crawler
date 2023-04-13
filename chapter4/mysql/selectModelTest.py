import pymysql

db = pymysql.connect(host='localhost',user='root',password='davidis2b',port=3306,db='spiders')
cursor = db.cursor()


table = 'students'

sql = 'SELECT * FROM students '
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one = cursor.fetchone()
    print('One:' , one)
    results = cursor.fetchall()
    print('Results:',results)
    print('Results type:',type(results))
    for row in results:
        print(row)
except:
    print('Error')

#更加推荐的方式
sql = 'SELECT * FROM students '
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    row = cursor.fetchall
    while row:
        print('Row:' , row)
        row = cursor.fetchone()
except:
    print('Error')