def color(text:str, color:int=15, bgcolor:int=None):
    if bgcolor:
        return(f"\033[48;5;{bgcolor}m\033[38;5;{color}m{text}\033[0;0m")
    else:
        return(f"\033[38;5;{str(color)}m{str(text)}\033[0;0m")