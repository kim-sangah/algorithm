def solution(babbling):
    count = 0
    for b in babbling:
        for w in ["aya", "ye", "woo", "ma"]:
            b = b.replace(w, " ")
        if b.strip() == '':
            count += 1
    return count