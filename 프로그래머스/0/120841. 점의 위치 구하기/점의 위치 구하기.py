def solution(dot):
    point = [['+','+'],['-','+'],['-','-'],['+','-']]
    dot_pos = ['+' if i>0 else '-' for i in dot ]
    return point.index(dot_pos)+1