# Python变量和数据类型练习
# 第二个Python学习项目

print("=== Python变量和数据类型练习 ===\n")

# 1. 基本数据类型
print("1. 基本数据类型：")

# 整数 (Integer)
my_integer = 42
print(f"整数: {my_integer}, 类型: {type(my_integer)}")

# 浮点数 (Float)
my_float = 3.14
print(f"浮点数: {my_float}, 类型: {type(my_float)}")

# 布尔值 (Boolean)
my_boolean = True
print(f"布尔值: {my_boolean}, 类型: {type(my_boolean)}")

# 字符串 (String)
my_string = "Hello Python!"
print(f"字符串: {my_string}, 类型: {type(my_string)}")

# 2. 字符串操作
print("\n2. 字符串操作：")

# 字符串拼接
first_name = "Python"
last_name = "Learner"
full_name = first_name + " " + last_name
print(f"字符串拼接: {full_name}")

# 字符串格式化
age = 25
message = f"我的名字是 {full_name}, 我 {age} 岁了"
print(f"f-string格式化: {message}")

# 字符串长度
print(f"字符串长度: {len(my_string)}")

# 字符串索引和切片
print(f"第一个字符: {my_string[0]}")
print(f"前5个字符: {my_string[:5]}")
print(f"最后5个字符: {my_string[-5:]}")

# 3. 列表 (List)
print("\n3. 列表操作：")

# 创建列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"水果列表: {fruits}, 类型: {type(fruits)}")

# 访问列表元素
print(f"第一个水果: {fruits[0]}")
print(f"最后一个水果: {fruits[-1]}")

# 修改列表元素
fruits[1] = "草莓"
print(f"修改后的列表: {fruits}")

# 添加元素
fruits.append("梨")
print(f"添加后的列表: {fruits}")

# 列表长度
print(f"列表长度: {len(fruits)}")

# 4. 字典 (Dictionary)
print("\n4. 字典操作：")

# 创建字典
student = {
    "name": "张三",
    "age": 20,
    "major": "计算机科学",
    "grade": "大一"
}
print(f"学生信息: {student}, 类型: {type(student)}")

# 访问字典值
print(f"学生姓名: {student['name']}")
print(f"学生年龄: {student.get('age')}")

# 修改字典值
student["age"] = 21
print(f"修改后的学生信息: {student}")

# 添加新键值对
student["city"] = "北京"
print(f"添加后的学生信息: {student}")

# 5. 类型转换
print("\n5. 类型转换：")

# 字符串转整数
str_number = "123"
int_number = int(str_number)
print(f"字符串'{str_number}'转整数: {int_number}, 类型: {type(int_number)}")

# 整数转字符串
int_to_str = str(my_integer)
print(f"整数{my_integer}转字符串: '{int_to_str}', 类型: {type(int_to_str)}")

# 浮点数转整数
float_to_int = int(my_float)
print(f"浮点数{my_float}转整数: {float_to_int}, 类型: {type(float_to_int)}")

# 整数转浮点数
int_to_float = float(my_integer)
print(f"整数{my_integer}转浮点数: {int_to_float}, 类型: {type(int_to_float)}")

# 6. 变量赋值和删除
print("\n6. 变量赋值和删除：")

# 多变量赋值
x, y, z = 1, 2, 3
print(f"多变量赋值: x={x}, y={y}, z={z}")

# 变量交换
a = 5
b = 10
a, b = b, a
print(f"变量交换后: a={a}, b={b}")

# 检查变量是否存在
variable_exists = 'my_integer' in locals()
print(f"变量my_integer是否存在: {variable_exists}")

print("\n=== 练习完成 ===")
print("\n提示: 尝试修改上面的代码，练习使用不同的数据类型和操作！")