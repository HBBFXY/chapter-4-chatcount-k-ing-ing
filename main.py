def char_count(s):
    eng, num, space, other = 0, 0, 0, 0
    for c in s:
        if c.isalpha() and ord(c) < 128:
            eng += 1
        elif c.isdigit():
            num += 1
        elif c == ' ':
            space += 1
        else:
            other += 1
    return f'英文字符：{eng}\n数字：{num}\n空格：{space}\n其他字符：{other}'
