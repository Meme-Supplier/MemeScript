import os, sys

os.system('clear')

def output(message):
    print(message)
def ask(message):
    input(message)
def assign(variable , value):
    #x = value
    #y = variable
    variable = value
    #print("Variable",y,"set to",x)
def varout(variable):
    try:
        output(variable)
    except:
        output("nah")

print("Welcome to MemeScript!\nVersion 0.1\nType \"help()\" if you need assistance.")

while True:
    error = True
    token = input('> ')
    
    # Real commands #####################

    # Output command (doesn't require quotes)
    if token.startswith("output("):
        
        string = token.replace("output(", "", 1)
        string = string.replace(")", "", 1)
        output(string)
        error = False
    
    # Output command (doesn't require quotes)
    if token.startswith("ask("):
        
        string = token.replace("ask(", "", 1)
        string = string.replace(")", "", 1)
        ask(string)
        error = False

    # Output a variable
    if token.startswith("varout("):
        
        x = token.replace("varout(", "", 1)
        x = x.replace(")", "", 1)
        varout(value)
        error = False

    # Variable assignment (Only 1 variable at a time)
    if token.startswith("assign("):

        x = token.replace("assign(", "", 1)
        x = x.replace("assign(", "", 1)
        x = x.replace(")", "", 1)
        temp = x
        x = x.replace(", ", "", 1)

        original = temp
        # Find the starting index of ", "
        index = original.find(", ") + 2  # After ", "
        value = original[index:]
        var = original[:index - 2]
        # part = Value
        # original = Variable
        assign(var , value)
        error = False

    # Other commands ####################
    
    if token == 'exit()':
        sys.exit()
        error = False
    if token == 'cls()':
        os.system('clear')
        error = False
    if token == 'help()':
        import other.help
        error = False

    # End ###############################    
    if error == True:
        print("Error! Try typing \"help()\"")