import pymysql


def get_connection():
    """
    创建并返回一个MySQL数据库连接
    :return:
    """
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database='student_system',
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

