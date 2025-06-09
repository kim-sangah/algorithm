def solution(babbling):
    a = ["aya", "ye", "woo", "ma"]
    count = 0
    for word in babbling:
        for sound in a:
            word = word.replace(sound, " ")
        if word.strip() == '':
            count += 1
    return count