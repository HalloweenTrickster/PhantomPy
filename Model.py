from pathlib import Path

FPQ = Path(__file__).parent / "nodes" / "QANodes" / "questions"
FPA = Path(__file__).parent / "nodes" / "QANodes" / "answers"

questions = []
answers = []
usrin = ""

def grabData():
    global questions, answers

    with open(FPQ, 'r') as file:
        questions = [line.strip() for line in file.readlines()]
    with open(FPA, 'r') as file:
        answers = [line.strip() for line in file.readlines()]


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


def questionCheck():
    if usrin in questions:
        answer()

    else:
        failRespond()

while True:

    grabData()

    usrin = input(">> ").strip().lower()

    questionCheck()