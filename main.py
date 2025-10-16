def char_count(s):
    eng = num = space = other = 0
    for c in s:
        if c.isalpha() and c.isascii():  # 只统计英文字母
            eng += 1
        elif c.isdigit():
            num += 1
        elif c == ' ':
            space += 1
        else:
            other += 1
    print(f'英文字符：{eng}')
    print(f'数字：{num}')
    print(f'空格：{space}')
    print(f'其他字符：{other}')
