# 文件操作和异常处理示例
# 这是一个面向Python初学者的文件操作和异常处理练习项目

print("===== 文件操作和异常处理示例 =====")

# 1. 文件写入操作
print("\n1. 文件写入操作")
try:
    # 使用open()函数打开文件，模式为'w'（写入）
    # 如果文件不存在，会自动创建；如果文件已存在，会覆盖原有内容
    with open('example.txt', 'w', encoding='utf-8') as file:
        file.write("这是第一行文本\n")
        file.write("这是第二行文本\n")
        file.write("Python是一种很棒的编程语言！\n")
    print("文件写入成功！")
except Exception as e:
    print(f"写入文件时出错: {e}")

# 2. 文件追加操作
print("\n2. 文件追加操作")
try:
    # 使用模式'a'（追加）打开文件，内容会添加到文件末尾
    with open('example.txt', 'a', encoding='utf-8') as file:
        file.write("这是追加的第一行\n")
        file.write("这是追加的第二行\n")
    print("文件追加成功！")
except Exception as e:
    print(f"追加文件时出错: {e}")

# 3. 文件读取操作
print("\n3. 文件读取操作")

# 3.1 读取整个文件
print("\n3.1 读取整个文件:")
try:
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"读取文件时出错: {e}")

# 3.2 逐行读取文件
print("\n3.2 逐行读取文件:")
try:
    with open('example.txt', 'r', encoding='utf-8') as file:
        print("文件内容（逐行读取）:")
        for line in file:
            # 使用strip()去除每行末尾的换行符和空白字符
            print(f"> {line.strip()}")
except Exception as e:
    print(f"读取文件时出错: {e}")

# 3.3 读取所有行到列表
print("\n3.3 读取所有行到列表:")
try:
    with open('example.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    print("文件行列表:")
    for i, line in enumerate(lines, 1):
        print(f"第{i}行: {line.strip()}")
except Exception as e:
    print(f"读取文件时出错: {e}")

# 4. 异常处理详解
print("\n4. 异常处理详解")

# 4.1 基础的try-except
print("\n4.1 基础的try-except:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误: 除数不能为零！")

# 4.2 捕获多个异常
print("\n4.2 捕获多个异常:")
try:
    # 尝试执行可能出错的代码
    num = int(input("请输入一个数字: "))  # 可能引发ValueError
    result = 10 / num  # 可能引发ZeroDivisionError
    print(f"10 / {num} = {result}")
except ValueError:
    print("错误: 请输入有效的数字！")
except ZeroDivisionError:
    print("错误: 除数不能为零！")

# 4.3 捕获所有异常
print("\n4.3 捕获所有异常:")
try:
    # 这里可能有各种错误
    x = int('abc')
except Exception as e:
    print(f"发生了一个错误: {type(e).__name__} - {e}")

# 4.4 try-except-else-finally结构
print("\n4.4 try-except-else-finally结构:")
try:
    # 尝试执行代码
    num = int(input("请输入一个数字: "))
    result = 10 / num
except ValueError:
    print("错误: 请输入有效的数字！")
except ZeroDivisionError:
    print("错误: 除数不能为零！")
else:
    # 如果没有异常发生，执行这里的代码
    print(f"计算结果: 10 / {num} = {result}")
finally:
    # 无论是否发生异常，都会执行这里的代码
    print("程序执行完成！")

# 5. 创建和使用自定义异常
print("\n5. 创建和使用自定义异常:")

# 定义自定义异常
class NegativeNumberError(Exception):
    """当输入负数时抛出的异常"""
    pass

try:
    num = int(input("请输入一个正数: "))
    if num < 0:
        # 抛出自定义异常
        raise NegativeNumberError("输入了负数！")
    print(f"你输入的正数是: {num}")
except NegativeNumberError as e:
    print(f"自定义异常: {e}")
except ValueError:
    print("错误: 请输入有效的数字！")

# 6. 实践练习：读写用户信息文件
print("\n6. 实践练习：读写用户信息文件")

def save_user_info():
    """保存用户信息到文件"""
    try:
        # 获取用户输入
        name = input("请输入您的姓名: ")
        age = input("请输入您的年龄: ")
        email = input("请输入您的邮箱: ")
        
        # 验证年龄是否为数字
        if not age.isdigit():
            raise ValueError("年龄必须是数字！")
        
        # 写入文件
        with open('user_info.txt', 'w', encoding='utf-8') as file:
            file.write(f"姓名: {name}\n")
            file.write(f"年龄: {age}\n")
            file.write(f"邮箱: {email}\n")
        
        print("用户信息保存成功！")
        
    except ValueError as e:
        print(f"验证错误: {e}")
    except Exception as e:
        print(f"保存用户信息时出错: {e}")

def read_user_info():
    """从文件读取用户信息"""
    try:
        with open('user_info.txt', 'r', encoding='utf-8') as file:
            print("\n用户信息:")
            print(file.read())
    except FileNotFoundError:
        print("错误: 用户信息文件不存在！")
    except Exception as e:
        print(f"读取用户信息时出错: {e}")

# 调用函数测试
print("\n请输入一些用户信息:")
save_user_info()
read_user_info()

# 7. 文件操作高级技巧
print("\n7. 文件操作高级技巧")

# 7.1 使用with语句管理多个文件
print("\n7.1 使用with语句管理多个文件:")
try:
    # 同时打开两个文件
    with open('example.txt', 'r', encoding='utf-8') as source_file, \
         open('copy_example.txt', 'w', encoding='utf-8') as target_file:
        # 复制文件内容
        for line in source_file:
            target_file.write(line)
    print("文件复制成功！")
except Exception as e:
    print(f"复制文件时出错: {e}")

# 7.2 使用os模块进行文件和目录操作
print("\n7.2 使用os模块进行文件和目录操作:")
import os

# 获取当前目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 列出当前目录下的文件和文件夹
print("\n当前目录内容:")
for item in os.listdir(current_dir):
    item_path = os.path.join(current_dir, item)
    if os.path.isfile(item_path):
        print(f"文件: {item}")
    elif os.path.isdir(item_path):
        print(f"目录: {item}")

# 8. 异常处理最佳实践
print("\n8. 异常处理最佳实践")
print("\n异常处理的一些建议:")
print("1. 只捕获你能处理的异常")
print("2. 尽量具体地指定异常类型，而不是捕获所有异常")
print("3. 使用finally确保资源正确释放")
print("4. 合理使用自定义异常提高代码可读性")
print("5. 记录异常信息以便调试")

# 9. 上下文管理器示例
print("\n9. 上下文管理器示例")

# 使用上下文管理器进行文件操作（自动关闭文件）
try:
    with open('example.txt', 'r', encoding='utf-8') as file:
        # 在这里使用文件
        first_line = file.readline()
        print(f"文件第一行: {first_line.strip()}")
    # 退出with块后，文件会自动关闭
    # 即使发生异常，文件也会被正确关闭
except Exception as e:
    print(f"操作文件时出错: {e}")

print("\n文件操作和异常处理示例程序执行完毕！")
print("\n提示：运行此程序后，您可以在当前目录中查看生成的文本文件。")