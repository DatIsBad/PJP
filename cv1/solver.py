#checker finds if list is valid
def checker( math_list ):   
    #size must be 3+
    if len(math_list) <=2:    
        return -1
    
    #check first and last value if is number or bracket
    if type( math_list[0] ) != int:
        if math_list[0] != '(':
            return -1
    if type( math_list[len(math_list)-1] ) != int:
        if math_list[len(math_list)-1] != ')':
            return -1


    #chars must be in ['(', ')', '+', '-', '*', '/']
    for item in math_list:
        if type(item) != int:
            if item not in ['(', ')', '+', '-', '*', '/']:
                return -1

    #check if number of brackets are even
    bracket1=0
    bracket2=0
    for item in math_list:
        if item == '(':
            bracket1 += 1 
        if item == ')':
            bracket2 += 1 
    if bracket1 != bracket2:
        return -1
    
    #check repeating of types
    for i in range(len(math_list) - 1):
        if type(math_list[i]) == type(math_list[i + 1]):
            if math_list[i] == "(":
                return -1
            elif math_list[i+1] == ")":
                return -1
            elif math_list[i+1] not in "()" and math_list[i] not in "()":
                return -1
            

    return 1


#****************************************************************
#fild brackets to later seperate them and process them first
def find_brackets(math_list):
    bracket1=-1
    bracket2=-1
    
    #check for brackets
    for i in range(len(math_list)):
        if math_list[i] == '(':
            bracket1 = i
        elif math_list[i] == ')':
            bracket2 = i
            break
    
    #if brackets found, process them first
    if bracket1 != -1:
        sublist = math_list[(bracket1 + 1) : (bracket2)]
        new_list = math_list[:(bracket1)] + splitter(sublist) + math_list[(bracket2+1):]
        return find_brackets(new_list)

    #else process rest
    else:
        return splitter(math_list)
    


#****************************************************************
def splitter(math_list): 
    #check for *, / to give them priority first
    #on default, first pair of numbers have priority
    priority = 1
    for i in range(len(math_list)):
        if math_list[i] == '*' or math_list[i] == '/':
            priority = i
            break
    
    #if list is too long, first process pair of numbers that are given priority
    if len(math_list) > 3:
        sublist = math_list[(priority-1):(priority+2)]
        value = [do_math(sublist)]
        new_list = math_list[:(priority-1)] + value + math_list[(priority+2):]

        #print(f"Value processed {value}; processed list {new_list}")
    else:
        return [do_math(math_list)]
    
        
    return splitter(new_list)


#****************************************************************
def do_math(smallmath_list):
    print(smallmath_list)
    if smallmath_list[1] == '+':
        return smallmath_list[0] + smallmath_list[2]
    
    elif smallmath_list[1] == '-':
        return smallmath_list[0] - smallmath_list[2]
    
    elif smallmath_list[1] == '*':
        return smallmath_list[0] * smallmath_list[2]
    
    elif smallmath_list[1] == '/':
        return smallmath_list[0] / smallmath_list[2]
    
    return 0


#****************************************************************
#change user_innput to list; seperating numbers with symbols
def to_list(user_input:str) -> list:   
    math_list = []
    number = ""
    numbers_list = [str(num) for num in range(0,10)]

    for i in range(len(user_input)):
        if user_input[i] in numbers_list:   
            number += user_input[i]

        else:
            if number.isdigit():
                math_list.append(int(number))
            
            math_list.append(user_input[i])
            number = ""

    if number.isdigit():
        math_list.append(int(number))
    #print(math_list)
    return math_list


#****************************************************************
def solve(user_input:str):
    user_input = user_input.replace(' ', '')   #remove all spaces
    math_list = to_list(user_input)
    if checker(math_list) != 1:
        print("ERROR")
        return
    


    print(f'final value is {find_brackets(math_list)}\n')



