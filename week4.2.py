def palindrome(word):
    #returns a boolean value if the argument is a palindrome, accepts 1 string type positional argument 
    a = 1
    for i in range(0,len(word)-1):
        if word[i] == word[-i-1]:
            pass
        #loops through 1st and last characters of the string, then 2nd and 2nd last etc. and passes if they match
        else:
            a = 0
            #gives a=0 which returns a false bool if any of the characters are mismatched         
    print(bool(a))    
palindrome("racecar")