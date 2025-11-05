# Python条件语句和循环结构练习
# 第三个Python学习项目

print("=== Python条件语句和循环结构练习 ===\n")

# 1. 条件语句 (if-elif-else)
print("1. 条件语句示例：")

# 简单if语句
age = 20
print(f"\n年龄: {age}")

if age >= 18:
    print("你已经成年了！")

# if-else语句
if age < 18:
    print("你还未成年。")
else:
    print("你已经是成年人了。")

# if-elif-else语句
if age < 13:
    print("你是儿童。")
elif age < 18:
    print("你是青少年。")
elif age < 60:
    print("你是成年人。")
else:
    print("你是老年人。")

# 2. 逻辑运算符
print("\n2. 逻辑运算符示例：")

x = 10
y = 5
z = 15

# and运算符 (两个条件都为True才为True)
if x > y and x < z:
    print(f"x({x}) 大于 y({y}) 并且小于 z({z})")

# or运算符 (至少一个条件为True就为True)
if x > y or x > z:
    print(f"x({x}) 大于 y({y}) 或者大于 z({z})")

# not运算符 (取反)
if not(x == y):
    print(f"x({x}) 不等于 y({y})")

# 3. 比较运算符
print("\n3. 比较运算符示例：")

print(f"x == y: {x == y}")  # 等于
print(f"x != y: {x != y}")  # 不等于
print(f"x > y: {x > y}")    # 大于
print(f"x < y: {x < y}")    # 小于
print(f"x >= y: {x >= y}")  # 大于等于
print(f"x <= y: {x <= y}")  # 小于等于

# 4. while循环
print("\n4. while循环示例：")

count = 1
print("\n倒计时:")
while count <= 5:
    print(f"数字: {count}")
    count += 1

# while循环与条件结合
guess = 0
secret_number = 7
attempts = 0

print("\n猜数字游戏！")
print("我想了一个1到10之间的数字，你能猜对吗？")
print("(示例中已设置答案为7，将循环5次)")

while guess != secret_number and attempts < 5:
    attempts += 1
    print(f"\n尝试 {attempts}/5")
    # 在实际运行时，可以取消下面一行的注释并注释掉下一行
    # guess = int(input("请输入你的猜测: "))
    guess = attempts  # 仅用于演示，实际运行时删除此行
    print(f"你的猜测是: {guess}")
    
    if guess < secret_number:
        print("太小了！")
    elif guess > secret_number:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")

if guess != secret_number:
    print(f"\n游戏结束，正确答案是: {secret_number}")

# 5. for循环
print("\n5. for循环示例：")

# 遍历字符串
word = "Python"
print(f"\n遍历字符串 '{word}':")
for char in word:
    print(char)

# 遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄", "草莓"]
print(f"\n遍历水果列表: {fruits}")
for fruit in fruits:
    print(f"- {fruit}")

# 使用range()函数
print("\n使用range(5)循环:")
for i in range(5):
    print(f"数字: {i}")

print("\n使用range(2, 8)循环:")
for i in range(2, 8):
    print(f"数字: {i}")

print("\n使用range(1, 10, 2)循环 (步长为2):")
for i in range(1, 10, 2):
    print(f"奇数: {i}")

# 6. 嵌套循环
print("\n6. 嵌套循环示例：")

# 九九乘法表
print("\n九九乘法表:")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} × {i} = {i*j}", end="  ")
    print()  # 换行

# 7. 控制循环的语句
print("\n7. 控制循环的语句示例：")

# break语句 (跳出循环)
print("\n使用break跳出循环:")
for i in range(1, 11):
    if i == 6:
        print(f"当i={i}时，使用break跳出循环")
        break
    print(f"i = {i}")

# continue语句 (跳过当前迭代，继续下一次循环)
print("\n使用continue跳过特定迭代:")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"跳过偶数: {i}")
        continue
    print(f"奇数: {i}")

# 8. 综合练习：判断素数
print("\n8. 综合练习：判断素数")

number = 17
print(f"\n判断数字 {number} 是否为素数:")

if number > 1:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{number} 是素数")
    else:
        print(f"{number} 不是素数")
else:
    print(f"{number} 不是素数")

print("\n=== 练习完成 ===")
print("\n提示: 尝试修改上面的代码，练习使用不同的条件和循环结构！")
print("例如：修改猜数字游戏的答案，或者实现一个简单的菜单选择程序。")