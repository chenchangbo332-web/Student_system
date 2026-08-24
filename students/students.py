"""

该文件用于记录学生类，学生的属性信息为：学号，姓名，性别，班级，专业，联系电话，入学日期
- student_id：学号
- name：姓名
- gender：性别
- age:年龄
- class_name：班级
- major：专业
- phone：联系电话
- enrollment_date：入学日期
"""

class Student:
    def __init__(self, student_id,name, gender,age,class_name,major,phone,enrollment_date):
        """

        :param student_id: 学号
        :param name: 姓名
        :param gender: 性别
        :param age: 年龄
        :param class_name:班级
        :param major: 专业
        :param phone: 联系电话
        :param enrollment_date:入学日期
        """
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.age = age
        self.class_name = class_name
        self.major = major
        self.phone = phone
        self.enrollment_date = enrollment_date

    def __str__(self):
        return f'学生ID:{self.student_id},学生姓名:{self.name},性别{self.gender},年龄:{self.age},班级:{self.class_name},专业:{self.major},联系电话:{self.phone},入学日期:{self.enrollment_date}'

if __name__ == '__main__':
    s1=Student(202099000000,'lip','男',18,'ai01','ai','130221125874','2020-9-1')
    print(s1)