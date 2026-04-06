#QUIZ GAME USING PYTHON


import math


Questions=("What is your name?",
           "How old are you?",
           "what do u like the most in the world",
           "What is your most favourite colour?",
           "what is your most favourite food?")
Options=(("A.Snehil","B.Sachin","C.Rohit","D.Virat"),
         ("A.15","B.18","C.21","D.19"),
         ("A.Mummy","B.Food","C.Me","D.Sleep"),
         ("A.Red","B.Purple","C.Orange","D.Black"),
         ("A.Mummy Food","B.Fast food","C.Healthy food","D.Japanese food"))
Answers=('A','D','A','B','A')
guesses=()
qstnno=[]
score=0
for question in Questions:
    print("------------------")
    print(question)
    for option in Options[qstnno]:
        print(option)
    guess=input("Choose the correct option...").upper()
    if guess== Answers[qstnno]:
        print("CORRECT!")
        score+=1
    else:
        print("INCORRECT!")
    qstnno+=1
print(f"Total score: {score}")