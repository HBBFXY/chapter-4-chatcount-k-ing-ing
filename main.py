# 初始化计数器
letters = 0    # 英文字符
digits = 0     # 数字
spaces = 0     # 空格
others = 0     # 其他字符

# 获取输入
s = input()

# 遍历每个字符
for c in s:
    # 英文字符判断（仅a-z,A-Z）
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
        letters += 1
    # 数字判断（仅0-9）
    elif '0' <= c <= '9':
        digits += 1
    # 空格判断（仅单个空格）
    elif c == ' ':
        spaces += 1
    # 其他字符
    else:
        others += 1

# 输出结果
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
