import token_value as tv

def to_list(user_input:str):
    values_list = []
    value = ""
    is_id = False

    #insert all datas into list
    for i in range(len(user_input)):
        if user_input[i] != ' ':

            #detect comment, if detected end processing line
            if user_input[i] == '/' and (len(user_input) - 1) > i:
                if user_input[i+1] == '/':
                    break

            value += user_input[i]

        elif user_input[i] == ' ' and value != "":
            values_list.append(value)
            value = ""
            
    #if value still contains something, add to list
    if value != "":
        values_list.append(value)
        value = ""

    print(f"values_list: {values_list}")


    new_list = []
    for i in range(len(values_list)):
        new_list += check_val(values_list[i]) 


    for item in new_list:
        print(item)

def check_val(value:str):
    result = []
    saved_value = ""

    #check if it is part of keywords
    if value == "div" or value == "mov":
        return [tv.Token("KEY", value)]

    #check each char in value (cannot be keyword)
    for i in range(len(value)):

        #if current value is delimeter ('(', ')' and ';') or operator ('+', '-', '*' and '/') 
        #append saved value and current value into result list
        if(value[i] in ['+', '-', '*', '/', '(', ')', ';']):
            
            #check if saved value is empty, if not it will get appended into result list
            if saved_value != "":
                #convert it into number if it is a number
                if saved_value.isdigit(): 
                    result.append(tv.Token("NUM", int(saved_value)))

                #is ID
                else:   
                    result.append(tv.Token("ID", saved_value))
                saved_value = ""


            #is operator
            if value[i] in ['+', '-', '*', '/']: 
                result.append(tv.Token("OP", value[i]))

            #is delimiter
            else:       
                result.append(tv.Token("DEL", value[i]))
        
        #add char into saved value
        else:
            saved_value += value[i]


    #if saved value was not added into list, add it now
    if saved_value != "":
        #convert it into number if it is a number
        if saved_value.isdigit(): 
            result.append(tv.Token("NUM", int(saved_value)))

        #is ID
        else:   
            result.append(tv.Token("ID", saved_value))
        saved_value = ""

    return result



def solve(user_input:str):
    #user_input = user_input.replace(' ', '')
    newlist = to_list(user_input)