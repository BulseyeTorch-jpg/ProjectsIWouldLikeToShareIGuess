MorseCodeList = [
	".-","-...","-.-.","-..",".","..-.","--.",
	"....","..",".---","-.-",".-..","--","-.","---",".--.",
	"--.-",".-.","...","-","..-","...-",
	".--","-..-","-.--","--..",
	".----""..---","...--","....-",".....",
	"-....","--...","---..","----.","-----",
	".-.-.-","--..--","..--..",".----.","-.-.--",
	"-..-.","---...","-.-.-.","-...-",".-.-.",
	"-....-","..--.-",".-..-.",".--.-."
	] 

EqualsList = [
	"a","b","c","d","e","f","g",
	"h","i","j","k","l","m","n","o","p",
	"q","r","s","t","u","v",
	"w","x","y","z",
	"1","2","3","4","5",
	"6","7","8","9","0",
	".",",","?","'","!",
	"/",":",";","=","+",
	"-","_",'"',"@"
	] #Had to use '' indentation for "
#is there still more?

def theListEning(A): 
	listA = []
	for i in range(len(A)): 
		listA.append(A[i])
	return listA

def MtoEfilter(B): 
	Contact = bool(False)
	Filtered = []
	for i in range(len(B)): 
		match B[i]:
			case "."|"-" if Contact == False: 
				Filtered.append(B[i])
				Contact = True
				Added = B[i]
			case "."|"-" if Contact == True: 
				Filtered.pop(-1)
				Filtered.append(Added+B[i])
				Added = Filtered[-1]
				Contact = True
			case " "|",":
				Contact = False
			case"/": 
				Contact = False
				Filtered.append("/")
			case _:
				Contact = False
	return Filtered

def EtoMfilter(B, Equ): 
	Filtered = []
	for i in range(len(B)): 
		counter = 0
		if B[i] == " ": 
			Filtered.append(" ")
		else: 
			while counter != len(Equ): 
				if Equ[counter] == str.lower(B[i]): 
					Filtered.append(B[i])
					counter = len(Equ)
				else: 
					counter += 1
	return Filtered

def Demorseify(C, Equ, Mor): 
	result = []
	for i in range(len(C)): 
		counter = 0
		if C[i] == "/": 
			result.append(" ")
		else: 
			while C[i] != Mor[counter]: 
				counter += 1
				if i == len(C) and C[i] != Mor[counter]: 
					return "This statement is invalid."
			result.append(Equ[counter])
	return result
def Morseify(C, Equ, Mor): 
	result = []
	for i in range(len(C)): 
		counter = 0
		if C[i] == " ": 
			result.append("/")
		else: 
			while C[i] != Equ[counter]: 
				counter += 1
				if i == len(C) and C[i] != Equ[counter]: 
					return "This statement is invalid."
			result.append(Mor[counter])
	return result

def translation(Equals, Morse): 
	Choice = input("Are you translating to or from morse code?")
	if str.lower(Choice[0]) == "f": 
		Morseified = str(input("Insert the morse code sentence you would like to translate:"))
		print(Morseified)
		Peeled = theListEning(Morseified)
		Baked = MtoEfilter(Peeled)
		print(Baked)
		Output = Demorseify(Baked, Equals, Morse)
	elif str.lower(Choice[0]) == "t": 
		Morseified = str(input("Insert the sentence you would like to translate into morse code:"))
		print(Morseified)
		Peeled = theListEning(Morseified)
		Baked = EtoMfilter(Peeled, Equals)
		print(Baked)
		Output = Morseify(Baked, Equals, Morse)
	else: 
		print("That's an invalid option. Please try again.")
		Output = translation(Equals, Morse)
	return Output

MorseCodeTranslatorOutput = translation(EqualsList, MorseCodeList)
print(MorseCodeTranslatorOutput)
#I might add more characters IF there are any more that are in Morse code
#Still quite a few bugs
