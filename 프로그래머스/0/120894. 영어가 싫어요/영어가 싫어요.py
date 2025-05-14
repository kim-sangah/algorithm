def solution(numbers):
    num_list = ["zero", "one", "two", "three", "four", 
                "five", "six", "seven", "eight", "nine"]
    
    for num, en in enumerate(num_list):
        numbers = numbers.replace(en, str(num))
            
    return int(numbers)