def check_password(s, n):
    if n <= 4:
        return 0
    
    has_digit = False
    has_upper = False
    has_invalid_char = False
    
    for char in s:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char == ' ' or char == '/':
            has_invalid_char = True
    
    if has_digit and has_upper and not has_invalid_char:
        return 1
    else:
        return 0
