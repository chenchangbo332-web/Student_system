"""

用户操作界面

"""

from students.student_manager import StudentManager

def show_menu():
    print(f"{'-' * 30}欢迎来到学生管理系统{'-' * 30}")
    print("1.学生管理")
    print("2.班级管理")
    print("0.退出系统")


def show_stu_menu():
        print(f"{'-' * 30}欢迎来到学生管理系统{'-' * 30}")
        print("1.添加学生信息")
        print("2.查询单个学生信息")
        print("3.查询所有学生信息")
        print("4.修改学生信息")
        print("5.删除学生信息")
        print("6.保存学生信息")
        print("9.返回上一级")
        print("0.退出系统")

def stu_manager():
    manager = StudentManager()
    manager.load_stu_info()

    while True:

        show_stu_menu()
        input_num2 = input("请输入要操作的功能对应的数字")
        if input_num2=="1":     #添加学生
            manager.add_student()

        elif input_num2=='2':   #查询单个学生
            manager.query_student()

        elif input_num2=='3':   #查询所有学生信息
            manager.search_all_student()

        elif input_num2=='4':   #修改学生信息
            manager.modify_student()

        elif input_num2=='5':   #删除学生信息
            manager.delete_student()

        elif input_num2=='6':   #保存学生信息
            manager.save_stu()

        elif input_num2=="9":   #返回上一级
            manager.save_stu()
            break

        else:
            print("您输入的数字有误，请重新输入！")

#班级模块管理
def classes_manger():
    pass

def main():

    while True:
        #展示菜单
        show_menu()
        input_num=input("请输入要操作的数字！")
        if input_num=="1":      #学生管理
            stu_manager()

        elif input_num=="2":    #班级管理
            classes_manger()

        elif input_num=="0":    #退出系统
            x = input("确认要退出吗？Y/N")
            if x == 'Y':
                break
            print("已退出学生管理系统")
            break
        else:
            print("输入有误，请重新输入！")




if __name__ =="__main__":
    main()






