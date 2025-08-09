def solution(chicken):
    s_chicken = 0
    
    while chicken >= 10:
        service = chicken//10
        s_chicken += service
        chicken = service + chicken%10
        
    return s_chicken