def count_char_types(s):
    eng_count = 0
    num_count = 0
    space_count = 0
    other_count = 0
    for c in s:
        if c.isalpha() and (ord(c) < 128):  # 仅统计ASCII英文字母
            eng_count += 1
        elif c.isdigit():
            num_count += 1
        elif c == ' ':
            space_count += 1
        else:
            other_count += 1
    return eng_count, num_count, space_count, other_count
