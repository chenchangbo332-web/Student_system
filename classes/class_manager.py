"""
以后我们希望班级有自己的编号、专业、年级和班主任，学生只关联班级。这样课程和成绩才能继续扩展。

"""
from classes.class_info import class_info


class Class_Manger:

    def __init__(self):
        self.class_list=[]

    #添加班级
    def add_class(self):
        class_id=input("请输入班级ID")
        if self.class_list.class_id==class_id:
            print("该班级已存在，请检查后重新输入")
            return
        class_name=input("请输入班级名")
        major=input("请输入班级对应的专业")
        grade=input("请输入班级对应的年级")
        head_teach=input("请输入负责班级的班主任")

    #查询单个班级
    def query_class(self):
        pass

    #查询全部班级
    def search_all_class(self):
        pass

    #修改班级
    def modify_class(self):
        pass

    #删除班级
    def delete_class(self):
        pass

