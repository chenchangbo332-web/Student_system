"""

用户操作界面

"""

from students.student_manager import StudentManager

def show_mean():
        print(f"{'-' * 30}欢迎来到学生管理系统{'-' * 30}")
        print("1.添加学生信息")
        print("2.查询单个学生信息")
        print("3.查询所有学生信息")
        print("4.修改学生信息")
        print("5.删除学生信息")
        print("6.保存学生信息")
        print("0.退出系统")

def main():
        manager=StudentManager()
        while True:
            show_mean()
            choice=input("请输入要操作的功能对应的数字")
            if choice=="1":     #添加学生
                manager.add_student()

            elif choice=='2':   #查询单个学生
                manager.query_student()

            elif choice=='3':   #查询所有学生信息
                manager.search_all_student()

            elif choice=='4':   #修改学生信息
                manager.modify_student()

            elif choice=='5':   #删除学生信息
                manager.delete_student()

            elif choice=='6':   #保存学生信息
                manager.save_stu()

            elif choice=='0':   #退出系统
                x=input("确认要退出吗？Y/N")
                if x=='Y':
                    break
                    manager.save_stu()
            else:
                print("您输入的数字有误，请重新输入！")


if __name__ =="__main__":
    main()






