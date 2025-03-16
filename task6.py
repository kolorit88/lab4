def bracket_check(string_with_bracket):
    open_brackets = 0
    for bracket in string_with_bracket:
        if bracket == '(':
            open_brackets += 1
        elif bracket == ')':
            open_brackets -= 1

        if open_brackets == -1:
            print("NO")
            return
    if open_brackets == 0:
        print("YES")
        return

    print("NO")


bracket_check("(())(")
bracket_check(")))))((((")
bracket_check("()")
bracket_check("(()()()())")