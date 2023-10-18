from Question import Question


question_prompts = [
    "What color are apples? \n(a) Red \n(b) Purple \n(c)Orange \n\n",
    "What is your country? \n(a) Bangladesh \n(b) Nepal \n(c)India \n\n",
    "How old are you? \n(a) 20 \n(b) 30 \n(c)40 \n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_text(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correction")

run_text(questions)