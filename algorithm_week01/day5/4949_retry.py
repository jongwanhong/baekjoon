
while True:
    string = input()
    check = []

    for char in string:
        # if char == '(' or char == '[':
        if char == '(':
            check.append(')')
        elif char == '[':
            check.append(']')

    print(check)
    check.reverse()
    print(check)

    for char in string:
        if char in check:
            check.pop()

    print(check)

    if check == []:
        print('yes')
    else:
        print('no')

    if string == '.':
        break


# while True:
#     bracket = input()
#     if bracket == ".":
#         break
#     bracket_stack = []
#     answer = True

#     for j in bracket:
#         if j == "(" or j == "[":
#             bracket_stack.append(j)

#         elif j == ")":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "(":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break

#         elif j == "]":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "[":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break

#     if answer == True and not bracket_stack:
#         print("yes")
#     else:
#         print("no")