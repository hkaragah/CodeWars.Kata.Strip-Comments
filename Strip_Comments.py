def solution(string,markers):

    reduced = ""
    for line in string.splitlines():
        for char in markers:
            if char in line:
                line = line[:line.find(char)]
        reduced = reduced + line.strip() + "\n"
    return reduced[:-1]
