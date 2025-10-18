letters = 0    # 英文字符（仅a-z,A-Z）
digits = 0     # 数字（仅0-9）
spaces = 0     # 半角空格（' '）
others = 0     # 其他字符（特殊符号，不含中文）

s = input()

for c in s:
    # 英文字符判断（严格匹配大小写字母）
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
        letters += 1
    # 数字判断（仅0-9）
    elif '0' <= c <= '9':
        digits += 1
    # 空格判断（仅半角空格）
    elif c == ' ':
        spaces += 1
    # 其他字符：仅特殊符号（排除中文）
    elif not('\u4e00' <= c <= '\u9fff'):  # 中文范围：\u4e00-\u9fff，排除中文
        others += 1

print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
