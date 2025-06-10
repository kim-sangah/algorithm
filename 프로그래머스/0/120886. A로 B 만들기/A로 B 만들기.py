def solution(before, after):
    for a in after:
        before = before.replace(a, " ", 1)
    if before.strip() == '':
        return 1
    else:
        return 0