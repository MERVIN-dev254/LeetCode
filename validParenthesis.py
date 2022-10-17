def validPar(par_str):
    stack = []    
    if par_str[0] == ')' or par_str[0] == '}' or par_str[0] == ']': return False
    if len(par_str) % 2 != 0: return False
    
    openPar = ['(', '{', ']']
    closePar = [')', '{', ']']
    for i in par_str:
        if i in openPar:
            stack.append(i)
        elif i in closePar:
            rel_op = stack.pop()
            
            if i == ')' and rel_op == '(' or i =='}' and rel_op == '{' or i == ']' and rel_op == '[':
                return True
    return False 
            
print(validPar("(){()}"))
            
