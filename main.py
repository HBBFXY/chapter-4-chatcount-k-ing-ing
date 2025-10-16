def char_count(s):
    eng = num = space = other = 0
    for c in s:
        if c.isalpha() and c.isascii():
            eng += 1
        elif c.isdigit():
            num += 1
        elif c == ' ':
            space += 1
        else:
            other += 1
    return "英文字符：{0}\n数字：{1}\n空格：{2}\n其他字符：{3}".format(eng, num, space, other)
