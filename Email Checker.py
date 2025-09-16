check = False
counter = 0
foundAt = -1
foundDot = -1

while check is False:
    email = str(input("What is your email?: "))
    for i in range(0, len(email)):
        print(email[i])
        
        if (email[i]=='@'):
            print("Found @ at: ", i)
            counter += 1 
            foundAt = i
        
        if (email[i]=='.'):
            print("Found . at: ", i)
            foundDot = i
    
    if (foundAt>0 and foundDot>foundAt + 3 and foundDot<len((email)) - 2):
         print("Email is good!!")
         check = True
        
    if counter != 1:
        print("That is not a correct email")
        counter = 0 
        
        



