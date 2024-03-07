import sys


def Checkfor_S(phrase):
    key = "ss"
    if key in phrase:
        return True
    else:
        return False


        
    
        
            

def main():
    phrase = input()
    
    Checkfor_S(phrase) 
    
    if Checkfor_S(phrase) == True:
        print("hiss")
    else:
        print("no hiss")
    
    
main()