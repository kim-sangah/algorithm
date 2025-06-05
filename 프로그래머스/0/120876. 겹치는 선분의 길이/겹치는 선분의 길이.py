def solution(lines):
    drawn_line = [i for s, e in lines for i in range(s, e)]
    
    overlap_dict = {}
    
    for l in drawn_line:
        if l in overlap_dict: 
            overlap_dict[l] += 1
        else:
            overlap_dict[l] = 1
    
    return sum(1 for c in overlap_dict.values() if c >= 2)