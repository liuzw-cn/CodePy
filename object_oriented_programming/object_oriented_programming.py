# 面向对象编程示例
# 这是一个面向Python初学者的面向对象编程练习项目

print("===== 面向对象编程示例 =====")

# 1. 基本的类定义和实例化
print("\n1. 基本的类定义和实例化")

class Person:
    """人类的基本类"""
    
    # 类变量（所有实例共享）
    species = "Human"
    
    # 初始化方法（构造函数）
    def __init__(self, name, age):
        # 实例变量（每个实例私有）
        self.name = name
        self.age = age
    
    # 实例方法
    def introduce(self):
        """介绍自己"""
        print(f"你好，我是{self.name}，今年{self.age}岁。")
    
    # 类方法
    @classmethod
    def get_species(cls):
        """获取物种信息"""
        return cls.species

# 创建实例
person1 = Person("张三", 25)
person2 = Person("李四", 30)

# 访问实例变量
print(f"person1的名字: {person1.name}")
print(f"person2的年龄: {person2.age}")

# 调用实例方法
person1.introduce()
person2.introduce()

# 访问类变量
print(f"人类物种: {Person.species}")
print(f"person1的物种: {person1.species}")

# 调用类方法
print(f"通过类方法获取物种: {Person.get_species()}")

# 2. 继承
print("\n2. 继承")

# 父类
class Animal:
    """动物类（父类）"""
    
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
        
    def make_sound(self):
        """发出声音（父类方法）"""
        print("一些动物的声音")
    
    def describe(self):
        """描述动物"""
        print(f"这是一只{self.name}，生活在{self.habitat}。")

# 子类 - 继承自Animal
class Dog(Animal):
    """狗类（子类）"""
    
    def __init__(self, name, breed):
        # 调用父类的初始化方法
        super().__init__(name, "陆地")
        # 子类特有的属性
        self.breed = breed
    
    # 重写父类方法
    def make_sound(self):
        """狗发出的声音"""
        print("汪汪汪！")
    
    # 子类特有方法
    def fetch(self):
        """狗的特有动作"""
        print(f"{self.name}正在捡球！")

# 另一个子类
class Fish(Animal):
    """鱼类（子类）"""
    
    def __init__(self, name, water_type):
        super().__init__(name, "水中")
        self.water_type = water_type
    
    def make_sound(self):
        """鱼发出的声音"""
        print("咕嘟咕嘟...")
    
    def swim(self):
        """鱼的特有动作"""
        print(f"{self.name}在{self.water_type}中游泳！")

# 创建子类实例
dog = Dog("小白", "金毛")
fish = Fish("金鱼", "淡水")

# 访问从父类继承的方法
dog.describe()
fish.describe()

# 调用重写的方法
dog.make_sound()
fish.make_sound()

# 调用子类特有方法
dog.fetch()
fish.swim()

# 3. 多态
print("\n3. 多态")

# 多态示例：同样的方法在不同类中表现不同
def animal_sound(animal):
    """让动物发出声音"""
    animal.make_sound()

print("多态演示:")
animal_sound(dog)  # 传递Dog实例
animal_sound(fish)  # 传递Fish实例

# 4. 封装
print("\n4. 封装")

class BankAccount:
    """银行账户类（封装示例）"""
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # 公共属性
        self.__balance = balance  # 私有属性（使用双下划线开头）
    
    # 公共方法用于访问私有属性（getter）
    def get_balance(self):
        """获取余额"""
        return self.__balance
    
    # 公共方法用于修改私有属性（setter）
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            print(f"存款成功！当前余额: {self.__balance}")
        else:
            print("存款金额必须大于0！")
    
    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"取款成功！当前余额: {self.__balance}")
        else:
            print("取款金额无效或余额不足！")

# 创建银行账户实例
account = BankAccount("张三", 1000)

# 通过公共方法访问和修改私有属性
print(f"账户持有人: {account.account_holder}")
print(f"当前余额: {account.get_balance()}")

account.deposit(500)
account.withdraw(300)

# 尝试直接访问私有属性（会失败，Python会名称修饰）
# print(account.__balance)  # 这行代码会引发错误

# 5. 组合
print("\n5. 组合")

class Engine:
    """发动机类"""
    
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        """启动发动机"""
        print(f"{self.horsepower}马力的发动机启动了！")

class Car:
    """汽车类（包含发动机对象）"""
    
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine  # 组合：Car包含Engine对象
    
    def start(self):
        """启动汽车"""
        print(f"启动{self.brand} {self.model}...")
        self.engine.start()  # 调用发动机的方法

# 创建发动机实例
engine = Engine(200)

# 创建汽车实例，将发动机对象组合进去
car = Car("丰田", "卡罗拉", engine)

# 使用组合后的对象
car.start()

# 6. 特殊方法（魔术方法）
print("\n6. 特殊方法（魔术方法）")

class Rectangle:
    """矩形类（演示特殊方法）"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # 特殊方法：__str__ - 打印对象时调用
    def __str__(self):
        return f"矩形(宽={self.width}, 高={self.height})"
    
    # 特殊方法：__repr__ - 交互式环境中显示对象时调用
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    # 特殊方法：__add__ - 实现加法运算符
    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        return NotImplemented
    
    # 特殊方法：__eq__ - 实现相等比较
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False
    
    # 计算面积
    def area(self):
        return self.width * self.height

# 创建矩形实例
rect1 = Rectangle(5, 3)
rect2 = Rectangle(2, 4)

# 测试特殊方法
print(f"打印rect1: {rect1}")  # 调用__str__
print(f"添加两个矩形: {rect1 + rect2}")  # 调用__add__
print(f"rect1 == rect2: {rect1 == rect2}")  # 调用__eq__
print(f"rect1的面积: {rect1.area()}")

# 7. 静态方法
print("\n7. 静态方法")

class Calculator:
    """计算器类（演示静态方法）"""
    
    @staticmethod
    def add(a, b):
        """静态方法：加法"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """静态方法：乘法"""
        return a * b

# 调用静态方法（无需创建实例）
sum_result = Calculator.add(5, 3)
mul_result = Calculator.multiply(4, 6)

print(f"5 + 3 = {sum_result}")
print(f"4 * 6 = {mul_result}")

# 8. 属性装饰器
print("\n8. 属性装饰器")

class Circle:
    """圆形类（演示属性装饰器）"""
    
    def __init__(self, radius):
        self._radius = radius  # 单下划线表示受保护的属性
    
    # 使用@property装饰器定义getter
    @property
    def radius(self):
        """获取半径"""
        print("获取半径...")
        return self._radius
    
    # 使用@radius.setter装饰器定义setter
    @radius.setter
    def radius(self, value):
        """设置半径"""
        if value > 0:
            print(f"设置半径为{value}...")
            self._radius = value
        else:
            print("半径必须大于0！")
    
    # 计算属性：面积
    @property
    def area(self):
        """计算面积"""
        import math
        return math.pi * self._radius ** 2

# 创建圆形实例
circle = Circle(5)

# 使用属性装饰器
print(f"圆形半径: {circle.radius}")  # 调用radius getter
circle.radius = 10  # 调用radius setter
print(f"修改后的半径: {circle.radius}")
print(f"圆形面积: {circle.area}")  # 调用area属性方法

# 9. 抽象基类
print("\n9. 抽象基类")

from abc import ABC, abstractmethod

class Shape(ABC):
    """形状抽象基类"""
    
    @abstractmethod
    def area(self):
        """计算面积的抽象方法"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长的抽象方法"""
        pass

class Square(Shape):
    """正方形类（实现抽象基类）"""
    
    def __init__(self, side):
        self.side = side
    
    def area(self):
        """实现面积计算方法"""
        return self.side ** 2
    
    def perimeter(self):
        """实现周长计算方法"""
        return 4 * self.side

# 不能直接实例化抽象基类
# shape = Shape()  # 这行会引发错误

# 创建实现类的实例
square = Square(5)
print(f"正方形面积: {square.area()}")
print(f"正方形周长: {square.perimeter()}")

# 10. 实践练习：学生管理系统
print("\n10. 实践练习：学生管理系统")

class Student:
    """学生类"""
    
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []  # 学生选修的课程列表
    
    def enroll(self, course):
        """学生选修课程"""
        if course not in self.courses:
            self.courses.append(course)
            print(f"学生{self.name}已成功选修{course}课程！")
        else:
            print(f"学生{self.name}已经选修了{course}课程！")
    
    def display_info(self):
        """显示学生信息"""
        print(f"学号: {self.student_id}")
        print(f"姓名: {self.name}")
        print(f"年龄: {self.age}")
        print(f"选修课程: {', '.join(self.courses) if self.courses else '暂无'}")

class StudentManager:
    """学生管理系统类"""
    
    def __init__(self):
        self.students = {}  # 使用字典存储学生，键为学号
    
    def add_student(self, student):
        """添加学生"""
        if student.student_id not in self.students:
            self.students[student.student_id] = student
            print(f"成功添加学生: {student.name}（学号: {student.student_id}）")
        else:
            print(f"学号{student.student_id}的学生已存在！")
    
    def find_student(self, student_id):
        """查找学生"""
        return self.students.get(student_id)
    
    def display_all_students(self):
        """显示所有学生信息"""
        if not self.students:
            print("当前没有学生信息！")
        else:
            print("\n所有学生信息:")
            for student in self.students.values():
                print(f"\n----- 学生信息 -----")
                student.display_info()

# 测试学生管理系统
manager = StudentManager()

# 创建学生实例
student1 = Student("2023001", "张三", 20)
student2 = Student("2023002", "李四", 21)

# 添加学生到系统
manager.add_student(student1)
manager.add_student(student2)

# 学生选修课程
student1.enroll("数学")
student1.enroll("英语")
student2.enroll("计算机科学")

# 显示所有学生信息
manager.display_all_students()

print("\n面向对象编程示例程序执行完毕！")
print("\n提示：本示例涵盖了面向对象编程的核心概念：类、对象、继承、多态、封装、组合、特殊方法、装饰器和抽象基类等。")