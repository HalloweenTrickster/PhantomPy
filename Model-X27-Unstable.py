from pathlib import Path

FPQ = Path(__file__).parent / "nodes" / "QANodes" / "questions"
FPA = Path(__file__).parent / "nodes" / "QANodes" / "answers"
CI = Path(__file__).parent / "nodes" / "CNodes" / "contextin"
CO = Path(__file__).parent / "nodes" / "CNodes" / "contextout"

questions = []
answers = []
contextin = []
contextout = []
usrin = ""

def grabData():
    global questions, answers

    with open(FPQ, 'r') as file:
        questions = [line.strip() for line in file.readlines()]
    with open(FPA, 'r') as file:
        answers = [line.strip() for line in file.readlines()]

    if len(questions) != len(answers):
        print("WARNING: Questions and Answers nodes out of sync!")


def answer():
    index = questions.index(usrin)
    print(answers[index])


def failRespond():
    print("I'm not too sure what I should respond with.")

    usrin2 = input("Type: ").strip()

    with open(FPQ, 'a') as file:
        file.write("\n" + usrin)

    with open(FPA, "a") as file:
        file.write("\n" + usrin2)


def contextcheck():
    global contextin, contextout
    with open(CI, 'r') as file:
        contextin = [line.strip() for line in file.readlines()]
    with open(CO, 'r') as file:
        contextout = [line.strip() for line in file.readlines()]
        
    if usrin in contextout:
        #something here.



def questionCheck():
    if usrin in questions:
        answer()
        contextanswer = Uhhhh whatever the last thingy was.

    else:
        failRespond()

while True:
    grabData()
    usrin = input(">> ").strip().lower()
    questionCheck()