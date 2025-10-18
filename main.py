# 初始化计数器
letters = 0    # 英文字符
digits = 0     # 数字
spaces = 0     # 空格
others = 0     # 其他字符

# 获取输入
s = input()

# 遍历每个字符
for c in s:
    if c.isalpha() and c.encode().isalpha():  # 确保是纯英文字母（排除中文等其他语言字母）
        letters += 1
    elif c.isdigit():
        digits += 1
    elif c == ' ':  # 仅统计半角空格
        spaces += 1
    else:
        others += 1

# 输出结果
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
