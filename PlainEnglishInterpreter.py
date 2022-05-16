from curses.ascii import isalpha, isdigit
import re
import os

def dropFloat(val):
    if (val % 1) == 0:
        return int(val)
    else:
        return val

def numerizeTokens(list):
    i = 0
    for x in list:
        if x.isnumeric():
            list[i] = float(list[i])
            list[i] = dropFloat(list[i])
        i += 1
    return list


# splitting the files into various tokens
def SplitTokens(line):
    pattern = re.compile('''((?:[^ "']|"[^"]*"|'[^']*')+)''')
    line = line.replace('(', ' ( ')
    line = line.replace(',', ' , ')
    line = line.replace(')', ' ) ')
    tokenList = pattern.split(line)[1::2]
    tokenList = numerizeTokens(tokenList)
    if(tokenList[len(tokenList)-1]) == '\n':
        tokenList.pop(len(tokenList)-1)
    return tokenList 

# put the file name here
fp = open("Program1.pe", "r")

tokens = []
for line in fp.readlines():
    tokens = tokens + SplitTokens(line)

ind = 0
a = []
flag1 = 1
flag2 = 1
i = 0
exec1 = 0
exec2 = 0

# implementation of the various functions of PlainEnglish
while i < len(tokens):
    
    if (tokens[i] == "Declare"):
        if(tokens[i+2] == "bool"):
            a.append(tokens[i+4])
            ind = ind + 1
            print("Declared: " + a[ind - 1])
            print()
        elif(tokens[i+2] == "string"):
            a.append(tokens[i+4])
            ind = ind + 1
            print("Declared: " + a[ind - 1])
            print()
        elif(tokens[i+2] == "int"):
            a.append(tokens[i+4])
            ind = ind + 1
            print("Declared: " + a[ind - 1])
            print()
        else:
            print("Error: Unsupported Datatype")
            print()
        
    elif (tokens[i] == "Assign"):
        ita = 0
        flag3 = 1
        while ita < len(a):
            if(a[ita] == tokens[i+2]):
                a.insert(ita+1, tokens[i+4])
                ind = ind + 1
                print("Assigned Value: " + str(a[ita + 1]) + " to " + a[ita])
                print()
                flag3 = 0
            if(flag3 == 1):
                ita = ita + 1
            else:
                break
        if(flag3 == 1):
            print("Error: Variable not found")
            print()
        
    elif (tokens[i] == "Add"):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                print("Results after adding: " + str(exec1 + exec2))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                print("Results after adding: " + str(exec1 + tokens[i+4]))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float) or isinstance(tokens[i+2], str)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float) or isinstance(tokens[i+2], str))):
            print("Results after adding: " + str(tokens[i+2] + tokens[i+4]))
            print()
        else:
            print("Error: Wrong Syntax")
            print()
            
    elif(tokens[i] == "Subtract" and tokens[i-1] != '('):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                print("Results after subtracting: " + str(exec1 - exec2))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                print("Results after subtracting: " + str(exec1 - tokens[i+4]))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            print("Results after subtracting: " + str(tokens[i+2] - tokens[i+4]))
            print()
        else:
            print("Error: Wrong Syntax")
            print()
        
    elif(tokens[i] == "Multiply"):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                print("Results after multiplying: " + str(exec1 * exec2))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                print("Results after multiplying: " + str(exec1 * tokens[i+4]))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            print("Results after multiplying: " + str(tokens[i+2] * tokens[i+4]))
            print()
        else:
            print("Error: Wrong Syntax")
            print()
        
    elif(tokens[i] == "Divide"):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                print("Results after dividing: " + str(exec1 / exec2))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                print("Results after dividing: " + str(exec1 / tokens[i+4]))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            print("Results after dividing: " + str(tokens[i+2] / tokens[i+4]))
            print()
        else:
            print("Error: Wrong Syntax")
            print()
            
    elif(tokens[i] == "Mod"):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                print("Results after the mod operation: " + str(exec1 % exec2))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                print("Results after the mod operation: " + str(exec1 % tokens[i+4]))
                print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            print("Results after the mod operation: " + str(tokens[i+2] % tokens[i+4]))
            print()
        else:
            print("Error: Wrong Syntax")
            print()
        
    elif(tokens[i] == "Greater"):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                if(exec1 > exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                if(exec1 > exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            if(exec1 > exec2):
                print(True)
                print()
            else:
                print(False)
                print()
        else:
            print("Error: Wrong Syntax")
            print()
        
    elif(tokens[i] == "GreaterOrEqual"):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                if(exec1 >= exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                if(exec1 >= exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            if(exec1 >= exec2):
                print(True)
                print()
            else:
                print(False)
                print()
        else:
            print("Error: Wrong Syntax")
            print()
        
    elif(tokens[i] == "Smaller"):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                if(exec1 < exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                if(exec1 < exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            if(exec1 < exec2):
                print(True)
                print()
            else:
                print(False)
                print()
        else:
            print("Error: Wrong Syntax")
            print()
        
    elif(tokens[i] == "SmallerOrEqual"):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                if(exec1 <= exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                if(exec1 <= exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            if(exec1 <= exec2):
                print(True)
                print()
            else:
                print(False)
                print()
        else:
            print("Error: Wrong Syntax")
            print()
        
    elif(tokens[i] == "Equal"):
        ita = 0
        if(isalpha(tokens[i+2]) and isalpha(tokens[i+4])):
  
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                elif(a[ita] == tokens[i+4]):
                    exec2 = a[ita+1]
                    flag2 = 0
                ita = ita + 1
            if(flag1 == 0 and flag2 == 0):
                if(exec1 == exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif(isalpha(tokens[i+2]) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    exec1 = a[ita+1]
                    flag1 = 0
                ita = ita + 1
            if(flag1 == 0):
                if(exec1 == exec2):
                    print(True)
                    print()
                else:
                    print(False)
                    print()
            else:
                print("Error: The variable has not been declared yet")
                print()
                
        elif((isinstance(tokens[i+2], int) or isinstance(tokens[i+2], float)) and (isinstance(tokens[i+4], int) or isinstance(tokens[i+4], float))):
            if(exec1 == exec2):
                print(True)
                print()
            else:
                print(False)
                print()
        else:
            print("Error: Wrong Syntax")
            print()
        
    elif(tokens[i] == "Print"):
        if(isinstance(tokens[i+2], str) and len(tokens[i+2]) > 1):
            print(tokens[i+2])
            print()
        elif(isalpha(tokens[i+2])):
            ita = 0
            while ita < len(a):
                if(a[ita] == tokens[i+2]):
                    print("Variable: " + a[ita] + " has value of: " + str(a[ita+1]))
                    print()
                ita = ita + 1
        else:
            print("Error: Wrong Syntax") 
            print()  
        
    elif(tokens[i] == "DeclareAndAssign"):
        if(tokens[i+2] == "bool"):
            if(tokens[i+6] == True or tokens[i+6] == False):
                a.append(tokens[i+4])
                ind = ind + 1
                print("Declared: " + a[ind - 1])
                print()
                a.append(tokens[i+6])
                ind = ind + 1
                print("Assigned Value: " + str(a[ind - 1]) + " to " + a[ind - 2])
                print()
            else:
                print("Error: \"boolean\" datatype can only take values True and False")
                print()
        elif(tokens[i+2] == "string"):
            if(isalpha(tokens[i+6])):
                a.append(tokens[i+4])
                ind = ind + 1
                print("Declared: " + a[ind - 1])
                print()
                a.append(tokens[i+6])
                ind = ind + 1
                print("Assigned Value: " + str(a[ind - 1]) + " to " + a[ind - 2])
                print()
            else:
                print("Error: \"string\" datatype can only alphabetical characters")
                print()
        elif(tokens[i+2] == "int"):
            if((isinstance(tokens[i+6], int) or isinstance(tokens[i+6], float))):
                a.append(tokens[i+4])
                ind = ind + 1
                print("Declared: " + a[ind - 1])
                print()
                a.append(tokens[i+6])
                ind = ind + 1
                print("Assigned Value: " + str(a[ind - 1]) + " to " + a[ind - 2])
                print()
            else:
                print("Error: \"int\" datatype can only take numeric characters")
                print()
        else:
            print("Error: Unsupported Datatype")
            print()
        
    elif(tokens[i] == "If"):
        print("If")
        
    elif(tokens[i] == "Else"):
        print("Else")
        
    elif(tokens[i] == "here"): # goto
        print("here")
        
    elif(tokens[i] == "End"):
        print("Program Ended")
        print()
        break
        
    i = i + 1
