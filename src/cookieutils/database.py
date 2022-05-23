import json
import base64

# ideas: Cookie User Memory 
# ideas: python external network index system <-- good 



class db():
    def __init__(self, temp=False, file="db"):

        # if temp = True then it will not save to a file and will instead just keep to memory, it will be faster (much faster becuase it does not need to write and read every time)

        self.__data = {}

        self.__temp = temp
        self.__file = file

    def __read_update(self):
        if not self.__temp:
            pass #.decode('base64')
    
    def __write_update(self):
        if not self.__temp:
            pass # str(base64.b64encode(data.encode("utf-8")), "utf-8")


    def __getitem__(self, index):      # allows getting items like  'foo = db['bar']
        self.__read_update()
        return self.__data[index]
    
    def __setitem__(self, key, value): # allows settings items like 'db['bar'] = "test"'
        self.__data[key] = value
        self.__write_update()

    def __repr__(self):
        return f"<Type: CookieDB>"
    
    def search(self, term, key=None, sub=False): 
        # sub is like looking at a sub value in a list of dicts, for example looking for a use with a spacific username
        
        # if key is set too none then it will look through all of the keys, it will automaticly not care about keyerrors 

        pass




