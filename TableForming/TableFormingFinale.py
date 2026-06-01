#Name of Wikipedia website used for this: Box-drawing Characters
#Characters used:   ━ ┏ ┓ ┗ ┛ ┃ ┠ ┨ ┷ ┯ ─ │ ┼
Middles, MiddlesT = int(0), int(0)
LNames, LCScores, LTScores = [], [], []
Decisions = bool(True)
#print(f" {'_oeoaa'*3}") this works

def LengthSort(Listed): 
    Longest = int(0)
    for i in range(len(Listed)): 
        if Longest < len(str(Listed[i])): 
            Longest = len(str(Listed[i]))
    return Longest

while Decisions == True: 
    Middles += 1 #Same as Middles = Middles + 1
    Name, CScore, TScore = str(input("Enter your name: ")), int(input("Score: ")), int(input("Total Score: "))
    LNames.append(Name), LCScores.append(CScore), LTScores.append(TScore)
    answer = str(input("Anyome else? [yes/no]"))
    Decisions = answer.lower()[0] == 'y'

NameL, CScoreL, TScoreL = LengthSort(LNames), LengthSort(LCScores), LengthSort(LTScores)
TheName, TheCScore, TheTScore = LNames[MiddlesT], str(LCScores[MiddlesT]), str(LTScores[MiddlesT])
FirstN, FirstCS, FirstTS = NameL - 4, CScoreL - 13, TScoreL - 11
if NameL - 4 < 0: 
    NameL = 4
if CScoreL - 13 < 0: 
    CScoreL = 13
if TScoreL - 11 < 0: 
    TScoreL = 11
BridgeN, BridgeCS, BridgeTS = NameL - len(TheName), CScoreL - len(TheCScore), TScoreL - len(TheTScore)

print("┏"+"━"*NameL+"┯"+"━"*CScoreL+"┯"+"━"*TScoreL+"┓")
print("┃"+" "*FirstN+"Name"+"│"+" "*FirstCS+"Current Score"+"│"+" "*FirstTS+"Total Score"+"┃")
print("┠"+"─"*NameL+"┼"+"─"*CScoreL+"┼"+"─"*TScoreL+"┨")
while Middles != MiddlesT: 
    TheName, TheCScore, TheTScore = LNames[MiddlesT], str(LCScores[MiddlesT]), str(LTScores[MiddlesT])
    BridgeN, BridgeCS, BridgeTS = NameL - len(TheName), CScoreL - len(TheCScore), TScoreL - len(TheTScore)
    MiddlesT += 1
    print("┃"+" "*BridgeN+TheName+"│"+" "*BridgeCS+TheCScore+"│"+" "*BridgeTS+TheTScore+"┃")
    if Middles != MiddlesT: 
        print("┠"+"─"*NameL+"┼"+"─"*CScoreL+"┼"+"─"*TScoreL+"┨")
print("┗"+"━"*NameL+"┷"+"━"*CScoreL+"┷"+"━"*TScoreL+"┛")
