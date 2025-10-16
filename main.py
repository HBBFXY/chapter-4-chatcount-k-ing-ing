# 定义计数器变量
english_count = 0  # 英文字符数量
digit_count = 0    # 数字数量
space_count = 0    # 空格数量
other_count = 0    # 其他字符数量

# 获取用户输入的一行字符
input_str = input("请输入一行字符：")

# 遍历每个字符进行判断和计数
for char in input_str:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        english_count += 1
    elif '0' <= char <= '9':
        digit_count += 1
    elif char == ' ':
        space_count += 1
    else:
        other_count += 1

# 按照指定格式输出结果
print(f"英文字符: {english_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
