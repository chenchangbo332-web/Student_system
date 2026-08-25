"""

用户操作界面

"""

from students.student_manager import StudentManager


if __name__ == '__main__':
    cms1=StudentManager()
    cms1.add_student()

    def show_mean():
        print("-*30欢迎来到学生管理系统-*30")
        print("1.添加学生信息")
        print("2.查询单个学生信息")
        print("3.查询所有学生信息")
        print("4.修改学生信息")
        print("5.删除学生信息")
        print("0.退出系统")

    def main():

        while True:



