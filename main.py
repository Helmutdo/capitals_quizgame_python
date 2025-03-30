"""This is a simple quiz program that asks the user about the capitals of various countries"""

from questionaire import questions


def run_quiz(questions):
    """
    Run the quiz by iterating through the quiestions and checking the answers
    
    param questions : list of questions
    
    return : None
    """

    print("\nWelcome to the capitals quiz!\n")
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)

        # get user input only within A B C D
        while True:
            try:
                answer = input("Enter A, B, C or D: ").upper()
                if answer not in ["A", "B", "C", "D"]:
                    print("Please enter A, B, C or D only.")
                else:
                    break
            except ValueError as e:
                print(e)
        # check if answer is correct and increment score
        if answer == question["answer"]:
            score += 1

    print(f"Your score is {score} out of {len(questions)}")


run_quiz(questions)