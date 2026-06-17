AlphaList = [
	"a","b","c","d","e","f","g",
	"h","i","j","k",
    "l","m","n","o","p",
	"q","r","s","t","u","v",
	"w","x","y","z"
    ]
PreCiphered = input("Please enter your sentence: ")
Shift = int(input("By how much would you like to shift this sentence by? (Can be negative)"))
def Cipher(Alp, Pre, Num): 
    Ciphered = []
    for i in range(len(Pre)): 
        if Pre[i] == " ": 
            Ciphered.append(" ")
        else: 
            Place = 0
            while Alp[Place] != str.lower(Pre[i]): 
                Place += 1
                if Place > 25: 
                    return "This sentence cannot be shifted"
            Place += Num
            while Place > 25: 
                Place -= 26
            while Place < -26: 
                Place += 26
            if Pre[i].isupper() == True: 
                Ciphered.append(str.upper(Alp[Place]))
            else: 
                Ciphered.append(Alp[Place])
    return Ciphered
def Combine(Word): 
    Decluttered = " "
    Match = bool(False)
    for i in range(len(Word)): 
        if Match == False: 
            Decluttered = Word[i]
            Match = True
        elif Match == True: 
            Decluttered = Decluttered + Word[i]
    return Decluttered
Decoded = Cipher(AlphaList, PreCiphered, Shift)
Result = Combine(Decoded)
print(Result)
