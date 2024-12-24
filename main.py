# TODO: Add if statements

import os, sys, random

def output(message):
    print(message)
def ask(message):
    input(message)
def assign(variable , value):
    variable
    value
    variable = value
def varout(variable):
    try:
        output(variable)
    except:
        output("nah")
def rand(max):
    try:
        max = random.randint(0, int(max))
        error = False
    except:
        print("Error! Must use number only!")
        error = True
    if error == False:
        print(max)

os.system('clear')
print("Welcome to MemeScript!\nVersion 0.2.1\nType \"help()\" if you need assistance.")

while True:
    error = True
    token = input('> ')
    
    # Real commands #####################

    # Output command (doesn't require quotes)
    if token.startswith("output("):
        try:
            string = token.replace("output(", "", 1)
            string = string.replace(")", "", 1)
            output(string)
            error = False
        except:
            error = True
    
    # Output command (doesn't require quotes)
    if token.startswith("ask("):
        try:
            string = token.replace("ask(", "", 1)
            string = string.replace(")", "", 1)
            ask(string)
            error = False
        except:
            error = True

    # Output a variable
    if token.startswith("varout("):
        try:
            try:
                x = token.replace("varout(", "", 1)
                x = x.replace(")", "", 1)
                varout(value)
            except:
                print(variable)
            error = False
        except:
            error = True

    # Variable assignment (Only 1 variable at a time)
    if token.startswith("assign("):
        try:
            x = token.replace("assign(", "", 1)
            x = x.replace("assign(", "", 1)
            x = x.replace(")", "", 1)
            temp = x
            x = x.replace(", ", "", 1)

            original = temp
            index = original.find(", ") + 2
            value = original[index:]
            var = original[:index - 2]
            assign(var , value)
            error = False
        except:
            error = True
    
    # Generates a random number between 0 and your desired number
    if token.startswith('rand('):
        try:
            
            x = token.replace("rand(", "", 1)
            x = x.replace(")", "", 1)
            rand(x)

            error = False
        except:
            error = True

    if token.startswith('randvar('):
            
        x = token.replace("randvar(", "", 1)
        x = x.replace("randvar(", "", 1)
        x = x.replace(")", "", 1)
        temp = x
        x = x.replace(", ", "", 1)

        original = temp
        index = original.find(", ") + 2
        max = original[index:]
        var = original[:index - 2]
        x = random.randint(0 , int(max))
        variable = x
        error = False
    
    if token.startswith('askvar('):
        try:
            x = token.replace("askvar(", "", 1)
            x = x.replace("askvar(", "", 1)
            x = x.replace(")", "", 1)
            variable = input(x)
            error = False
        except:
            error = True
    # Other commands ####################
    
    if token == 'exit()':
        sys.exit()
    if token == 'cls()':
        try:
            os.system('clear')
            error = False
        except:
            error = True
    if token == 'help()':
        try:
            import other.help
            error = False
        except:
            error = True

    # End ###############################    
    if error == True:
        print("(Very unhelpful) error!Try typing \"help()\" or retype the line!")
