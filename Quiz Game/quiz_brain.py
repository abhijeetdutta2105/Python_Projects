# TODO 1: asking the question : next_question() method

# TODO 2: checking if the answer is correct : is_correct() method

# TODO 3: checking if we are at the end of the quiz : still_has_question() method

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question_text = self.question_list[self.question_number].text
        self.question_number += 1
        return input(f"Q.{self.question_number}: {question_text} (True/False)?: ").title()


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def is_correct(self):
        correct_answer = self.question_list[self.question_number].answer
        if self.next_question() == correct_answer:
            self.score += 1
            print("Congrats! You got it right")
        else:
            print("Sorry! You got it wrong")
        print(f"The correct answer: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}\n")


    def exit_quiz(self):
        print("You've completed the quiz")
        print(f"Your final score is : {self.score}/{self.question_number}")


