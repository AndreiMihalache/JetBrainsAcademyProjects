import random
#choices = ["rock", "paper", "scissors"]
name = input("Enter your name: ")
print("Hello, "+name)
points =0
file = open("rating.txt", 'r')
lines = file.readlines()
ok =0
score = 0
for line in lines:
    if name in line:
        el = line.split()
        score = int(el[1])
        ok=1
userchoices = input()
if userchoices == "":
  choices = ["rock", "paper", "scissors"]
else:
    choices = userchoices.split(",")
print("Okay, let's start")
ui = input()
while ui != "!exit":
    if ui == "!rating":
        print("Your rating: "+ str(score))
        ui = input()
        continue
    if ui not in choices:
        print("Invalid input")
    else:
        computer = random.choice(choices)
        lose = f"Sorry, but the computer chose {computer}"
        draw = f"There is a draw ({computer})"
        win = f"Well done. The computer chose {computer} and failed"
        rez = {"paper": -1, "rock": 0, "scissors": 1}
        if computer == ui:
            print(draw.format(computer))
            score +=50
        else:
            index = choices.index(ui)
            result = []
            for i in range(index+1, len(choices)):
                result.append(choices[i])
            if len(result)!=len(choices)-1  :
                for i in range(0, index):
                    result.append(choices[i])
            losslist = []
            winlist = []
            for i in range(len(result)//2):
                winlist.append(result[i])
            for i in range(len(result) // 2, len(result)):
                losslist.append(result[i])
            if computer in losslist:
                print(win.format(computer))
                score += 100
            else:
                print(lose.format(computer))
    ui = input()
file.close()
file = open("rating.txt", 'w')
if ok:
    for line in lines:
        if name in line:
            print(name,score, sep=" ", file = file)
        else:
            print(line, file = file)
else:
    for line in lines:
        print(line, file=file)
    print(name, score, sep=" ", file = file)
    file.close()
print("Bye!")