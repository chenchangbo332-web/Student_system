"""

班级信息
"""

class class_info:
    #班级属性
    def __init__(self, class_id, class_name, major, grade, head_teacher):
        """

        :param class_id: 班级ID
        :param class_name: 班级名
        :param major: 专业
        :param grade: 年级
        :param head_teacher:班主任
        """
        self.class_id = class_id
        self.class_name = class_name
        self.major = major
        self.grade = grade
        self.head_teacher = head_teacher

    def __str__(self) :
        return f"班级ID:{self.class_id},班级名:{self.class_name},专业:{self.major},班主任:{self.head_teacher}"


