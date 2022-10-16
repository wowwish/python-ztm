# CODE FILE TO BE TESTED

def do_stuff(num=0):
    try:
        if(num): # handle input being None
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err
