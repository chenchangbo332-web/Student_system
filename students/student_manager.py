"""
学生管理类


"""
from students.student import Student


class StudentManager:
    #初始化学生对象
    def __init__(self):
        self.stu_list = [
            Student(20240000, "李四", "男", 18, "2班", "大数据", "13578952456", "2024-09-01"),
            Student(20240001, "张三", "男", 18, "2班", "大数据", "18314542025", "2024-09-01"),
            Student(20240002, "王五", "女", 19, "2班", "大数据", "13678952456", "2024-09-01"),
            Student(20240003, "赵六", "男", 18, "2班", "大数据", "13778952456", "2024-09-01"),
            Student(20240004, "陈晨", "女", 19, "2班", "大数据", "13878952456", "2024-09-01"),
            Student(20240005, "刘洋", "男", 18, "2班", "大数据", "13978952456", "2024-09-01"),
            Student(20240006, "杨帆", "女", 18, "2班", "大数据", "15078952456", "2024-09-01"),
            Student(20240007, "黄敏", "女", 19, "2班", "大数据", "15178952456", "2024-09-01"),
            Student(20240008, "周杰", "男", 18, "2班", "大数据", "15278952456", "2024-09-01"),
            Student(20240009, "吴迪", "男", 19, "2班", "大数据", "15378952456", "2024-09-01"),
            Student(20240010, "徐静", "女", 18, "2班", "大数据", "15578952456", "2024-09-01"),
            Student(20240011, "孙浩", "男", 18, "2班", "大数据", "15678952456", "2024-09-01"),
            Student(20240012, "胡悦", "女", 19, "2班", "大数据", "15778952456", "2024-09-01"),
            Student(20240013, "朱明", "男", 18, "2班", "大数据", "15878952456", "2024-09-01"),
            Student(20240014, "高飞", "男", 19, "2班", "大数据", "15978952456", "2024-09-01"),
            Student(20240015, "林雪", "女", 18, "2班", "大数据", "18078952456", "2024-09-01"),
            Student(20240016, "何超", "男", 18, "2班", "大数据", "18178952456", "2024-09-01"),
            Student(20240017, "郭琳", "女", 19, "2班", "大数据", "18278952456", "2024-09-01"),
            Student(20240018, "马良", "男", 18, "2班", "大数据", "18378952456", "2024-09-01"),
            Student(20240019, "唐欣", "女", 19, "2班", "大数据", "18478952456", "2024-09-01"),
        ]

    #添加学生信息
    def add_student(self):
        student_id=input("请输入学生ID").strip()
        for stu in self.stu_list:
            if student_id==str(stu.student_id):
                print(f"学号 {student_id} 已存在，不能重复添加！")
                return

        name=input("请输入学生姓名")
        gender=input("请输入学生性别")
        age=input("请输入学生年龄")
        class_name=input("请输入学生所属班级")
        major=input("请输入学生专业")
        phone=input("请输入学生电话")
        enrollment_date=input("请输入学生入学日期")
        stu=Student(student_id,name, gender,age,class_name,major,phone,enrollment_date)
        self.stu_list.append(stu)
        print(f"添加学生{name}成功")


    #修改学生信息
    def modify_student(self):

        student_name = input("请输入要修改学生的姓名")

        for stu in self.stu_list:
            if stu.name == student_name:
                stu.gender = input('输入新的性别：')
                stu.age = int(input('输入新的年龄：'))
                stu.desc = input('输入新的班级信息：')
                stu.desc = input('输入新的专业信息：')
                stu.phone = input('输入新的手机号：')
                stu.phone = input('输入新的入学日期：')

                print(f"学生{student_name}信息已修改")
                break
            print(f"学生{student_name}未找到！")



    #查询单个学生信息
    def query_student(self):
        student_name = input("请输入要查询学生的姓名")
        for stu in self.stu_list:
            if stu.name == student_name:
                print(stu)
                return
        print(f"学生{student_name}未找到！")

    #根据学号找到学生，找不到就返回None
    def find_student_by_id(self, stu_id=None):
        if stu_id is None:
            stu_id=input("请输入要查询的学生ID")

        for stu in self.stu_list:
            if stu.student_id==stu_id:
                print("查找成功，该学生信息如下:")
                return stu
        print(f"未找到学生ID为{stu_id}的学生,请确认后再查找！")
        return None


    #查询所有学生信息
    def search_all_student(self):
        if len(self.stu_list)==0:
            print("当前未添加学生！ ")
        for stu in self.stu_list:
            print(stu)
            print() #美观，加换行
    #保存学生信息
    def save_stu(self):
        with open("./students/stu_info.txt",'w',encoding='utf-8')as dest_f:
        # 把[学生对象，学生对象，学生对象]写入--->[字典,字典,字典]
            dict_data=[stu.__dict__ for stu in self.stu_list]
        # 9.3把字典列表写入文件
            dest_f.write(str(dict_data))
            print('学生信息保存成功！')

    #加载学生信息
    def load_stu_info(self):
        with open('students/stu_info.txt','r',encoding='utf-8') as src_f:
            stu_list=eval(src_f.read())     #'[字典,字典,字典]'-->[字典,字典,字典]
            if len(stu_list)==0:
                stu_list=[]
            else:
                self.stu_list= [Student(**stu) for stu in stu_list]





    #删除某个学生信息
    def delete_student(self, student_name=None):
        """根据姓名删除学生，成功返回 True，未找到返回 False。"""
        if student_name is None:
            student_name = input("请输入要删除学生的姓名").strip()

        for stu in self.stu_list:
            if stu.name == student_name:
                self.stu_list.remove(stu)
                print(f"学生{student_name}信息已删除")
                return True

        print(f"未找到学生{student_name}的信息，请检查后重新删除！")
        return False



if __name__ == '__main__':
    manager = StudentManager()
    before_count = len(manager.stu_list)
    name = input("请输入要测试删除的学生姓名：").strip()
    deleted = manager.delete_student(name)
    after_count = len(manager.stu_list)

    print(f"删除前数量：{before_count}")
    print(f"删除后数量：{after_count}")
    print(f"删除是否成功：{deleted}")




