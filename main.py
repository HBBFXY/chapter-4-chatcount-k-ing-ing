input_str = input()

# 初始化计数器
letter_count = 0   # 英文字母
digit_count = 0    # 数字
space_count = 0    # 空格
other_count = 0    # 其他字符

# 精确字符分类逻辑
for char in input_str:
    if char in ' \t\n\r':  # 扩展空格检测（包括制表符等空白字符）
        space_count += 1
    elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letter_count += 1
    elif '0' <= char <= '9': 
        digit_count += 1
    else:
        other_count += 1  # 包含中文/特殊符号等

# 严格按格式输出
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
