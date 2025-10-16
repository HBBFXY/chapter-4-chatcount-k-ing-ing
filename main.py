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
    # 一次性输出，避免 print 多次导致多余空行
    print(f'英文字符：{eng}\n数字：{num}\n空格：{space}\n其他字符：{other}')

if __name__ == "__main__":
    s = input()
    char_count(s)
