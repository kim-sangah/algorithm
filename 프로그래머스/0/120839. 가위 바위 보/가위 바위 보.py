def solution(rsp):
    rsp_dict = {'2':'0', '0':'5', '5':'2'}
    return ''.join(rsp_dict.get(i) for i in rsp)