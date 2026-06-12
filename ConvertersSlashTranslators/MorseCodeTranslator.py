AlphaList = ["a","b","c","d","e","f","g",
	"h","i","j","k","l","m","n","o","p",
	"q","r","s","t","u","v",
	"w","x","y","z"] #Maybe add more

MorseList = [".-","-...","-.-.","-..",".","..-.","--.",
	"....","..",".---","-.-",".-..","--","-.","---",".--.",
	"--.-",".-.","...","-","..-","...-",
	".--","-..-","-.--","--.."] #Maybe add more (Found an 'International' morse list)

def theListEning(A): 
	listA = []
	for i in range(len(A)): 
		listA.append(A[i])
	return listA
def Mfilter(B): 
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
				Filtered.append(" ")
			case _:
				Contact = False
	return Filtered

def Demorseify(C, Alp, Mor): 
	result = []
	for i in range(len(C)): 
		pass

Morseified = str(input("Insert the morse code sentence you would like to translate:"))
print(Morseified)
Peeled = theListEning(Morseified)
Baked = Mfilter(Peeled)
print(Baked)
#Just add the main translation and repeat stuff for english --> morse 
#May also wanna add more morse letters if I feel like it
