def solution(string,markers):

    reduced = ""
    for line in string.splitlines():
        # [char in line for char in markers]
        flag = False
        addition = ""
        for char in markers:
            if char in line:
                addition = line[:line.find(char)]
                flag = False
                break
            else:
                flag = True
        if flag:
            addition = line
        if addition[-1]==" ":
            reduced = reduced + addition[:-1] + "\n"
        else:
            reduced = reduced + addition + "\n"
    return reduced[:-1]
    
