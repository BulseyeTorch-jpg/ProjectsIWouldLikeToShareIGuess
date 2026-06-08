AlphaList = ["a","b","c","d","e","f","g",
	"h","i","j","k","l","m","n","o","p",
	"q","r","s","t","u","v",
	"w","x","y","z"]

MorseList = [".-","-...","-.-.","-..",".","..-.","--.",
	"....","..",".---","-.-",".-..","--","-.","---",".--.",
	"--.-",".-.","...","-","..-","...-",
	".--","-..-","-.--","--.."]

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
			case "."|"-" if Contact == True: 
				Filtered.append(Filtered.pop(-1)+B[i])
				Contact = True
			case " "|","|"/"|"\\": #2 \s = 1 \ cuz escaping or something idk
				Contact = False
			case _:
				Contact = False
	return Filtered
