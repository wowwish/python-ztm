# Finding and Removing Errors and bugs from Code - Debugging


# Linting - detects issues as you code, use IDEs with read-to-use linting
# Use good IDEs - autoformating based on PEP8 python style guide, code formatting, error detection, highlighting

# The built-in python debugger module - allows us to interact with the code and debug it interactively
# Type 'help' to see all available commands. You can also display values of variables using their name.l
# You can get help on a command by typing 'help <command>'. For example: 'help step' or 'help list'
# The command 'step' allows you to execute the next line of code below 'pdb.set_trace()'.
# The command 'next' also runs the next code line
# The command 'a' will print all arguments in the current function 'add' and the command 'w' will print the 
# current function name, the function call statement used to call it and the next code line that is 
# going to be executed
# You will also be able to change the values of arguments / variables by using '<var/arg name> = <value>'
# For example: "num2 = 'asdsad'" and check the if the value is changed using 'num2'

# Exit the pdb terminal using 'exit'

import pdb # step through your code and debug it

def add(num1, num2):
    pdb.set_trace()
    t = 4 * 5
    return num1 + num2

add(4, 5)