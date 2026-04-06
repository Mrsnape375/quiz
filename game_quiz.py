quiz = [
    ["What is your name?",["Snehil","Sachin","Rohit","Virat"],"Snehil"],
    ["How old are you?",["13","20","56","34"],"20"],
    ["What is your favourite colour?",["Red","Purple","Yellow","Violet","Green"],"Purple"],
    ["What is your favourite food?",["Mummy's food","Fast food","Street food","Healthy food"],"Mummy's food"],
    ["Are you going to be successful?",["Yes","Yes","Yes","Yes"],"Yes"]
]
score = 0
print("======= WELCOME TO GAME! =======")
for item in quiz:
    question = item[0]
    choice = item[1]
    answer = item[2]

    print(question)
    for i in range(len(choice)):
        print(f"{i+1}. {choice[i]}")

    user = input("Enter your answer(number): ")
    if user.isdigit():
        user = int(user)

        if 1 <= user <= len(choice):
            if choice[user - 1] == answer:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
        else:
            print("INVALID ANSWER NUMBER!")
    else:
        print("INVALID INPUT!")

print(f"Total score: {score}")

