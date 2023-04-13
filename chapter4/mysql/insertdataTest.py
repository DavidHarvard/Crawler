import pymysql 

id = '20010411'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost',user='root',password='davidis2b',port=3306,db='spiders')
cursor = db.cursor()
#直接用格式化符号%ss来构造 有几个value就写几个%ss
sql = 'INSERT INTO students(id,name,ages) valus(%ss,%ss,%ss)'

try:
    cursor.execute(sql(id,user,age))
    #需要执行db对象的commit方法才可以u实现数据插入 这个方法才是真正将语句提交曹数据库中执行的方法
    db.commit()
except:
     db.rollback() 
print('data set insert into table students successfully')
db.close()