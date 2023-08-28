def isValid(s: str) -> bool:
    if (len(s) % 2 != 0):
        # If string has odd num chars, not valid
        return False

    if (s.count('(') != s.count(')')) or (s.count('[') != s.count(']')) or (s.count('{') != s.count('}')):
        # Check if equal number of closed and open parentheses
        return False

    bracket_map = {'(':')', '{':'}', '[':']'}
    stack = []

    for i in s:
        if bracket_map.get(i):
            stack.append(i)
        else:
            if (len(stack) == 0):
                return False 
            elif (i != bracket_map[stack[-1]]):
                return False
            else:
                stack.pop()
                  
    return True

if __name__ == '__main__':
    print(isValid('(()]'))