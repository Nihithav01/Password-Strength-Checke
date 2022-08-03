
NIHITHA VEMULAPALLI <nihithavemulapalli@gmail.com>
19:08 (1 hour ago)
to me

def Get_Score(password):
    print("\nPassword : " + str(password))
    t = 0
    sugg = []
    uppercaseLetter = 0
    lowercaseLetter = 0
    specialCharacter = 0
    number = 0
    underscore = 0
    brackets = 0
    #Checking password length
    if len(password) > 8:
        t= t+2
    else:
        sugg.append("Length Should Be More Than 8")
    #Assigning score
    for i in password:
        if i.isdigit():
           number = 1
        if i.isupper():
            uppercaseLetter = 1
        if i.islower():
            lowercaseLetter = 1
        if i in ['!', '@', '#', '$', '%', '&']:
            specialCharacter = 2
        if i == "_":
            underscore = 1
        if i in ['(', ')', '{', '}', '[', ']', '<', '>']:
            brackets = 2
    #strong password Suggestion
    if number == 0:
        sugg.append("Add Numbers")
    if lowercaseLetter == 0:
        sugg.append("Add Lower Case Letters")
    if uppercaseLetter == 0:
        sugg.append("Add Upper Case letters")
    if specialCharacter == 0:
        sugg.append("Add Special Character ! @ # $ % &")
    if underscore == 0:
        sugg.append("Add Underscore")
    if brackets == 0:
        sugg.append("Add Brackets ( ) { } [ ] < >")
    return sugg,(t+number+uppercaseLetter+lowercaseLetter+specialCharacter+underscore+brackets)
password = input("Enter Passwords : ")
suggestion,score = Get_Score(password)
if score <= 3:
    print("Strength : Weak")
elif score <= 6 and score > 3:
    print("Strength : Medium")
else:
    print("Strength : Strong")
if score == 10:
    print("Status : Valid Passwords")
else:
    print("Status : Invalid Passwords")
    print("\n\tPassword Suggestion : ")
    print(*suggestion, sep = "\n")
