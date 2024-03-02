from random import choice, randint

def get_responce(user_input:str)->str:
    lower:str=user_input.lower()
    
    if lower=="help":
        return "This is a help message"
    elif lower=="about":
        return "This is a about message"
    elif lower=="roll":
        return str(randint(1,6))
    elif lower=="":
        return "Well you\'ve got to say something"
    else:
        return "I don't understand the command"

