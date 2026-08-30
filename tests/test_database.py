from database.db import get_connection

connection = get_connection()
print("数据库连接成功")
connection.close()



