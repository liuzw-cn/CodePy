# 函数和模块示例
# 这是一个面向Python初学者的函数和模块练习项目

# 1. 基本函数定义和调用
print("===== 基本函数定义和调用 =====")
def greet_user():
    """简单的问候函数，无参数无返回值"""
    print("Hello! Welcome to Python functions!")

greet_user()  # 调用函数

# 2. 带参数的函数
def greet_by_name(name):
    """带参数的问候函数"""
    print(f"Hello, {name}! Nice to meet you!")

greet_by_name("Alice")
greet_by_name("Bob")

# 3. 带返回值的函数
def add_numbers(a, b):
    """计算两个数的和并返回结果"""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# 4. 带默认参数的函数
def calculate_total(price, tax_rate=0.08):
    """计算总价，税率有默认值"""
    total = price * (1 + tax_rate)
    return total

print(f"商品价格$100，默认税率总价: ${calculate_total(100):.2f}")
print(f"商品价格$100，税率10%总价: ${calculate_total(100, 0.1):.2f}")

# 5. 带可变参数的函数
def sum_numbers(*args):
    """计算任意数量数字的和"""
    total = 0
    for num in args:
        total += num
    return total

print(f"1 + 2 + 3 = {sum_numbers(1, 2, 3)}")
print(f"10 + 20 + 30 + 40 = {sum_numbers(10, 20, 30, 40)}")

# 6. 带关键字参数的函数
def print_person_info(**kwargs):
    """打印人员信息，参数不固定"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n人员信息:")
print_person_info(name="张三", age=25, city="北京")
print("\n另一个人员信息:")
print_person_info(name="李四", job="工程师", country="中国")

# 7. 局部变量和全局变量
print("\n===== 局部变量和全局变量 =====")
global_var = "我是全局变量"

def test_scope():
    local_var = "我是局部变量"
    print(f"函数内访问局部变量: {local_var}")
    print(f"函数内访问全局变量: {global_var}")
    
    # 使用global关键字修改全局变量
    global global_var
    global_var = "全局变量被修改了"

test_scope()
print(f"函数外访问全局变量: {global_var}")
# print(local_var)  # 这行会报错，因为local_var是局部变量

# 8. 函数嵌套
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# 创建一个闭包
add_five = outer_function(5)
print(f"5 + 10 = {add_five(10)}")

# 9. Lambda表达式（匿名函数）
print("\n===== Lambda表达式 =====")
multiply = lambda a, b: a * b
print(f"3 * 4 = {multiply(3, 4)}")

# Lambda表达式常用于排序
tuples = [(1, 'z'), (2, 'a'), (3, 'b')]
tuples.sort(key=lambda x: x[1])  # 按第二个元素排序
print(f"按字母排序后的列表: {tuples}")

# 10. 模块导入示例
print("\n===== 模块导入示例 =====")
# 导入Python内置模块
import math
print(f"π的值: {math.pi}")
print(f"2的平方根: {math.sqrt(2)}")

# 从模块导入特定函数
from random import randint, choice
print(f"生成1-100的随机数: {randint(1, 100)}")
colors = ['红', '绿', '蓝', '黄']
print(f"随机选择一个颜色: {choice(colors)}")

# 11. 创建自己的模块
print("\n===== 创建自己的模块 =====")
# 注意：要运行这段代码，你需要创建一个名为my_math.py的文件
# 以下是如何在另一个文件中使用该模块的示例代码
'''
# 在my_math.py文件中
# def multiply_numbers(a, b):
#     return a * b
# 
# def subtract_numbers(a, b):
#     return a - b

# 然后在这个文件中可以这样导入
# import my_math
# result = my_math.multiply_numbers(4, 5)
'''

# 12. 递归函数示例
print("\n===== 递归函数示例 =====")
def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"5的阶乘: {factorial(5)}")

# 13. 函数文档字符串
def square_area(side_length):
    """
    计算正方形的面积
    
    参数:
        side_length (float): 正方形的边长
        
    返回:
        float: 正方形的面积
    """
    return side_length ** 2

# 打印函数的文档字符串
print("\n函数文档字符串:")
print(square_area.__doc__)

# 14. 函数类型注解（Python 3.5+）
def greet_with_type(name: str, age: int = 0) -> str:
    """带类型注解的函数"""
    if age > 0:
        return f"Hello, {name}! You are {age} years old."
    else:
        return f"Hello, {name}!"

print(greet_with_type("Charlie"))
print(greet_with_type("David", 30))

# 15. 实践练习：简单的计算器函数
def calculator(num1, num2, operation):
    """
    简单的计算器函数
    
    参数:
        num1: 第一个数字
        num2: 第二个数字
        operation: 操作类型 ('add', 'subtract', 'multiply', 'divide')
        
    返回:
        计算结果
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "错误: 除数不能为零!"
        return num1 / num2
    else:
        return "错误: 不支持的操作!"

print("\n===== 简易计算器 =====")
print(f"10 + 5 = {calculator(10, 5, 'add')}")
print(f"10 - 5 = {calculator(10, 5, 'subtract')}")
print(f"10 * 5 = {calculator(10, 5, 'multiply')}")
print(f"10 / 5 = {calculator(10, 5, 'divide')}")
print(f"10 / 0 = {calculator(10, 0, 'divide')}")
print(f"未知操作: {calculator(10, 5, 'power')}")

print("\n函数和模块示例程序执行完毕！")