def is_valid_parentheses(given:str) ->bool:
    stack = []
    pair_map = {")": "(", "}": "{", "]": "["}

    for char in given:
        if char in pair_map:
            if not stack:
                return False

            required_opener = pair_map[char]
            last_opener = stack.pop()
            if last_opener != required_opener:
                return False
        else:
            stack.append(char)
    return not stack
        
s1 = '()'
s2 = "()[]{}"
s3 = "(]"
s4 = "{[]}"

print(f"'{s1}' is valid: {is_valid_parentheses(s1)}") # Output: True
print(f"'{s2}' is valid: {is_valid_parentheses(s2)}") # Output: True