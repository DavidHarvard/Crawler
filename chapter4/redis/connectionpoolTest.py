from redis import StrictRedis,ConnectionPool

pool = ConnectionPool(host='localhost',port=6379,db=0,password='foobard')
redis=StrictRedis(connection_pool=pool)
